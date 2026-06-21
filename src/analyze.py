"""
analyze.py — M4. The econometrics.

Everything is WITHIN-channel: we use channel fixed effects (entity effects) so identification
comes from a channel deviating from its OWN norm, never from cross-channel differences (which are
hopelessly confounded by size/topic/era). Standard errors are clustered by channel.

Models:
  1. Core within-channel (video-level):
        engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers
                          + upload_frequency + ChannelFE         [thumbnail/title/combined]
     + a log_views variant WITH age control as robustness.
  2. Channel-week:
        mean_engagement_rate ~ week homogeneity + controls + ChannelFE.
  3. Direction / reverse-causation probe (channel-week, lagged), head to head:
        forward: engagement_t   ~ homogeneity_{t-1} + controls + ChannelFE
        reverse: homogeneity_t  ~ engagement_{t-1}  + controls + ChannelFE
     Labeled a poor-man's Granger test — suggestive, not proof.
  4. Robustness subsample: channels HIGH-engagement early that later INCREASED homogeneity.
  5. Sanity/manipulation checks: within-channel variance of formula_adherence, thumbnail vs
     title similarity correlation, and thumbnail-tile panels for high/low-homogeneity channels.

Outputs: per-model CSV + a combined readable summary, plots, and FINDINGS.md.

We deliberately report EVERY specification we run (no cherry-picking). A null/weak/wrong-signed
result is reported plainly.
"""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd

from .config import Cfg
from .logging_setup import get_logger

warnings.filterwarnings("ignore")  # linearmodels/statsmodels chatter; results unaffected

CONTROLS_VIDEO = ["log_days_since_upload", "log_subscribers", "upload_frequency"]


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def _time_index(d, entity, time):
    """linearmodels needs a numeric/date-like time index that is UNIQUE within entity.
    We build a within-channel chronological ordinal (0,1,2,... ordered by the time column,
    parsed as a date when possible, else lexically — which is already chronological for
    'YYYY-Www' ISO weeks). Returned aligned to d.index."""
    tmp = d[[entity, time]].copy()
    key = pd.to_datetime(tmp[time], errors="coerce")
    if key.isna().all():
        key = tmp[time].astype(str)
    tmp["_k"] = key
    order = tmp.sort_values([entity, "_k"], kind="mergesort")
    order["_t"] = order.groupby(entity).cumcount().astype(int)
    return order["_t"].reindex(d.index)


def _panel_ols(df, y, xs, entity, time, add_time_effects=False):
    """Fit PanelOLS with entity (channel) effects, channel-clustered SE. Returns a tidy dict
    of results plus the per-regressor coefficient table. None on failure / insufficient data."""
    import statsmodels.api as sm
    from linearmodels.panel import PanelOLS

    cols = [y] + xs + [entity, time]
    d = df[cols].replace([np.inf, -np.inf], np.nan).dropna()
    # need within-entity variation: drop singleton channels
    counts = d[entity].value_counts()
    keep = counts[counts >= 2].index
    d = d[d[entity].isin(keep)]
    if d[entity].nunique() < 5 or len(d) < 30:
        return None
    d = d.copy()
    d["__t"] = _time_index(d, entity, time)
    d = d.set_index([entity, "__t"])
    exog = sm.add_constant(d[xs])
    try:
        mod = PanelOLS(
            d[y], exog, entity_effects=True, time_effects=add_time_effects, drop_absorbed=True
        )
        res = mod.fit(cov_type="clustered", cluster_entity=True)
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)[:120]}
    table = []
    for name in res.params.index:
        if name == "const":
            continue
        table.append(
            {
                "term": name,
                "coef": float(res.params[name]),
                "se": float(res.std_errors[name]),
                "t": float(res.tstats[name]),
                "p": float(res.pvalues[name]),
                "ci_low": float(res.conf_int().loc[name, "lower"]),
                "ci_high": float(res.conf_int().loc[name, "upper"]),
            }
        )
    return {
        "n_obs": int(res.nobs),
        "n_channels": int(d.index.get_level_values(0).nunique()),
        "rsq_within": float(res.rsquared_within),
        "table": pd.DataFrame(table),
    }


