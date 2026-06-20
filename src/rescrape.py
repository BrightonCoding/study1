"""
rescrape.py — M5. Daily longitudinal appender.

The snapshot panel can't give per-video view/like/comment TRAJECTORIES (one scrape = one point
in time). This script re-snapshots the SAME known video ids and APPENDS a fresh row per
(video_id, scrape_date) to paths.longitudinal_parquet. Run daily (cron) and, over weeks, true
per-video engagement trajectories accumulate — the proper dataset for modeling wear-out.

Key properties:
  * Idempotent per (video_id, scrape_date): re-running on the same day overwrites that day's rows,
    never duplicates them.
  * Uses a FRESH extraction (bypasses the metadata cache) because the whole point is to capture
    how counts CHANGE over time — a cached snapshot would defeat that.
  * Reads the id universe from the built video panel (falls back to raw / smoke).
  * Reuses the same Collector (concurrency, retries, politeness) as collection.
"""
from __future__ import annotations

import datetime as _dt

import pandas as pd

from .collect import make_collector
from .config import Cfg
from .logging_setup import get_logger


def _video_id_universe(cfg: Cfg) -> list[str]:
    for key in ("video_panel_parquet",):
        p = cfg.path(key)
        if p.exists():
            return pd.read_parquet(p, columns=["video_id"])["video_id"].dropna().unique().tolist()
    for name in ("raw_video_panel.parquet", "smoke_video_panel.parquet"):
        p = cfg.path("panels_dir") / name
        if p.exists():
            return pd.read_parquet(p, columns=["video_id"])["video_id"].dropna().unique().tolist()
    raise FileNotFoundError("no panel to source video ids from; run collect/panel first")


def _fresh_stats(collector, video_id: str) -> dict | None:
    """Fresh (uncached) extraction of just the volatile stats for one video."""
    import yt_dlp

    url = f"https://www.youtube.com/watch?v={video_id}"

    def _run():
        with yt_dlp.YoutubeDL(collector._opts()) as ydl:  # noqa: SLF001 (intentional reuse)
            return ydl.extract_info(url, download=False)

    info = collector._retrying(_run, f"rescrape {video_id}")  # noqa: SLF001
    if info is None:
        return None
    return {
        "video_id": video_id,
        "view_count": info.get("view_count"),
        "like_count": info.get("like_count"),
        "comment_count": info.get("comment_count"),
    }


def main(cfg: Cfg, log=None):
    from concurrent.futures import ThreadPoolExecutor

    log = log or get_logger("rescrape", cfg.path("logs_dir"))
    scrape_date = cfg.scrape_date().isoformat()
    ids = _video_id_universe(cfg)
    log.info(f"rescrape {len(ids)} videos @ {scrape_date}")

    collector = make_collector(cfg, log)
    workers = max(1, collector.concurrency)
    records = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for rec in ex.map(lambda v: _fresh_stats(collector, v), ids):
            if rec is None:
                continue
            rec["scrape_date"] = scrape_date
            rec["scrape_ts_utc"] = _dt.datetime.now(_dt.timezone.utc).isoformat()
            records.append(rec)

    new = pd.DataFrame(records)
    out = cfg.path("longitudinal_parquet")
    if out.exists():
        prev = pd.read_parquet(out)
        # idempotent: drop any existing rows for this scrape_date before appending
        prev = prev[prev["scrape_date"] != scrape_date]
        combined = pd.concat([prev, new], ignore_index=True)
    else:
        combined = new
    combined.to_parquet(out, index=False)
    log.info(f"rescrape: appended {len(new)} rows for {scrape_date}; total {len(combined)} -> {out}")
    print(f"rescrape done: {len(new)} videos snapshotted @ {scrape_date}; total rows {len(combined)}")
    return {"appended": len(new), "total": len(combined)}
