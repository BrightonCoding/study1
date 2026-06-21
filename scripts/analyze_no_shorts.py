#!/usr/bin/env python3
"""
Robustness spec: re-run the full analysis EXCLUDING YouTube Shorts.

Shorts (is_short) are a different format (vertical, <=60s, different thumbnail conventions and
engagement dynamics). They can contaminate BOTH the outcome and the 'formula' centroid. So we
drop them BEFORE recomputing homogeneity — i.e. each video's formula_adherence is measured only
against the channel's previous non-Shorts, not its Shorts.

Reuses the exact same feature + model code as the main pipeline; only the input rows change.
Writes to outputs/no_shorts/ and prints a with-vs-without coefficient comparison.
Run:  .venv/bin/python scripts/analyze_no_shorts.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.config import load_config
from src.logging_setup import get_logger
from src import features as F
from src import analyze as A
from src.build_panel import _upload_frequency, _week_pairwise_homogeneity
from src.embed import embeddings_as_dict


def build_panels_no_shorts(cfg, log):
    raw = pd.read_parquet(cfg.path("panels_dir") / "raw_video_panel.parquet")
    raw = raw.dropna(subset=["video_id"]).drop_duplicates(subset=["video_id"]).reset_index(drop=True)
    n_all = len(raw)
    v = raw[~raw["is_short"].fillna(False)].copy().reset_index(drop=True)
    log.info(f"dropped {n_all - len(v)} Shorts; {len(v)} long-form videos remain "
             f"across {v['channel_ref'].nunique()} channels")

    # derived covariates + features (identical to build_panel, on the filtered set)
    v["iso_week"] = v["upload_date"].apply(F.iso_week)
    v["upload_frequency"] = _upload_frequency(v)
    v = F.add_title_features(v)
    emb_by_variant = {x: embeddings_as_dict(cfg, x) for x in F.VARIANTS}
    v = F.add_homogeneity_features(cfg, v, emb_by_variant)
    v = F.add_exposure_features(cfg, v, emb_by_variant)  # wear-out predictors
    if "log_subscribers" not in v.columns:
        v["log_subscribers"] = np.log1p(v["subscriber_count"])

    # channel-week panel (same aggregation as build_panel)
    min_uploads = int(cfg.features.min_uploads_for_week)
    agg = {"engagement_rate": "mean", "like_rate": "mean", "comment_rate": "mean",
           "log_views": "mean", "view_count": "median", "days_since_upload": "mean",
           "subscriber_count": "max", "upload_frequency": "first", "video_id": "count"}
    for variant in F.VARIANTS:
        for base in ("formula_adherence", "rolling_homogeneity", "niche_adherence"):
            col = f"{base}_{variant}"
            if col in v.columns:
                agg[col] = "mean"
    cw = v.groupby(["channel_ref", "iso_week"]).agg(agg).rename(columns={"video_id": "n_uploads"})
    for variant in F.VARIANTS:
        emb = emb_by_variant.get(variant, {})
        if emb:
            cw[f"week_pairwise_homogeneity_{variant}"] = _week_pairwise_homogeneity(v, emb, min_uploads)
    cw = cw.reset_index()
    chan_map = v.dropna(subset=["channel_id"]).groupby("channel_ref")["channel_id"].first()
    cw["channel_id"] = cw["channel_ref"].map(chan_map)
    return v, cw


def main():
    cfg_path = sys.argv[1] if len(sys.argv) > 1 else None  # optional --config-style path
    cfg = load_config(cfg_path)
    log = get_logger("analyze_noshorts", cfg.path("logs_dir"))
    out = cfg.path("outputs_dir") / "no_shorts"
    (out / "tables").mkdir(parents=True, exist_ok=True)

    v, cw = build_panels_no_shorts(cfg, log)

    # apply same analysis filter (min videos/channel)
    minv = int(cfg.analysis.min_videos_per_channel)
    vc = v["channel_ref"].value_counts()
    v = v[v["channel_ref"].isin(vc[vc >= minv].index)].copy()
    log.info(f"analysis sample (no Shorts): {len(v)} videos, {v['channel_ref'].nunique()} channels")

    rows, sections = [], []
    for fn, args in [(A.core_video_models, (cfg, log, v)),
                     (A.wear_out_models, (cfg, log, v)),
                     (A.channel_week_models, (cfg, log, cw)),
                     (A.direction_probe, (cfg, log, cw)),
                     (A.robustness_subsample, (cfg, log, v))]:
        r, md = fn(*args)
        rows += r
        sections.append(md)
    sanity_md = A.sanity_checks(cfg, log, v)

    coef = pd.DataFrame(rows)
    coef.to_csv(out / "tables" / "all_coefficients.csv", index=False)
    (out / "tables" / "model_summaries.md").write_text(
        "# Model summaries — Study 1 (Shorts EXCLUDED)\n\n" + "\n\n".join(sections) + "\n\n" + sanity_md)
    # _write_findings writes to the MAIN outputs/FINDINGS.md, so preserve & restore it.
    main_findings = cfg.path("outputs_dir") / "FINDINGS.md"
    saved = main_findings.read_text() if main_findings.exists() else None
    A._write_findings(cfg, log, v, cw, coef, sanity_md)
    (out / "FINDINGS.md").write_text(main_findings.read_text())  # the no-shorts version
    if saved is not None:
        main_findings.write_text(saved)  # restore the with-shorts version

    # print a with-vs-without comparison on the key models
    base = pd.read_csv(cfg.path("tables_dir") / "all_coefficients.csv")
    print("\n" + "=" * 78)
    print("WITH-SHORTS vs NO-SHORTS  (coefficient on the homogeneity regressor)")
    print("=" * 78)
    keymodels = ["core_thumbnail", "core_title", "core_combined",
                 "week_thumbnail", "week_title", "week_combined",
                 "direction_thumbnail_forward", "direction_thumbnail_reverse",
                 "robust_thumbnail"]
    def row(df, m):
        r = df[df["model"] == m]
        return (f"{r.iloc[0]['coef']:+.5f} (p={r.iloc[0]['p']:.3f}, N={int(r.iloc[0]['n_obs'])})"
                if len(r) else "—")
    print(f"{'model':30s} {'WITH shorts':28s} {'NO shorts':28s}")
    for m in keymodels:
        print(f"{m:30s} {row(base,m):28s} {row(coef,m):28s}")
    print(f"\nsaved -> {out}/FINDINGS.md , {out}/tables/")


if __name__ == "__main__":
    main()