def _zscore_within(df, col, by="channel_ref"):
    def z(s):
        sd = s.std(ddof=0)
        return (s - s.mean()) / sd if sd and sd > 0 else s * 0.0
    return df.groupby(by)[col].transform(z)


def _fmt_result(title, spec, res) -> str:
    if res is None:
        return f"### {title}\n_{spec}_\n\n**Skipped** — insufficient within-channel data.\n"
    if "error" in res:
        return f"### {title}\n_{spec}_\n\n**Error**: {res['error']}\n"
    lines = [f"### {title}", f"_{spec}_", "",
             f"N = {res['n_obs']} videos/obs across {res['n_channels']} channels; "
             f"within-R² = {res['rsq_within']:.4f}", "",
             "| term | coef | SE | t | p | 95% CI |", "|---|---:|---:|---:|---:|---|"]
    for _, r in res["table"].iterrows():
        star = "***" if r.p < 0.01 else "**" if r.p < 0.05 else "*" if r.p < 0.10 else ""
        lines.append(
            f"| `{r.term}` | {r.coef:+.5f}{star} | {r.se:.5f} | {r.t:+.2f} | {r.p:.3f} | "
            f"[{r.ci_low:+.4f}, {r.ci_high:+.4f}] |"
        )
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# models
# --------------------------------------------------------------------------- #
def core_video_models(cfg, log, v) -> tuple[list[dict], str]:
    """Model 1: within-channel association, per embedding variant (+ log_views robustness)."""
    md = ["## 1. Core within-channel association (video-level)\n",
          "Outcome = engagement_rate. Regressor of interest = formula_adherence "
          "(z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). "
          "Channel FE; SE clustered by channel.\n"]
    rows = []
    for variant in cfg.analysis.variants:
        zcol = f"formula_adherence_{variant}_z"
        if zcol not in v.columns:
            continue
        xs = [zcol] + CONTROLS_VIDEO
        res = _panel_ols(v, "engagement_rate", xs, "channel_ref", "video_id")
        md.append(_fmt_result(
            f"1.{variant} — engagement_rate ~ formula_adherence ({variant})",
            "engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers "
            "+ upload_frequency + ChannelFE",
            res,
        ))
        if res and "table" in res:
            r = res["table"].query("term == @zcol")
            if len(r):
                rows.append({"model": f"core_{variant}", "outcome": "engagement_rate",
                             **r.iloc[0].to_dict(), "n_obs": res["n_obs"],
                             "n_channels": res["n_channels"]})
    # log_views robustness (REQUIRES age control, which is in CONTROLS_VIDEO)
    for variant in cfg.analysis.variants:
        zcol = f"formula_adherence_{variant}_z"
        if zcol not in v.columns:
            continue
        xs = [zcol] + CONTROLS_VIDEO
        res = _panel_ols(v, "log_views", xs, "channel_ref", "video_id")
        md.append(_fmt_result(
            f"1.{variant}.logviews — log_views ~ formula_adherence ({variant}) [age-controlled]",
            "log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers "
            "+ upload_frequency + ChannelFE",
            res,
        ))
        if res and "table" in res:
            r = res["table"].query("term == @zcol")
            if len(r):
                rows.append({"model": f"core_{variant}_logviews", "outcome": "log_views",
                             **r.iloc[0].to_dict(), "n_obs": res["n_obs"],
                             "n_channels": res["n_channels"]})
    return rows, "\n".join(md)


