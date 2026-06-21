"""
build_panel.py — M3. Assemble the two tidy parquet panels + data dictionary.

  1. VIDEO-LEVEL panel  (paths.video_panel_parquet): one row per video with engagement,
     age, channel covariates, title features, and homogeneity scores (all variants).
  2. CHANNEL-WEEK panel (paths.channel_week_panel_parquet): aggregated to (channel, ISO-week)
     with mean homogeneity, mean engagement_rate, upload counts, subscriber_count, and a
     week-level pairwise homogeneity (mean pairwise cosine among that week's uploads).

Also (re)writes docs/data_dictionary.md describing every column.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import features as F
from .config import Cfg
from .embed import embeddings_as_dict
from .logging_setup import get_logger


def assemble_raw_from_cache(cfg: Cfg, log) -> pd.DataFrame:
    """Rebuild raw_video_panel.parquet from the on-disk JSON cache (the source of truth).

    The collector caches each video/channel response as JSON keyed by id. This makes the
    cache — not a single in-memory run — authoritative, so a crashed/killed/throttled
    collection is fully recoverable: we just re-derive the panel from whatever is cached.
    Re-derives channel_ref (via channel_id->ref map), thumbnail_path (from the thumbnail
    cache), and the basic engagement features.
    """
    import json
    import numpy as np

    vids_dir = cfg.path("raw_dir") / "videos"
    chans_dir = cfg.path("raw_dir") / "channels"
    thumbs_dir = cfg.path("thumbnails_dir")

    # channel_id -> channel metadata (incl. channel_ref = the seed reference used)
    chan_by_id: dict[str, dict] = {}
    for p in chans_dir.glob("*.json"):
        try:
            c = json.loads(p.read_text())
            if c.get("channel_id"):
                chan_by_id[c["channel_id"]] = c
        except (json.JSONDecodeError, OSError):
            continue

    rows = []
    for p in vids_dir.glob("*.json"):
        try:
            v = json.loads(p.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        cid = v.get("channel_id")
        cmeta = chan_by_id.get(cid, {})
        v["channel_ref"] = v.get("channel_ref") or cmeta.get("channel_ref") or cid
        if v.get("subscriber_count") is None:
            v["subscriber_count"] = cmeta.get("subscriber_count")
        tp = thumbs_dir / f"{v.get('video_id')}.jpg"
        v["thumbnail_path"] = str(tp) if tp.exists() else None
        v["thumbnail_url"] = v.get("thumbnail")
        v.pop("thumbnails", None)
        rows.append(v)

    df = pd.DataFrame(rows)
    if df.empty:
        raise RuntimeError("no cached videos found to assemble")

    # basic age-robust engagement features (same definitions as the collect stage)
    vv = df["view_count"]
    denom = vv.where(vv > 0)
    df["engagement_rate"] = (df["like_count"] + df["comment_count"]) / denom
    df["like_rate"] = df["like_count"] / denom
    df["comment_rate"] = df["comment_count"] / denom
    df["log_views"] = np.log1p(vv)
    df["log_subscribers"] = np.log1p(df["subscriber_count"])
    df["log_days_since_upload"] = np.log1p(df["days_since_upload"].clip(lower=0))

    out_v = cfg.path("panels_dir") / "raw_video_panel.parquet"
    df.to_parquet(out_v, index=False)

    # channel panel with collected counts
    counts = df.groupby("channel_ref")["video_id"].count().rename("n_videos_collected")
    cdf = pd.DataFrame(list(chan_by_id.values()))
    if not cdf.empty:
        cdf = cdf.merge(counts, on="channel_ref", how="right") if "channel_ref" in cdf.columns else cdf
    cdf.to_parquet(cfg.path("panels_dir") / "raw_channel_panel.parquet", index=False)

    log.info(f"assembled raw panel from cache: {len(df)} videos, "
             f"{df['channel_ref'].nunique()} channels -> {out_v}")
    return df


def _load_raw_video_panel(cfg: Cfg) -> pd.DataFrame:
    p = cfg.path("panels_dir") / "raw_video_panel.parquet"
    if not p.exists():
        # fall back to the smoke panel so M3 code is testable before the full collect
        p = cfg.path("panels_dir") / "smoke_video_panel.parquet"
    if not p.exists():
        raise FileNotFoundError("no collected video panel found; run `collect` (or `smoke`) first")
    return pd.read_parquet(p)


def _upload_frequency(df: pd.DataFrame) -> pd.Series:
    """Uploads per week per channel over the observed window (>=1 week). Maps to each row."""
    g = df.groupby("channel_ref")["upload_date"]
    spans = g.agg(lambda s: max((pd.to_datetime(s).max() - pd.to_datetime(s).min()).days / 7.0, 1.0))
    counts = g.count()
    freq = (counts / spans).rename("upload_frequency")
    return df["channel_ref"].map(freq)


def _week_pairwise_homogeneity(
    df: pd.DataFrame, emb: dict[str, np.ndarray], min_uploads: int
) -> pd.Series:
    """Mean pairwise cosine among a (channel, iso_week) group's videos (>=min_uploads)."""
    out = {}
    for (ch, wk), sub in df.groupby(["channel_ref", "iso_week"]):
        vids = [v for v in sub["video_id"] if v in emb]
        if len(vids) < max(2, min_uploads):
            continue
        M = F._norm_rows(np.vstack([emb[v] for v in vids]))
        S = M @ M.T
        iu = np.triu_indices(len(vids), k=1)
        out[(ch, wk)] = float(S[iu].mean())
    idx = pd.MultiIndex.from_tuples(out.keys(), names=["channel_ref", "iso_week"]) if out else None
    return pd.Series(list(out.values()), index=idx, dtype=float) if out else pd.Series(dtype=float)


