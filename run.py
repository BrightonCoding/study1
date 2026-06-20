#!/usr/bin/env python3
"""
run.py — single orchestrator / CLI. Each stage can be run independently.

Stages:
  smoke       M1: collect a small sample (config collection.smoke) -> video_panel head
  collect     M3: collect the full seed list -> raw cache (+ light video panel)
  embed       M2: compute & cache thumbnail/title embeddings
  features    build homogeneity scores + engagement features
  panel       assemble the two tidy parquet panels + data dictionary
  analyze     M4: run the econometric analysis -> tables/plots/FINDINGS.md
  rescrape    M5: append a fresh snapshot of known video ids (cron daily)
  discover    expand the seed list via niche keyword search (writes seed CSV)

Usage:
  python run.py smoke
  python run.py collect
  python run.py analyze
  python run.py --config config.yaml smoke
"""
from __future__ import annotations

import argparse
import sys

from src.config import load_config, ensure_dirs
from src.logging_setup import get_logger


def _collect_sample(cfg, log, max_channels: int, videos_per_channel: int, tag: str):
    """Shared collection routine for both `smoke` and full `collect`."""
    import pandas as pd

    from src.collect import make_collector
    from src import seeds

    seed_df = seeds.load_seed_channels(cfg)
    refs = seed_df["channel_ref"].tolist()[:max_channels]
    log.info(f"[{tag}] collecting {len(refs)} channels x <= {videos_per_channel} videos")

    from concurrent.futures import ThreadPoolExecutor

    collector = make_collector(cfg, log)
    channel_records: list[dict] = []
    video_records: list[dict] = []

    # --- Phase 1: per-channel header + video listing (sequential; one cheap call each) ---
    tasks: list[tuple[str, str, dict]] = []  # (channel_ref, video_id, cmeta)
    for i, ref in enumerate(refs, 1):
        cmeta = collector.get_channel_metadata(ref)
        if cmeta is None:
            log.warning(f"[{tag}] ({i}/{len(refs)}) skipping {ref}: no channel metadata")
            continue
        listing = collector.list_channel_videos(ref, videos_per_channel)
        log.info(f"[{tag}] ({i}/{len(refs)}) {ref}: listed {len(listing)} videos")
        cmeta["n_videos_listed"] = len([v for v in listing if v.get("video_id")])
        cmeta["n_videos_collected"] = 0
        channel_records.append(cmeta)
        for v in listing:
            if v.get("video_id"):
                tasks.append((ref, v["video_id"], cmeta))

    # --- Phase 2: per-video full metadata (backend-optimal: batched for API) ---
    dl_thumbs = bool(cfg.collection.download_thumbnails)
    workers = max(1, collector.concurrency)
    all_ids = [vid for (_, vid, _) in tasks]
    log.info(f"[{tag}] fetching metadata for {len(all_ids)} videos "
             f"(backend={cfg.collection.backend}, concurrency={workers})")
    meta_by_id = collector.get_videos_metadata(all_ids)
    log.info(f"[{tag}] got metadata for {len(meta_by_id)}/{len(all_ids)} videos")

    # --- Phase 3: post-process + thumbnail download (parallel; network-bound) ---
    cmeta_by_ref = {c["channel_ref"]: c for c in channel_records}

    def _post(task):
        ref, vid, cmeta = task
        vmeta = meta_by_id.get(vid)
        if vmeta is None:
            return None
        if vmeta.get("subscriber_count") is None:
            vmeta["subscriber_count"] = cmeta.get("subscriber_count")
        vmeta["channel_ref"] = ref
        if dl_thumbs:
            url, path = collector.download_thumbnail(vid, vmeta)
            vmeta["thumbnail_url"] = url
            vmeta["thumbnail_path"] = path
        return vmeta

    counts: dict[str, int] = {}
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for vmeta in ex.map(_post, tasks):
            done += 1
            if done % 1000 == 0:
                log.info(f"[{tag}]   post-processed {done}/{len(tasks)}")
            if vmeta is None:
                continue
            video_records.append(vmeta)
            counts[vmeta["channel_ref"]] = counts.get(vmeta["channel_ref"], 0) + 1
    for cmeta in channel_records:
        cmeta["n_videos_collected"] = counts.get(cmeta["channel_ref"], 0)

    vdf = pd.DataFrame(video_records)
    cdf = pd.DataFrame(channel_records)

    # engagement features that don't need embeddings (so the smoke panel is already useful)
    if not vdf.empty:
        vdf = _add_basic_engagement(vdf)
        # drop the bulky thumbnails blob from the tabular panel (kept in raw JSON cache)
        vdf = vdf.drop(columns=[c for c in ["thumbnails", "thumbnail"] if c in vdf.columns])

    log.info(
        f"[{tag}] DONE. channels={len(cdf)} videos={len(vdf)} | "
        f"net_calls={collector.stats['net_calls']} cache_hits={collector.stats['cache_hits']} "
        f"failures={collector.stats['failures']}"
    )
    return cdf, vdf


