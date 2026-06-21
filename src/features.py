"""
features.py — M3. Homogeneity scores + interpretable title features.

Pure functions over (video DataFrame, embedding dicts) so they are easy to test and reuse.
All embeddings arriving here are already L2-normalized (see embed.py), so cosine = dot product.

Homogeneity scores built (per embedding variant: thumbnail / title / combined):
  (a) formula_adherence  — cosine of video v to the MEAN of that channel's PREVIOUS N videos
      (trailing centroid, ordered by upload_date). "How much does v look like what the channel
      has been doing lately." This is the PRIMARY within-video regressor for H1.
  (b) rolling_homogeneity — mean pairwise cosine over the trailing window of K recent videos
      (incl. v). A sparse-channel-friendly homogeneity that doesn't need >=2 uploads/week.
  (c) niche_adherence — cosine of v to the niche-wide centroid of TOP-performing videos (by
      engagement_rate). Lets us later separate "like my own channel" from "like the whole niche".

Plus cheap interpretable title features (length, ALLCAPS ratio, punctuation/number/emoji flags,
bracket/pipe usage) for robustness and human inspection.

Standardization: formula_adherence is optionally z-scored WITHIN channel (config), because the
H1 test is within-channel — we care about a video being more/less on-formula *relative to its own
channel's norm*, not the absolute cosine level (which differs by channel/style).
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

VARIANTS = ("thumbnail", "title", "combined")

# --- emoji detection (broad ranges; good enough for a flag/count) ---
_EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF←-⇿⌀-⏿]"
)
_BRACKET_PIPE_RE = re.compile(r"[\[\]\(\)\|]")


def iso_week(d) -> str | float:
    """ISO year-week label 'YYYY-Www' from a date/datetime/str. NaN-safe."""
    if pd.isna(d):
        return np.nan
    ts = pd.Timestamp(d)
    y, w, _ = ts.isocalendar()
    return f"{int(y)}-W{int(w):02d}"


# --------------------------------------------------------------------------- #
# title features
# --------------------------------------------------------------------------- #
def title_features(title: str | float) -> dict:
    t = "" if (title is None or (isinstance(title, float) and np.isnan(title))) else str(title)
    letters = [c for c in t if c.isalpha()]
    n_upper = sum(1 for c in letters if c.isupper())
    words = t.split()
    n_emoji = len(_EMOJI_RE.findall(t))
    return {
        "title_char_len": len(t),
        "title_word_count": len(words),
        "title_allcaps_ratio": (n_upper / len(letters)) if letters else 0.0,
        "title_has_question": int("?" in t),
        "title_has_exclaim": int("!" in t),
        "title_has_number": int(any(c.isdigit() for c in t)),
        "title_n_emoji": n_emoji,
        "title_has_emoji": int(n_emoji > 0),
        "title_has_bracket_or_pipe": int(bool(_BRACKET_PIPE_RE.search(t))),
    }


def add_title_features(df: pd.DataFrame) -> pd.DataFrame:
    feats = df["title"].apply(title_features).apply(pd.Series)
    return pd.concat([df, feats], axis=1)


# --------------------------------------------------------------------------- #
# embedding-based homogeneity
# --------------------------------------------------------------------------- #
def _ordered_channel_indices(df: pd.DataFrame) -> dict[str, list[int]]:
    """Map channel -> row-index list ordered oldest->newest (stable tie-break by video_id)."""
    order = df.sort_values(["channel_ref", "upload_date", "video_id"], kind="mergesort")
    out: dict[str, list[int]] = {}
    for ch, sub in order.groupby("channel_ref", sort=False):
        out[ch] = sub.index.tolist()
    return out


def _norm_rows(mat: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(mat, axis=1, keepdims=True)
    n[n == 0] = 1.0
    return mat / n


def formula_adherence(df, emb: dict[str, np.ndarray], n_trailing: int) -> pd.Series:
    """(a) cosine of each video to the mean embedding of its channel's previous N videos."""
    out = pd.Series(np.nan, index=df.index, dtype=float)
    chan_idx = _ordered_channel_indices(df)
    vid_by_row = df["video_id"].to_dict()
    for ch, rows in chan_idx.items():
        vecs = [emb.get(vid_by_row[r]) for r in rows]
        for i, r in enumerate(rows):
            if i == 0 or vecs[i] is None:
                continue
            prev = [v for v in vecs[max(0, i - n_trailing):i] if v is not None]
            if not prev:
                continue
            centroid = np.mean(np.vstack(prev), axis=0)
            nrm = np.linalg.norm(centroid)
            if nrm == 0:
                continue
            out.at[r] = float(np.dot(vecs[i], centroid / nrm))
    return out