def build_video_panel(cfg: Cfg, log) -> pd.DataFrame:
    df = _load_raw_video_panel(cfg)
    df = df.dropna(subset=["video_id"]).drop_duplicates(subset=["video_id"]).reset_index(drop=True)
    log.info(f"video panel: {len(df)} videos, {df['channel_ref'].nunique()} channels")

    # derived covariates
    df["iso_week"] = df["upload_date"].apply(F.iso_week)
    df["upload_frequency"] = _upload_frequency(df)

    # title features
    df = F.add_title_features(df)

    # homogeneity features (all variants)
    emb_by_variant = {v: embeddings_as_dict(cfg, v) for v in F.VARIANTS}
    have = {k: len(d) for k, d in emb_by_variant.items()}
    log.info(f"embeddings available: {have}")
    df = F.add_homogeneity_features(cfg, df, emb_by_variant)
    df = F.add_exposure_features(cfg, df, emb_by_variant)  # wear-out: cumulative exposure

    out = cfg.path("video_panel_parquet")
    df.to_parquet(out, index=False)
    log.info(f"saved video panel -> {out}  ({df.shape[0]} rows x {df.shape[1]} cols)")
    return df


def build_channel_week_panel(cfg: Cfg, log, vdf: pd.DataFrame) -> pd.DataFrame:
    min_uploads = int(cfg.features.min_uploads_for_week)
    emb_by_variant = {v: embeddings_as_dict(cfg, v) for v in F.VARIANTS}

    # aggregate engagement + per-video homogeneity means to (channel, week)
    agg = {
        "engagement_rate": "mean",
        "like_rate": "mean",
        "comment_rate": "mean",
        "log_views": "mean",
        "view_count": "median",
        "days_since_upload": "mean",
        "subscriber_count": "max",
        "upload_frequency": "first",
        "video_id": "count",
    }
    for variant in F.VARIANTS:
        for base in ("formula_adherence", "rolling_homogeneity", "niche_adherence"):
            col = f"{base}_{variant}"
            if col in vdf.columns:
                agg[col] = "mean"
    cw = vdf.groupby(["channel_ref", "iso_week"]).agg(agg).rename(
        columns={"video_id": "n_uploads"}
    )

    # week-level pairwise homogeneity (the channel-week homogeneity (b) measure)
    for variant in F.VARIANTS:
        emb = emb_by_variant.get(variant, {})
        if not emb:
            continue
        s = _week_pairwise_homogeneity(vdf, emb, min_uploads)
        cw[f"week_pairwise_homogeneity_{variant}"] = s

    cw = cw.reset_index()
    # add channel_id for clustering/joins
    chan_map = vdf.dropna(subset=["channel_id"]).groupby("channel_ref")["channel_id"].first()
    cw["channel_id"] = cw["channel_ref"].map(chan_map)

    out = cfg.path("channel_week_panel_parquet")
    cw.to_parquet(out, index=False)
    log.info(f"saved channel-week panel -> {out}  ({cw.shape[0]} rows x {cw.shape[1]} cols)")
    return cw


