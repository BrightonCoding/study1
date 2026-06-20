"""
embed.py — M2. Thumbnail (CLIP image encoder) + title (sentence-transformers) embeddings.

Outputs three variant embedding stores under data/embeddings/, each a (matrix.npy, ids.json)
pair keyed by video_id:
  * thumbnail.npy  — open_clip image encoder (config embedding.thumbnail_model/_pretrained)
  * title.npy      — sentence-transformers title encoder (config embedding.title_model)
  * combined.npy   — L2-normalize each, weighted-concat, renormalize (config embedding.combined)

Design choices:
  * Store as a dense .npy matrix + parallel ids.json (not 500-wide parquet): downstream
    homogeneity math is pure numpy cosine over these matrices, so a matrix is the natural form.
  * Vectors are L2-NORMALIZED at write time. Cosine similarity then = plain dot product, and
    centroid/mean-similarity computations are consistent across the codebase.
  * Fully cached & resumable: we only encode video_ids not already present in a variant store.
  * Deterministic: eval mode, no dropout, fixed model weights (pinned in requirements).

Reproducibility note on the COMBINED variant: thumbnail (512-d for ViT-B/32) and title
(384-d for MiniLM) live in different spaces and have different native scales. We L2-normalize
each sub-vector, apply the configured weights, concatenate, then L2-normalize the whole. So the
combined cosine is a weighted average of the thumbnail-cosine and title-cosine — interpretable,
and the weights are the only knob.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

# Keep logs readable: silence HF/tokenizers progress bars & advisory chatter. The model
# versions are pinned, so the downloads are deterministic and not worth streaming to the log.
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("TRANSFORMERS_NO_ADVISORY_WARNINGS", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import numpy as np
import pandas as pd

from .config import Cfg
from .logging_setup import get_logger


# --------------------------------------------------------------------------- #
# variant store I/O  (matrix.npy + ids.json), resumable
# --------------------------------------------------------------------------- #
def _store_paths(cfg: Cfg, variant: str) -> tuple[Path, Path]:
    d = cfg.path("embeddings_dir")
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{variant}.npy", d / f"{variant}_ids.json"


def load_embeddings(cfg: Cfg, variant: str) -> tuple[np.ndarray, list[str]]:
    """Return (matrix, ids). Empty if not computed yet."""
    mat_p, ids_p = _store_paths(cfg, variant)
    if mat_p.exists() and ids_p.exists():
        mat = np.load(mat_p)
        ids = json.loads(ids_p.read_text())
        return mat, ids
    return np.zeros((0, 0), dtype=np.float32), []


def embeddings_as_dict(cfg: Cfg, variant: str) -> dict[str, np.ndarray]:
    mat, ids = load_embeddings(cfg, variant)
    return {vid: mat[i] for i, vid in enumerate(ids)}


def _save_store(cfg: Cfg, variant: str, mat: np.ndarray, ids: list[str]) -> None:
    mat_p, ids_p = _store_paths(cfg, variant)
    np.save(mat_p, mat.astype(np.float32))
    ids_p.write_text(json.dumps(ids))


def _l2(mat: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(mat, axis=1, keepdims=True)
    n[n == 0] = 1.0
    return mat / n


def _resolve_device(pref: str):
    import torch

    if pref != "auto":
        return pref
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


# --------------------------------------------------------------------------- #
# encoders
# --------------------------------------------------------------------------- #
def _encode_thumbnails(cfg: Cfg, log, video_ids: list[str], titleless_paths: dict[str, str]):
    """Encode thumbnails with open_clip. Returns (ids_encoded, matrix) for ids with a usable
    image on disk; ids whose thumbnail is missing/corrupt are skipped and reported."""
    import open_clip
    import torch
    from PIL import Image

    device = _resolve_device(str(cfg.embedding.device))
    arch = str(cfg.embedding.thumbnail_model)
    pretrained = str(cfg.embedding.thumbnail_pretrained)
    log.info(f"loading CLIP {arch}/{pretrained} on {device}")
    model, _, preprocess = open_clip.create_model_and_transforms(arch, pretrained=pretrained)
    model = model.to(device).eval()

    bs = int(cfg.embedding.batch_size)
    out_ids: list[str] = []
    vecs: list[np.ndarray] = []
    batch_imgs, batch_ids = [], []

    def _flush():
        if not batch_imgs:
            return
        with torch.no_grad():
            x = torch.stack(batch_imgs).to(device)
            feats = model.encode_image(x)
            feats = feats / feats.norm(dim=-1, keepdim=True)
        vecs.append(feats.cpu().numpy().astype(np.float32))
        out_ids.extend(batch_ids)
        batch_imgs.clear()
        batch_ids.clear()

    n_missing = 0
    for vid in video_ids:
        p = titleless_paths.get(vid)
        if not p or not Path(p).exists():
            n_missing += 1
            continue
        try:
            img = Image.open(p).convert("RGB")
            batch_imgs.append(preprocess(img))
            batch_ids.append(vid)
        except Exception as e:  # noqa: BLE001
            log.info(f"thumbnail unreadable for {vid}: {e}")
            n_missing += 1
            continue
        if len(batch_imgs) >= bs:
            _flush()
    _flush()
    if n_missing:
        log.info(f"thumbnail encode: skipped {n_missing} videos w/o usable image")
    mat = np.vstack(vecs) if vecs else np.zeros((0, 512), dtype=np.float32)
    return out_ids, mat


def _encode_titles(cfg: Cfg, log, video_ids: list[str], titles: dict[str, str]):
    backend = str(cfg.embedding.title_backend)
    device = _resolve_device(str(cfg.embedding.device))
    texts = [titles.get(v, "") or "" for v in video_ids]

    if backend == "sentence_transformers":
        from sentence_transformers import SentenceTransformer

        name = str(cfg.embedding.title_model)
        log.info(f"loading sentence-transformers {name} on {device}")
        model = SentenceTransformer(name, device=device)
        emb = model.encode(
            texts,
            batch_size=int(cfg.embedding.batch_size),
            normalize_embeddings=True,  # L2-normalized -> cosine == dot
            show_progress_bar=False,
            convert_to_numpy=True,
        ).astype(np.float32)
    elif backend == "clip_text":
        import open_clip
        import torch

        arch = str(cfg.embedding.thumbnail_model)
        pretrained = str(cfg.embedding.thumbnail_pretrained)
        model, _, _ = open_clip.create_model_and_transforms(arch, pretrained=pretrained)
        model = model.to(device).eval()
        tok = open_clip.get_tokenizer(arch)
        with torch.no_grad():
            t = tok(texts).to(device)
            feats = model.encode_text(t)
            feats = feats / feats.norm(dim=-1, keepdim=True)
        emb = feats.cpu().numpy().astype(np.float32)
    else:
        raise ValueError(f"unknown embedding.title_backend: {backend!r}")
    return list(video_ids), emb


def _build_combined(cfg: Cfg, log, thumb: dict[str, np.ndarray], title: dict[str, np.ndarray]):
    """Combined = renorm( [w_t * thumb_norm ; w_l * title_norm] ) for ids present in BOTH."""
    wt = float(cfg.embedding.combined.thumbnail_weight)
    wl = float(cfg.embedding.combined.title_weight)
    ids = [v for v in thumb if v in title]
    if not ids:
        return [], np.zeros((0, 0), dtype=np.float32)
    th = _l2(np.vstack([thumb[v] for v in ids])) * wt
    tl = _l2(np.vstack([title[v] for v in ids])) * wl
    combined = _l2(np.hstack([th, tl]))
    log.info(f"combined: {len(ids)} videos, dim={combined.shape[1]} (w_thumb={wt}, w_title={wl})")
    return ids, combined


# --------------------------------------------------------------------------- #
# orchestration  (resumable: only encodes ids not already stored)
# --------------------------------------------------------------------------- #
def _load_panel(cfg: Cfg) -> pd.DataFrame:
    """Pick the list of videos to embed. Precedence: the RAW collected panel (full run) >
    the smoke panel (M2) > the already-built panel (fallback). We read the RAW panel, not the
    built `video_panel.parquet`, so embeddings track freshly collected ids rather than a stale
    built panel from a prior run."""
    raw = cfg.path("panels_dir") / "raw_video_panel.parquet"
    smoke = cfg.path("panels_dir") / "smoke_video_panel.parquet"
    built = cfg.path("video_panel_parquet")
    for p in (raw, smoke, built):
        if p.exists():
            return pd.read_parquet(p)
    raise FileNotFoundError(
        f"no video panel found ({raw} / {smoke}). Run `collect` (or `smoke`) first."
    )


def run_embeddings(cfg: Cfg, log) -> dict:
    df = _load_panel(cfg)
    df = df.dropna(subset=["video_id"]).drop_duplicates(subset=["video_id"])
    all_ids = df["video_id"].tolist()
    titles = dict(zip(df["video_id"], df["title"].fillna("")))
    thumb_paths = dict(zip(df["video_id"], df.get("thumbnail_path")))
    log.info(f"embedding stage over {len(all_ids)} videos from panel")

    summary = {}

    # ---- thumbnail (resumable) ----
    have_mat, have_ids = load_embeddings(cfg, "thumbnail")
    todo = [v for v in all_ids if v not in set(have_ids)]
    log.info(f"thumbnail: {len(have_ids)} cached, {len(todo)} to encode")
    if todo:
        new_ids, new_mat = _encode_thumbnails(cfg, log, todo, thumb_paths)
        if have_ids and new_ids:
            mat = np.vstack([have_mat, new_mat])
            ids = have_ids + new_ids
        elif new_ids:
            mat, ids = new_mat, new_ids
        else:
            mat, ids = have_mat, have_ids
        _save_store(cfg, "thumbnail", mat, ids)
    summary["thumbnail"] = len(load_embeddings(cfg, "thumbnail")[1])

    # ---- title (resumable) ----
    have_mat, have_ids = load_embeddings(cfg, "title")
    todo = [v for v in all_ids if v not in set(have_ids)]
    log.info(f"title: {len(have_ids)} cached, {len(todo)} to encode")
    if todo:
        new_ids, new_mat = _encode_titles(cfg, log, todo, titles)
        if have_ids and new_ids:
            mat = np.vstack([have_mat, new_mat])
            ids = have_ids + new_ids
        else:
            mat, ids = new_mat, new_ids
        _save_store(cfg, "title", mat, ids)
    summary["title"] = len(load_embeddings(cfg, "title")[1])

    # ---- combined (rebuilt from the two normalized stores) ----
    if bool(cfg.embedding.combined.enabled):
        thumb_d = embeddings_as_dict(cfg, "thumbnail")
        title_d = embeddings_as_dict(cfg, "title")
        ids, mat = _build_combined(cfg, log, thumb_d, title_d)
        if ids:
            _save_store(cfg, "combined", mat, ids)
        summary["combined"] = len(ids)

    log.info(f"embedding stage DONE: {summary}")
    return summary


def make_sanity_panels(cfg, log, variant: str = "thumbnail", n_channels: int = 3, k: int = 6):
    """
    M2 sanity check: for the channels with the most videos, tile the thumbnails that are MOST
    vs LEAST similar to the channel's own thumbnail centroid. This is the human-eyeball test —
    do the high-similarity thumbnails actually look like "the formula", and the low ones look
    off-formula? Saves one PNG per channel to outputs/plots/sanity_<variant>_<channel>.png.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from PIL import Image

    df = _load_panel(cfg)
    emb = embeddings_as_dict(cfg, variant)
    df = df[df["video_id"].isin(emb.keys())].copy()
    thumb_paths = dict(zip(df["video_id"], df.get("thumbnail_path")))

    # pick channels with the most embedded videos
    top_channels = (
        df.groupby("channel_ref")["video_id"].count().sort_values(ascending=False).index.tolist()
    )
    out_paths = []
    plots_dir = cfg.path("plots_dir")
    plots_dir.mkdir(parents=True, exist_ok=True)

    for ch in top_channels[:n_channels]:
        sub = df[df["channel_ref"] == ch]
        ids = [v for v in sub["video_id"] if v in emb]
        if len(ids) < 2 * k:
            continue
        mat = _l2(np.vstack([emb[v] for v in ids]))
        centroid = _l2(mat.mean(axis=0, keepdims=True))[0]
        sims = mat @ centroid  # cosine to channel centroid (formula adherence)
        order = np.argsort(sims)[::-1]
        most = [(ids[i], sims[i]) for i in order[:k]]
        least = [(ids[i], sims[i]) for i in order[-k:]]

        fig, axes = plt.subplots(2, k, figsize=(2.2 * k, 5.2))
        fig.suptitle(
            f"{ch} — {variant} similarity to channel centroid  (top: most 'on-formula', bottom: least)",
            fontsize=11,
        )
        for row, group, label in [(0, most, "MOST"), (1, least, "LEAST")]:
            for col, (vid, s) in enumerate(group):
                ax = axes[row, col]
                ax.axis("off")
                p = thumb_paths.get(vid)
                if p and Path(p).exists():
                    try:
                        ax.imshow(Image.open(p).convert("RGB"))
                    except Exception:  # noqa: BLE001
                        pass
                ax.set_title(f"{label}\ncos={s:.3f}", fontsize=8)
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        safe = ch.replace("@", "").replace("/", "_")
        out = plots_dir / f"sanity_{variant}_{safe}.png"
        fig.savefig(out, dpi=110)
        plt.close(fig)
        out_paths.append(out)
        log.info(f"sanity panel: {out}  (centroid-sim range {sims.min():.3f}..{sims.max():.3f})")
    return out_paths


def main(cfg, log=None):
    log = log or get_logger("embed", cfg.path("logs_dir"))
    summary = run_embeddings(cfg, log)
    make_sanity_panels(cfg, log, variant="thumbnail")
    return summary