def rolling_homogeneity(df, emb: dict[str, np.ndarray], k_window: int) -> pd.Series:
    """(b) mean pairwise cosine over the trailing window of K videos (incl. current)."""
    out = pd.Series(np.nan, index=df.index, dtype=float)
    chan_idx = _ordered_channel_indices(df)
    vid_by_row = df["video_id"].to_dict()
    for ch, rows in chan_idx.items():
        vecs = [emb.get(vid_by_row[r]) for r in rows]
        for i, r in enumerate(rows):
            window = [v for v in vecs[max(0, i - k_window + 1):i + 1] if v is not None]
            if len(window) < 2:
                continue
            w = _norm_rows(np.vstack(window))
            sims = w @ w.T
            iu = np.triu_indices(len(window), k=1)
            out.at[r] = float(sims[iu].mean())
    return out


def niche_adherence(df, emb: dict[str, np.ndarray], top_fraction: float) -> pd.Series:
    """(c) cosine of each video to the niche centroid of TOP-engagement videos."""
    out = pd.Series(np.nan, index=df.index, dtype=float)
    have = df[df["video_id"].isin(emb.keys())].copy()
    eng = have["engagement_rate"]
    valid = have[eng.notna()]
    if len(valid) < 5:
        return out
    cutoff = valid["engagement_rate"].quantile(1.0 - top_fraction)
    top_ids = valid[valid["engagement_rate"] >= cutoff]["video_id"].tolist()
    if not top_ids:
        return out
    centroid = np.mean(np.vstack([emb[v] for v in top_ids]), axis=0)
    nrm = np.linalg.norm(centroid)
    if nrm == 0:
        return out
    centroid = centroid / nrm
    for r, vid in df["video_id"].items():
        v = emb.get(vid)
        if v is not None:
            out.at[r] = float(np.dot(v, centroid))
    return out


# --------------------------------------------------------------------------- #
# cumulative-exposure ("wear-out") measures
# --------------------------------------------------------------------------- #
def template_similarity(df, emb: dict[str, np.ndarray]) -> pd.Series:
    """Per-video cosine similarity to its channel's TEMPLATE (the channel's overall centroid).
    This is 'how on-formula is this video' — order-independent, the building block for the
    accumulation measures below. (The centroid uses all the channel's videos to DEFINE the
    formula; the accumulation that follows only ever reads PAST videos.)"""
    out = pd.Series(np.nan, index=df.index, dtype=float)
    vid_by_row = df["video_id"].to_dict()
    for ch, sub in df.groupby("channel_ref"):
        vecs = {r: emb.get(vid_by_row[r]) for r in sub.index}
        present = [v for v in vecs.values() if v is not None]
        if len(present) < 2:
            continue
        centroid = np.mean(np.vstack(present), axis=0)
        nrm = np.linalg.norm(centroid)
        if nrm == 0:
            continue
        centroid = centroid / nrm
        for r, v in vecs.items():
            if v is not None:
                out.at[r] = float(np.dot(v, centroid))
    return out