def wear_out_models(cfg, log, v) -> tuple[list[dict], str]:
    """REDESIGNED wear-out test (video-level). Instead of 'is this video on-formula', the
    predictor is ACCUMULATED audience exposure to the formula before the video:
      dose      — recency-weighted past on-template-ness (PRIMARY),
      winshare  — share of recent window that was on-template,
      streak    — consecutive prior on-template videos.
    Wear-out predicts NEGATIVE coefficients. We also test:
      nonlinear — dose + dose^2 (fatigue may be a threshold, not a line),
      rebound   — coef on the CURRENT video's template-similarity; NEGATIVE means on-formula
                  videos underperform / breaking the formula gives a bump.
    All within-channel (channel FE), channel-clustered SE. Standardized predictors.
    """
    md = ["## 6. Wear-out: cumulative formula EXPOSURE (redesign)\n",
          "Outcome = engagement_rate. Predictor = accumulated exposure to the channel's formula "
          "BEFORE the video (recency-weighted dose / window-share / streak), z-scored within "
          "channel. Channel FE; clustered SE. Wear-out => NEGATIVE coefficient.\n"]
    rows = []
    for variant in cfg.analysis.variants:
        specs = [
            ("dose", f"dose_{variant}_z"),
            ("winshare", f"winshare_{variant}_z"),
            ("streak", f"streak_{variant}_z"),
        ]
        for label, zcol in specs:
            if zcol not in v.columns:
                continue
            res = _panel_ols(v, "engagement_rate", [zcol] + CONTROLS_VIDEO,
                             "channel_ref", "video_id")
            md.append(_fmt_result(
                f"6.{variant}.{label} — engagement_rate ~ {label} exposure ({variant})",
                f"engagement_rate ~ {label}_z + controls + ChannelFE", res))
            if res and "table" in res:
                r = res["table"].query("term == @zcol")
                if len(r):
                    rows.append({"model": f"wearout_{variant}_{label}", "outcome": "engagement_rate",
                                 **r.iloc[0].to_dict(), "n_obs": res["n_obs"],
                                 "n_channels": res["n_channels"]})
        # nonlinear dose (dose + dose^2)
        zc = f"dose_{variant}_z"
        if zc in v.columns:
            vv = v.copy()
            vv[f"{zc}_sq"] = vv[zc] ** 2
            res = _panel_ols(vv, "engagement_rate", [zc, f"{zc}_sq"] + CONTROLS_VIDEO,
                             "channel_ref", "video_id")
            md.append(_fmt_result(
                f"6.{variant}.nonlinear — engagement_rate ~ dose + dose^2 ({variant})",
                "quadratic in cumulative dose; channel FE", res))
            if res and "table" in res:
                for term, tag in [(zc, "nonlin_lin"), (f"{zc}_sq", "nonlin_sq")]:
                    r = res["table"].query("term == @term")
                    if len(r):
                        rows.append({"model": f"wearout_{variant}_{tag}", "outcome": "engagement_rate",
                                     **r.iloc[0].to_dict(), "n_obs": res["n_obs"],
                                     "n_channels": res["n_channels"]})
        # novelty rebound: coef on the current video's template similarity
        ts = f"tmpl_sim_{variant}_z"
        if ts in v.columns:
            res = _panel_ols(v, "engagement_rate", [ts] + CONTROLS_VIDEO,
                             "channel_ref", "video_id")
            md.append(_fmt_result(
                f"6.{variant}.rebound — engagement_rate ~ template_similarity ({variant})",
                "NEGATIVE => on-formula videos underperform / breaking formula bumps engagement",
                res))
            if res and "table" in res:
                r = res["table"].query("term == @ts")
                if len(r):
                    rows.append({"model": f"wearout_{variant}_rebound", "outcome": "engagement_rate",
                                 **r.iloc[0].to_dict(), "n_obs": res["n_obs"],
                                 "n_channels": res["n_channels"]})
    return rows, "\n".join(md)