def _add_basic_engagement(vdf):
    """Age-robust engagement + log transforms. (Embedding features added later.)"""
    import numpy as np

    v = vdf["view_count"]
    likes = vdf["like_count"]
    comments = vdf["comment_count"]
    # engagement_rate = (likes + comments) / views  -> PRIMARY, age-robust outcome.
    # nulls (disabled likes/comments) propagate to NaN rather than being treated as 0.
    denom = v.where(v > 0)
    vdf["engagement_rate"] = (likes + comments) / denom
    vdf["like_rate"] = likes / denom
    vdf["comment_rate"] = comments / denom
    vdf["log_views"] = np.log1p(v)
    vdf["log_subscribers"] = np.log1p(vdf["subscriber_count"])
    # log age (+1 day) — every raw-views model MUST control for this
    vdf["log_days_since_upload"] = np.log1p(vdf["days_since_upload"].clip(lower=0))
    return vdf


def cmd_smoke(cfg, log):
    import pandas as pd

    pd.set_option("display.max_columns", 40)
    pd.set_option("display.width", 200)

    sm = cfg.collection.smoke
    cdf, vdf = _collect_sample(
        cfg, log, int(sm.max_channels), int(sm.videos_per_channel), tag="SMOKE"
    )
    if vdf.empty:
        log.error("smoke produced 0 videos — check network / yt-dlp install")
        return 1

    out_v = cfg.path("panels_dir") / "smoke_video_panel.parquet"
    out_c = cfg.path("panels_dir") / "smoke_channel_panel.parquet"
    vdf.to_parquet(out_v, index=False)
    cdf.to_parquet(out_c, index=False)

    # ---- console report (this is what the user reviews for M1) ----
    cols = [
        "channel_ref", "video_id", "title", "upload_date", "days_since_upload",
        "duration_seconds", "is_short", "view_count", "like_count", "comment_count",
        "engagement_rate", "subscriber_count",
    ]
    cols = [c for c in cols if c in vdf.columns]
    print("\n" + "=" * 100)
    print("M1 SMOKE TEST — VIDEO-LEVEL PANEL (head)")
    print("=" * 100)
    print(vdf[cols].head(15).to_string(index=False))

    print("\n" + "=" * 100)
    print("PER-CHANNEL COUNTS")
    print("=" * 100)
    per_ch = (
        vdf.groupby("channel_ref")
        .agg(
            videos=("video_id", "count"),
            shorts=("is_short", "sum"),
            median_views=("view_count", "median"),
            median_eng_rate=("engagement_rate", "median"),
            subs=("subscriber_count", "max"),
        )
        .reset_index()
    )
    print(per_ch.to_string(index=False))

    print("\n" + "=" * 100)
    print("DATA HEALTH / MISSINGNESS")
    print("=" * 100)
    print(f"channels: {len(cdf)}   videos: {len(vdf)}   shorts flagged: {int(vdf['is_short'].sum())}")
    miss = vdf[["view_count", "like_count", "comment_count", "upload_date"]].isna().sum()
    print("null counts:\n" + miss.to_string())
    print(f"\nsaved: {out_v}")
    print(f"saved: {out_c}")
    return 0


def cmd_discover(cfg, log):
    from src.collect import discover_channels_by_search
    from src import seeds

    n_per = int(cfg.niche.get("discover_per_keyword", 40))
    chans = discover_channels_by_search(
        cfg, log, list(cfg.niche.search_keywords), n_per_keyword=n_per
    )
    n = seeds.merge_discovered_into_seed(cfg, chans, log)
    log.info(f"discover: {len(chans)} found; seed CSV now has {n} channels")
    return 0