def exposure_measures(df, tmpl_sim: pd.Series, decay: float, k_window: int):
    """From per-video template-similarity, build three PAST-only accumulation measures:
      dose      — recency-weighted mean of past on-template-ness (recent videos weigh more).
      winshare  — mean on-template-ness over the previous K videos (order-free, robust).
      streak    — # of consecutive previous videos above the channel's median similarity.
    All ordered by upload_date within channel; first video per channel = NaN (no history).
    Returns (dose, winshare, streak) Series aligned to df.index.
    """
    dose = pd.Series(np.nan, index=df.index, dtype=float)
    winshare = pd.Series(np.nan, index=df.index, dtype=float)
    streak = pd.Series(np.nan, index=df.index, dtype=float)

    order = df.sort_values(["channel_ref", "upload_date", "video_id"], kind="mergesort")
    for ch, sub in order.groupby("channel_ref", sort=False):
        rows = sub.index.tolist()
        s = [tmpl_sim.get(r, np.nan) for r in rows]
        valid = [x for x in s if not np.isnan(x)]
        med = np.median(valid) if valid else np.nan
        for i, r in enumerate(rows):
            past = [s[j] for j in range(i) if not np.isnan(s[j])]
            if not past:
                continue
            # recency-weighted dose: most-recent past video weight 1, older decay^gap
            w = np.array([decay ** (len(past) - 1 - t) for t in range(len(past))])
            dose.at[r] = float(np.dot(w, past) / w.sum())
            # window-share: mean over previous K
            win = [s[j] for j in range(max(0, i - k_window), i) if not np.isnan(s[j])]
            if win:
                winshare.at[r] = float(np.mean(win))
            # streak: consecutive previous above channel median
            if not np.isnan(med):
                cnt = 0
                for j in range(i - 1, -1, -1):
                    if np.isnan(s[j]):
                        break
                    if s[j] > med:
                        cnt += 1
                    else:
                        break
                streak.at[r] = float(cnt)
    return dose, winshare, streak


def add_exposure_features(cfg, df: pd.DataFrame, emb_by_variant) -> pd.DataFrame:
    """Attach template_similarity + dose/winshare/streak (and within-channel z-scores) per
    variant. These are the redesigned wear-out predictors: accumulated exposure, not conformity.
    """
    decay = float(cfg.features.get("exposure_decay", 0.8))
    k = int(cfg.features.get("exposure_window_k", cfg.features.rolling_window_k))
    df = df.copy()
    for variant in VARIANTS:
        emb = emb_by_variant.get(variant, {})
        if not emb:
            continue
        ts = template_similarity(df, emb)
        df[f"tmpl_sim_{variant}"] = ts
        dose, winshare, streak = exposure_measures(df, ts, decay, k)
        df[f"dose_{variant}"] = dose
        df[f"winshare_{variant}"] = winshare
        df[f"streak_{variant}"] = streak
        for col in (f"tmpl_sim_{variant}", f"dose_{variant}",
                    f"winshare_{variant}", f"streak_{variant}"):
            df[f"{col}_z"] = _zscore_within_channel(df, col)
    return df


def _zscore_within_channel(df: pd.DataFrame, col: str) -> pd.Series:
    def z(s):
        sd = s.std(ddof=0)
        return (s - s.mean()) / sd if sd and sd > 0 else s * 0.0
    return df.groupby("channel_ref")[col].transform(z)


def add_homogeneity_features(
    cfg, df: pd.DataFrame, emb_by_variant: dict[str, dict[str, np.ndarray]]
) -> pd.DataFrame:
    """Attach formula_adherence / rolling_homogeneity / niche_adherence for every variant,
    plus within-channel z-scored formula_adherence when configured."""
    n_trailing = int(cfg.features.trailing_window_n)
    k_window = int(cfg.features.rolling_window_k)
    top_frac = float(cfg.features.niche_top_fraction)
    standardize = bool(cfg.features.standardize_within_channel)

    df = df.copy()
    for variant in VARIANTS:
        emb = emb_by_variant.get(variant, {})
        if not emb:
            continue
        fa = formula_adherence(df, emb, n_trailing)
        df[f"formula_adherence_{variant}"] = fa
        df[f"rolling_homogeneity_{variant}"] = rolling_homogeneity(df, emb, k_window)
        df[f"niche_adherence_{variant}"] = niche_adherence(df, emb, top_frac)
        if standardize:
            df[f"formula_adherence_{variant}_z"] = _zscore_within_channel(
                df, f"formula_adherence_{variant}"
            )
    return df