def channel_week_models(cfg, log, cw) -> tuple[list[dict], str]:
    """Model 2: channel-week version."""
    md = ["## 2. Channel-week association\n",
          "Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise "
          "homogeneity (falls back to mean formula_adherence where pairwise is sparse). "
          "Channel FE; SE clustered by channel.\n"]
    cw = cw.copy()
    cw["week_ord"] = cw["iso_week"]
    rows = []
    for variant in cfg.analysis.variants:
        hcol = f"week_pairwise_homogeneity_{variant}"
        fcol = f"formula_adherence_{variant}"
        # prefer pairwise; fill missing weeks with the mean-adherence homogeneity
        if hcol not in cw.columns:
            continue
        cw[f"_hom_{variant}"] = cw[hcol].fillna(cw.get(fcol))
        cw[f"_hom_{variant}_z"] = _zscore_within(cw, f"_hom_{variant}")
        xs = [f"_hom_{variant}_z", "log_subscribers" if "log_subscribers" in cw.columns
              else "subscriber_count", "upload_frequency"]
        # build needed controls
        if "log_subscribers" not in cw.columns:
            cw["log_subscribers"] = np.log1p(cw["subscriber_count"])
            xs = [f"_hom_{variant}_z", "log_subscribers", "upload_frequency"]
        res = _panel_ols(cw, "engagement_rate", xs, "channel_ref", "week_ord")
        md.append(_fmt_result(
            f"2.{variant} — mean engagement_rate ~ homogeneity ({variant})",
            "engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE",
            res,
        ))
        if res and "table" in res:
            r = res["table"].query("term == @xs[0]")
            if len(r):
                rows.append({"model": f"week_{variant}", "outcome": "engagement_rate",
                             **r.iloc[0].to_dict(), "n_obs": res["n_obs"],
                             "n_channels": res["n_channels"]})
    return rows, "\n".join(md)


def direction_probe(cfg, log, cw) -> tuple[list[dict], str]:
    """Model 3: forward vs reverse lagged channel-week regressions (poor-man's Granger)."""
    md = ["## 3. Direction / reverse-causation probe (poor-man's Granger)\n",
          "Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. "
          "Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* "
          "(NOT proof) that the arrow runs homogeneity→engagement.\n"]
    cw = cw.sort_values(["channel_ref", "iso_week"]).copy()
    cw["log_subscribers"] = np.log1p(cw["subscriber_count"])
    rows = []
    for variant in cfg.analysis.variants:
        hcol = f"week_pairwise_homogeneity_{variant}"
        fcol = f"formula_adherence_{variant}"
        if hcol not in cw.columns:
            continue
        cw["_hom"] = cw[hcol].fillna(cw.get(fcol))
        cw["_eng"] = cw["engagement_rate"]
        g = cw.groupby("channel_ref")
        cw["_hom_lag"] = g["_hom"].shift(1)
        cw["_eng_lag"] = g["_eng"].shift(1)
        # standardize within channel for comparable magnitudes
        for c in ["_hom", "_eng", "_hom_lag", "_eng_lag"]:
            cw[f"{c}_z"] = _zscore_within(cw, c)
        cw["week_ord"] = cw["iso_week"]

        fwd = _panel_ols(cw, "_eng_z", ["_hom_lag_z", "log_subscribers", "upload_frequency"],
                         "channel_ref", "week_ord")
        rev = _panel_ols(cw, "_hom_z", ["_eng_lag_z", "log_subscribers", "upload_frequency"],
                         "channel_ref", "week_ord")
        md.append(_fmt_result(f"3.{variant}.forward — engagement_t ~ homogeneity_(t-1)",
                              "ChannelFE; standardized", fwd))
        md.append(_fmt_result(f"3.{variant}.reverse — homogeneity_t ~ engagement_(t-1)",
                              "ChannelFE; standardized", rev))
        for label, res, key in [("forward", fwd, "_hom_lag_z"), ("reverse", rev, "_eng_lag_z")]:
            if res and "table" in res:
                r = res["table"].query("term == @key")
                if len(r):
                    rows.append({"model": f"direction_{variant}_{label}",
                                 "outcome": ("engagement" if label == "forward" else "homogeneity"),
                                 **r.iloc[0].to_dict(), "n_obs": res["n_obs"],
                                 "n_channels": res["n_channels"]})
    return rows, "\n".join(md)