def cmd_collect(cfg, log):
    c = cfg.collection
    cdf, vdf = _collect_sample(
        cfg, log, int(c.max_channels), int(c.videos_per_channel), tag="COLLECT"
    )
    if vdf.empty:
        log.error("collect produced 0 videos — check network / seed list")
        return 1
    out_v = cfg.path("panels_dir") / "raw_video_panel.parquet"
    out_c = cfg.path("panels_dir") / "raw_channel_panel.parquet"
    vdf.to_parquet(out_v, index=False)
    cdf.to_parquet(out_c, index=False)
    log.info(f"collect: saved {out_v} ({len(vdf)} videos, {len(cdf)} channels)")
    # quick health summary to console
    print("\n" + "=" * 80)
    print(f"COLLECT DONE — {len(vdf)} videos across {len(cdf)} channels")
    print("=" * 80)
    print(f"shorts flagged: {int(vdf['is_short'].sum())}")
    print(f"null like_count: {int(vdf['like_count'].isna().sum())}  "
          f"null comment_count: {int(vdf['comment_count'].isna().sum())}")
    print("videos collected per channel (describe):")
    print(cdf["n_videos_collected"].describe().round(1).to_string())
    return 0


def _not_yet(stage):
    def _fn(cfg, log):
        log.error(f"stage '{stage}' is implemented in a later milestone — not available yet")
        return 2

    return _fn


def cmd_embed(cfg, log):
    from src import embed

    summary = embed.run_embeddings(cfg, log)
    panels = embed.make_sanity_panels(cfg, log, variant="thumbnail")
    print("\n" + "=" * 80)
    print("M2 EMBEDDINGS — cached vector counts per variant")
    print("=" * 80)
    for k, v in summary.items():
        print(f"  {k:10s}: {v} videos")
    print("\nthumbnail-tile sanity panels written:")
    for p in panels:
        print(f"  {p}")
    return 0


def cmd_buildraw(cfg, log):
    from src import build_panel

    df = build_panel.assemble_raw_from_cache(cfg, log)
    print(f"\nraw panel rebuilt from cache: {len(df)} videos, {df['channel_ref'].nunique()} channels")
    return 0


def cmd_panel(cfg, log):
    from src import build_panel

    res = build_panel.main(cfg, log)
    print("\n" + "=" * 80)
    print("M3 PANELS BUILT")
    print("=" * 80)
    print(f"  video-level rows : {res['videos']}")
    print(f"  channel-week rows: {res['channel_weeks']}")
    print(f"  data dictionary  : docs/data_dictionary.md")
    return 0


def cmd_analyze(cfg, log):
    from src import analyze

    res = analyze.main(cfg, log)
    print("\n" + "=" * 80)
    print("M4 ANALYSIS COMPLETE")
    print("=" * 80)
    print(f"  coefficient rows : {res['models']}")
    print(f"  tables           : outputs/tables/all_coefficients.csv, model_summaries.md")
    print(f"  findings         : outputs/FINDINGS.md")
    print(f"  plots            : outputs/plots/")
    return 0


def cmd_rescrape(cfg, log):
    from src import rescrape

    rescrape.main(cfg, log)
    return 0


COMMANDS = {
    "smoke": cmd_smoke,
    "discover": cmd_discover,
    "collect": cmd_collect,
    "buildraw": cmd_buildraw,         # rebuild raw panel from JSON cache (crash/throttle recovery)
    "embed": cmd_embed,               # M2
    "features": cmd_panel,            # features are built as part of the panel stage
    "panel": cmd_panel,               # M3
    "analyze": cmd_analyze,           # M4
    "rescrape": cmd_rescrape,         # M5
}


def main(argv=None):
    p = argparse.ArgumentParser(description="Study 1 orchestrator")
    p.add_argument("stage", choices=list(COMMANDS))
    p.add_argument("--config", default=None, help="path to config.yaml")
    args = p.parse_args(argv)

    cfg = load_config(args.config)
    ensure_dirs(cfg)
    log = get_logger(args.stage, cfg.path("logs_dir"))
    log.info(f"=== stage '{args.stage}' | niche={cfg.niche.name} | backend={cfg.collection.backend} ===")
    return COMMANDS[args.stage](cfg, log)


if __name__ == "__main__":
    sys.exit(main())