def write_data_dictionary(cfg: Cfg, vdf: pd.DataFrame, cw: pd.DataFrame) -> str:
    path = cfg.root / "docs" / "data_dictionary.md"
    descriptions = {
        "video_id": "YouTube video id (primary key).",
        "channel_id": "YouTube channel id (UC...).",
        "channel_ref": "Seed reference used to fetch the channel (@handle or URL).",
        "channel_title": "Channel display name.",
        "title": "Video title (raw).",
        "description": "Video description (raw).",
        "upload_date": "Upload date (ISO YYYY-MM-DD).",
        "duration_seconds": "Video duration in seconds.",
        "view_count": "Accumulated views AT SCRAPE TIME (snapshot, age-dependent).",
        "like_count": "Accumulated likes at scrape time; null if disabled.",
        "comment_count": "Accumulated comments at scrape time; null if disabled.",
        "like_count_is_null": "Flag: likes were unavailable/disabled.",
        "comment_count_is_null": "Flag: comments were unavailable/disabled.",
        "subscriber_count": "Channel subscriber count at scrape time.",
        "tags": "Video tags (list) if present.",
        "is_short": "Flag: detected YouTube Short (duration<=short_max_seconds or shorts source).",
        "was_live": "Flag: video was a livestream.",
        "availability": "yt-dlp availability field (public/unlisted/...).",
        "scrape_date": "UTC date the snapshot was taken.",
        "days_since_upload": "scrape_date - upload_date, in days (age control).",
        "thumbnail_url": "URL of the highest-res thumbnail fetched.",
        "thumbnail_path": "Local cached thumbnail path (null if none usable).",
        "engagement_rate": "(like_count + comment_count) / view_count. PRIMARY age-robust outcome.",
        "like_rate": "like_count / view_count.",
        "comment_rate": "comment_count / view_count.",
        "log_views": "log1p(view_count). Secondary outcome; REQUIRES age control.",
        "log_subscribers": "log1p(subscriber_count).",
        "log_days_since_upload": "log1p(days_since_upload). Age control regressor.",
        "iso_week": "ISO year-week 'YYYY-Www' of upload_date.",
        "upload_frequency": "Channel uploads per week over its observed window.",
        "title_char_len": "Title length in characters.",
        "title_word_count": "Title word count.",
        "title_allcaps_ratio": "Share of alphabetic chars that are uppercase.",
        "title_has_question": "Flag: '?' present.",
        "title_has_exclaim": "Flag: '!' present.",
        "title_has_number": "Flag: a digit present.",
        "title_n_emoji": "Count of emoji.",
        "title_has_emoji": "Flag: any emoji.",
        "title_has_bracket_or_pipe": "Flag: contains [], (), or |.",
        "n_uploads": "(channel-week) number of uploads that week.",
        "n_videos_listed": "(channel) videos listed before filtering.",
        "n_videos_collected": "(channel) videos with full metadata collected.",
    }
    for variant in F.VARIANTS:
        descriptions[f"tmpl_sim_{variant}"] = (
            f"Cosine of video {variant}-embedding to the channel's overall template centroid "
            f"(how on-formula this video is)."
        )
        descriptions[f"dose_{variant}"] = (
            f"Wear-out: recency-weighted mean of PAST videos' on-template-ness ({variant}). "
            f"Higher = audience recently saturated with the formula."
        )
        descriptions[f"winshare_{variant}"] = (
            f"Wear-out: mean on-template-ness over the previous {cfg.features.get('exposure_window_k', 10)} videos ({variant})."
        )
        descriptions[f"streak_{variant}"] = (
            f"Wear-out: # consecutive prior videos above the channel's median template-similarity ({variant})."
        )
        for b in ("tmpl_sim", "dose", "winshare", "streak"):
            descriptions[f"{b}_{variant}_z"] = f"{b}_{variant} z-scored within channel."
        descriptions[f"formula_adherence_{variant}"] = (
            f"(a) cosine of video {variant}-embedding to mean of channel's previous "
            f"{cfg.features.trailing_window_n} videos. Higher=more on-formula. PRIMARY H1 regressor."
        )
        descriptions[f"formula_adherence_{variant}_z"] = (
            f"formula_adherence_{variant} z-scored WITHIN channel."
        )
        descriptions[f"rolling_homogeneity_{variant}"] = (
            f"(b) mean pairwise cosine over trailing {cfg.features.rolling_window_k} "
            f"{variant}-embeddings (incl. current)."
        )
        descriptions[f"niche_adherence_{variant}"] = (
            f"(c) cosine of video {variant}-embedding to niche top-performer centroid."
        )
        descriptions[f"week_pairwise_homogeneity_{variant}"] = (
            f"(channel-week) mean pairwise cosine among that week's {variant}-embeddings."
        )

    lines = [
        "# Data dictionary — Study 1",
        "",
        "Two panels. **Snapshot caveat:** view/like/comment counts are accumulated values at "
        "`scrape_date`, not a time series — always control for `days_since_upload` and prefer "
        "`engagement_rate`. The longitudinal `rescrape` dataset (M5) carries true trajectories.",
        "",
        "## 1. video-level panel (`video_panel.parquet`)",
        f"{vdf.shape[0]} rows × {vdf.shape[1]} cols.",
        "",
        "| column | description |",
        "|---|---|",
    ]
    for c in vdf.columns:
        lines.append(f"| `{c}` | {descriptions.get(c, '(see code)')} |")
    lines += [
        "",
        "## 2. channel-week panel (`channel_week_panel.parquet`)",
        f"{cw.shape[0]} rows × {cw.shape[1]} cols. Aggregated to (channel_ref, iso_week).",
        "",
        "| column | description |",
        "|---|---|",
    ]
    for c in cw.columns:
        lines.append(f"| `{c}` | {descriptions.get(c, '(aggregated; see code)')} |")
    path.write_text("\n".join(lines))
    return str(path)


def main(cfg, log=None):
    log = log or get_logger("panel", cfg.path("logs_dir"))
    vdf = build_video_panel(cfg, log)
    cw = build_channel_week_panel(cfg, log, vdf)
    dd = write_data_dictionary(cfg, vdf, cw)
    log.info(f"data dictionary -> {dd}")
    return {"videos": len(vdf), "channel_weeks": len(cw)}