def robustness_subsample(cfg, log, v) -> tuple[list[dict], str]:
    """Model 4: channels HIGH-engagement early that later INCREASED homogeneity."""
    md = ["## 4. Robustness subsample (strong-start, then homogenized)\n",
          "Restrict to channels whose EARLY-window engagement was above the niche median AND "
          "whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is "
          "not just 'always-struggling channels chasing a formula'.\n"]
    variant = cfg.analysis.variants[0]
    fcol = f"formula_adherence_{variant}"
    if fcol not in v.columns:
        return [], "\n".join(md) + "\n_(no formula_adherence column)_\n"
    v = v.dropna(subset=["upload_date"]).copy()
    niche_med_eng = v["engagement_rate"].median()
    keep = []
    for ch, sub in v.groupby("channel_ref"):
        sub = sub.sort_values("upload_date")
        if len(sub) < 8:
            continue
        half = len(sub) // 2
        early, late = sub.iloc[:half], sub.iloc[half:]
        early_eng = early["engagement_rate"].mean()
        if not np.isfinite(early_eng) or early_eng <= niche_med_eng:
            continue
        if late[fcol].mean() > early[fcol].mean():  # homogenized over time
            keep.append(ch)
    md.append(f"Subsample: {len(keep)} channels meet 'strong start + later homogenized'.\n")
    if len(keep) < 5:
        return [], "\n".join(md) + "\n_Too few channels for a stable estimate._\n"
    sub = v[v["channel_ref"].isin(keep)]
    zcol = f"formula_adherence_{variant}_z"
    res = _panel_ols(sub, "engagement_rate", [zcol] + CONTROLS_VIDEO, "channel_ref", "video_id")
    md.append(_fmt_result(f"4.{variant} — engagement_rate ~ formula_adherence (subsample)",
                          "same spec as Model 1, restricted sample", res))
    rows = []
    if res and "table" in res:
        r = res["table"].query("term == @zcol")
        if len(r):
            rows.append({"model": f"robust_{variant}", "outcome": "engagement_rate",
                         **r.iloc[0].to_dict(), "n_obs": res["n_obs"],
                         "n_channels": res["n_channels"]})
    return rows, "\n".join(md)


def sanity_checks(cfg, log, v) -> str:
    """Model 5: manipulation/sanity checks + tile panels."""
    from .embed import _l2, embeddings_as_dict, make_sanity_panels

    md = ["## 5. Manipulation / sanity checks\n"]
    # 5a within-channel SD of formula_adherence
    variant = cfg.analysis.variants[0]
    fcol = f"formula_adherence_{variant}"
    sd = v.groupby("channel_ref")[fcol].std()
    md.append(f"**5a. Within-channel SD of formula_adherence ({variant})** — the regressor must "
              f"vary within channel or the test is dead.\n")
    md.append(f"- mean within-channel SD = {sd.mean():.4f}; median = {sd.median():.4f}; "
              f"share of channels with SD>0.02 = {(sd > 0.02).mean():.0%}\n")

    # 5b thumbnail vs title similarity correlation
    thumb = embeddings_as_dict(cfg, "thumbnail")
    title = embeddings_as_dict(cfg, "title")
    corrs = []
    for ch, subdf in v.groupby("channel_ref"):
        vids = [x for x in subdf["video_id"] if x in thumb and x in title]
        if len(vids) < 5:
            continue
        T = _l2(np.vstack([thumb[x] for x in vids])); L = _l2(np.vstack([title[x] for x in vids]))
        iu = np.triu_indices(len(vids), k=1)
        c = np.corrcoef((T @ T.T)[iu], (L @ L.T)[iu])[0, 1]
        if np.isfinite(c):
            corrs.append(c)
    if corrs:
        md.append(f"\n**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): "
                  f"mean = {np.mean(corrs):.3f} (want positive but <1 — related, not redundant).\n")

    # 5c tile panels for highest & lowest homogeneity channels
    chan_h = v.groupby("channel_ref")[fcol].mean().dropna().sort_values()
    panels = []
    try:
        panels = make_sanity_panels(cfg, log, variant="thumbnail", n_channels=3)
    except Exception as e:  # noqa: BLE001
        md.append(f"\n_(tile panels skipped: {e})_\n")
    if panels:
        md.append("\n**5c. Thumbnail-tile panels** (eyeball the score): "
                  + ", ".join(f"`{p.name}`" for p in panels) + "\n")
    if len(chan_h):
        md.append(f"\nHomogeneity ranking ({variant}): most-formulaic = "
                  f"`{chan_h.index[-1]}` ({chan_h.iloc[-1]:.3f}); least = "
                  f"`{chan_h.index[0]}` ({chan_h.iloc[0]:.3f}).\n")
    return "\n".join(md)


