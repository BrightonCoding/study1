"""
seeds.py — versioned, reproducible channel seed list.

The seed CSV (paths.seed_channels_csv) is the reproducibility anchor for the sample:
it is hand-curated initially and EXPANDED (not silently regenerated) by keyword search
via `discover`. We dedupe on channel_ref / channel_id and never drop existing rows.
"""
from __future__ import annotations

import pandas as pd

from .config import Cfg


def load_seed_channels(cfg: Cfg) -> pd.DataFrame:
    path = cfg.path("seed_channels_csv")
    if not path.exists():
        raise FileNotFoundError(
            f"seed channel CSV not found at {path}. Provide a hand seed or run `discover`."
        )
    df = pd.read_csv(path)
    if "channel_ref" not in df.columns:
        raise ValueError("seed CSV must have a 'channel_ref' column")
    df = df.dropna(subset=["channel_ref"]).drop_duplicates(subset=["channel_ref"])
    return df.reset_index(drop=True)


def merge_discovered_into_seed(cfg: Cfg, discovered: list[dict], logger) -> int:
    """Append newly discovered channels to the seed CSV (idempotent). Returns new total."""
    path = cfg.path("seed_channels_csv")
    existing = load_seed_channels(cfg) if path.exists() else pd.DataFrame(
        columns=["channel_ref", "channel_name", "source", "notes"]
    )
    have_refs = set(existing["channel_ref"].astype(str))
    have_ids = set(existing.get("channel_id", pd.Series(dtype=str)).astype(str))

    rows = []
    for c in discovered:
        ref = c.get("channel_url") or c.get("channel_id")
        if not ref:
            continue
        if ref in have_refs or str(c.get("channel_id")) in have_ids:
            continue
        rows.append(
            {
                "channel_ref": ref,
                "channel_name": c.get("channel_title"),
                "channel_id": c.get("channel_id"),
                "source": f"search:{c.get('source_keyword')}",
                "notes": "",
            }
        )
    if not rows:
        logger.info("merge_discovered: nothing new to add")
        return len(existing)

    out = pd.concat([existing, pd.DataFrame(rows)], ignore_index=True)
    out = out.drop_duplicates(subset=["channel_ref"]).reset_index(drop=True)
    out.to_csv(path, index=False)
    logger.info(f"merge_discovered: added {len(rows)} channels -> {path}")
    return len(out)