# --------------------------------------------------------------------------- #
# orchestration
# --------------------------------------------------------------------------- #
def main(cfg: Cfg, log=None):
    log = log or get_logger("analyze", cfg.path("logs_dir"))
    v = pd.read_parquet(cfg.path("video_panel_parquet"))
    cw = pd.read_parquet(cfg.path("channel_week_panel_parquet"))

    # apply the analysis sample filter (min videos per channel)
    minv = int(cfg.analysis.min_videos_per_channel)
    vc = v["channel_ref"].value_counts()
    v = v[v["channel_ref"].isin(vc[vc >= minv].index)].copy()
    if "log_subscribers" not in v.columns:
        v["log_subscribers"] = np.log1p(v["subscriber_count"])
    log.info(f"analysis sample: {len(v)} videos, {v['channel_ref'].nunique()} channels "
             f"(min {minv} videos/channel)")

    all_rows, sections = [], []
    for fn, args in [
        (core_video_models, (cfg, log, v)),
        (wear_out_models, (cfg, log, v)),
        (channel_week_models, (cfg, log, cw)),
        (direction_probe, (cfg, log, cw)),
        (robustness_subsample, (cfg, log, v)),
    ]:
        rows, md = fn(*args)
        all_rows += rows
        sections.append(md)
        log.info(f"{fn.__name__}: {len(rows)} coefficient rows")
    sanity_md = sanity_checks(cfg, log, v)

    # write tidy coefficient table (CSV)
    tables_dir = cfg.path("tables_dir")
    coef = pd.DataFrame(all_rows)
    coef_path = tables_dir / "all_coefficients.csv"
    coef.to_csv(coef_path, index=False)
    log.info(f"saved {coef_path}")

    # readable combined summary
    summary_path = tables_dir / "model_summaries.md"
    summary_path.write_text("# Model summaries — Study 1\n\n" + "\n\n".join(sections) + "\n\n" + sanity_md)
    log.info(f"saved {summary_path}")

    _write_findings(cfg, log, v, cw, coef, sanity_md)
    _plots(cfg, log, v)
    return {"models": len(all_rows), "summary": str(summary_path)}


def _write_findings(cfg, log, v, cw, coef, sanity_md):
    """The plain-language FINDINGS.md — honest about sign/size/significance and limitations."""
    path = cfg.path("outputs_dir") / "FINDINGS.md"
    n_videos = len(v); n_channels = v["channel_ref"].nunique()

    def grab(model):
        if coef.empty or "model" not in coef.columns:
            return None
        r = coef[coef["model"] == model]
        return r.iloc[0] if len(r) else None

    primary_variant = cfg.analysis.variants[0]
    core = grab(f"core_{primary_variant}")

    lines = [
        "# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out",
        "",
        f"**Sample:** {n_channels} channels, {n_videos} videos "
        f"(personal-finance/investing niche; snapshot taken {cfg.scrape_date()}).",
        "",
        "## Headline (H1)",
    ]
    if core is not None:
        direction = "LOWER" if core["coef"] < 0 else "HIGHER"
        sig = ("statistically significant (p<0.05)" if core["p"] < 0.05
               else "not statistically significant (p≥0.05)")
        lines += [
            f"Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is "
            f"associated with **{core['coef']:+.5f}** change in engagement_rate "
            f"(SE {core['se']:.5f}, p={core['p']:.3f}) — i.e. **{direction}** subsequent "
            f"engagement, controlling for video age, subscribers, and upload frequency, with "
            f"channel fixed effects. This is **{sig}**.",
            "",
            "H1 predicts a NEGATIVE coefficient. " +
            ("**Consistent with H1.**" if core["coef"] < 0 and core["p"] < 0.05 else
             "**Not clearly supported** at conventional significance — reported honestly." if
             core["coef"] < 0 else "**Wrong-signed vs H1** — reported honestly."),
        ]
    else:
        lines += ["_Core model did not estimate (insufficient data)._"]

    lines += [
        "",
        "## All specifications (coefficient on the homogeneity regressor)",
        "",
        "| model | outcome | coef | SE | p | N obs | N chan |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for _, r in coef.iterrows():
        lines.append(f"| {r['model']} | {r['outcome']} | {r['coef']:+.5f} | {r['se']:.5f} | "
                     f"{r['p']:.3f} | {int(r['n_obs'])} | {int(r['n_channels'])} |")

    # direction read
    fwd = grab(f"direction_{primary_variant}_forward")
    rev = grab(f"direction_{primary_variant}_reverse")
    lines += ["", "## Direction probe (suggestive, not causal)"]
    if fwd is not None and rev is not None:
        lines.append(
            f"Forward (engagement_t ~ homogeneity_(t-1)): coef {fwd['coef']:+.4f} (p={fwd['p']:.3f}). "
            f"Reverse (homogeneity_t ~ engagement_(t-1)): coef {rev['coef']:+.4f} (p={rev['p']:.3f}). "
            + ("Forward stronger than reverse — weakly consistent with homogeneity→engagement."
               if abs(fwd['coef']) > abs(rev['coef']) else
               "Reverse is comparable/stronger — cannot rule out that declining engagement drives "
               "homogenization (the main reverse-causation threat).")
        )
    else:
        lines.append("_Direction probe did not estimate (insufficient lagged within-channel data)._")

    rob = grab(f"robust_{primary_variant}")
    lines += ["", "## Robustness subsample (strong-start, then homogenized)"]
    lines.append(
        (f"Coef {rob['coef']:+.5f} (p={rob['p']:.3f}, N={int(rob['n_obs'])}). "
         + ("H1 survives in the strong-start subsample." if rob['coef'] < 0 and rob['p'] < 0.10
            else "H1 does not clearly survive here.")) if rob is not None
        else "_Subsample too small to estimate._"
    )

    lines += [
        "", "## Sanity checks", "", sanity_md,
        "", "## LIMITATIONS (read these)",
        "- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control "
        "for age and use the age-robust engagement_rate, but per-video time dynamics await the "
        "longitudinal rescrape dataset (M5).",
        "- **Observational.** Channel FE removes fixed confounders but not time-varying ones "
        "(e.g. a channel simultaneously homogenizing AND declining for an external reason).",
        "- **Reverse causation** is probed, not eliminated — see the direction section.",
        "- **Single niche** (personal finance). External validity to other niches is untested.",
        "- **Discovery noise.** Search-expanded channels may include some off-niche channels.",
        "- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).",
    ]
    path.write_text("\n".join(lines))
    log.info(f"saved {path}")


def _plots(cfg, log, v):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plots = cfg.path("plots_dir")
    variant = cfg.analysis.variants[0]
    fcol = f"formula_adherence_{variant}"
    d = v[[fcol, "engagement_rate", "channel_ref"]].dropna()
    if len(d) < 30:
        return
    # within-channel partialled scatter: demean both vars within channel (FE residuals)
    d = d.copy()
    d["x"] = d[fcol] - d.groupby("channel_ref")[fcol].transform("mean")
    d["y"] = d["engagement_rate"] - d.groupby("channel_ref")["engagement_rate"].transform("mean")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(d["x"], d["y"], s=8, alpha=0.3)
    if len(d) > 2:
        b, a = np.polyfit(d["x"], d["y"], 1)
        xs = np.linspace(d["x"].min(), d["x"].max(), 50)
        ax.plot(xs, a + b * xs, color="red", lw=2, label=f"slope={b:+.4f}")
        ax.legend()
    ax.set_xlabel(f"formula_adherence ({variant}), within-channel demeaned")
    ax.set_ylabel("engagement_rate, within-channel demeaned")
    ax.set_title("Within-channel: engagement vs formula adherence (FE-partialled)")
    ax.axhline(0, color="gray", lw=0.5); ax.axvline(0, color="gray", lw=0.5)
    fig.tight_layout()
    out = plots / "within_channel_engagement_vs_adherence.png"
    fig.savefig(out, dpi=120); plt.close(fig)
    log.info(f"saved {out}")
