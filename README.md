# Study 1 — Stylistic homogeneity → engagement wear-out on YouTube

Observational test of whether a YouTube channel becoming more **stylistically homogeneous**
over time (converging on one thumbnail/title "formula") predicts **faster subsequent
engagement decay** than per-video novelty would predict — measured *within* channels.

> **This is observational.** We do not claim clean causality. A known reverse-causation
> threat (a declining channel may chase the formula *because* it is losing engagement) is
> probed explicitly, not assumed away. See `outputs/FINDINGS.md` (produced in M4).

## Results

We collected **4 niches** via the YouTube Data API — personal finance (240 channels / 26.9k
videos) plus **gaming, tech reviews, beauty** (~80 channels / ~8–9k videos each). **YouTube
Shorts are excluded** from all results below (they are a different vertical format that
contaminates both the outcome and the style measure). The full table is in
**[`outputs/cross_niche_summary.csv`](outputs/cross_niche_summary.csv)**.

We tested two mechanisms the original hypothesis had blurred together:

1. **Conformity / novelty** — does a *single* video that matches the channel's formula get less
   engagement (and does *breaking* it give a bump)?
2. **Cumulative wear-out** — does engagement fall as the channel *piles up* the same formula over
   time (recency-weighted "dose", and consecutive "streak")? **This is the original hypothesis.**

### Coefficients on `engagement_rate` (within-channel, channel fixed effects)

Each cell is the effect of more "sameness" on engagement. **Negative = sameness lowers
engagement** (supports the hypothesis, H1). `*` = statistically significant (p < 0.05); no star
≈ indistinguishable from zero. Magnitudes are on a mean engagement_rate of ~0.03–0.04, so
−0.0010 ≈ a ~3% relative change.

| measure | finance | gaming | tech | beauty |
|---|---:|---:|---:|---:|
| **CONFORMITY** — single on-formula video | | | | |
| &nbsp;&nbsp;`core_thumbnail` | −0.0000 | −0.0014\* | −0.0020\* | −0.0014\* |
| &nbsp;&nbsp;`core_title` | −0.0007\* | −0.0019\* | −0.0016\* | −0.0022\* |
| &nbsp;&nbsp;`core_combined` | −0.0005\* | −0.0020\* | −0.0021\* | −0.0023\* |
| **WEAR-OUT** — cumulative dose | | | | |
| &nbsp;&nbsp;`dose_thumbnail` | +0.0004 | −0.0007\* | −0.0003 | −0.0003 |
| &nbsp;&nbsp;`dose_title` | +0.0003 | −0.0010\* | −0.0000 | −0.0007 |
| &nbsp;&nbsp;`dose_combined` | +0.0006 | −0.0010\* | −0.0002 | −0.0006 |
| **WEAR-OUT** — streak | | | | |
| &nbsp;&nbsp;`streak_combined` | +0.0001 | −0.0006\* | +0.0001 | −0.0004 |
| **NOVELTY REBOUND** — breaking the formula | −0.0009\* | −0.0024\* | −0.0024\* | −0.0025\* |

*(thumbnail = image style, title = text style, combined = both; N per niche ≈ finance 21k,
gaming 6.4k, tech 6.6k, beauty 5.0k videos.)*

### What it means

- **Conformity / novelty is real and universal (top + bottom rows).** In every niche, a video
  that *blends into* the channel's formula gets a little less engagement, and one that *breaks*
  it gets a ~1–2.5% bump. (Thumbnails show this everywhere except finance, whose thumbnails are
  already so uniformly formulaic there is no contrast to detect.) This is a **per-video standout
  effect** — about one video at one moment, not about time.

- **Cumulative wear-out is NOT general — it appears only in gaming (the two WEAR-OUT blocks).**
  The accumulation measures (`dose`, `streak`) are significantly negative *only* in the gaming
  column. Finance and tech are null; beauty leans the right way but is not significant. So the
  original "audience fatigues on the repeated formula over time" hypothesis holds in **1 of 4
  niches**, not as a general law. Plausibly because gaming audiences binge many videos from one
  channel (real repeated exposure), while finance/tech/beauty are watched one-off.

**Bottom line:** *People give a small, consistent bump to videos that break the formula — but
they do not generally wear out on the formula over time. Genuine wear-out shows up only in
gaming, and even there the reverse-causation probe leans the other way, so we cannot yet call it
causal.*

### Where to read more (all Shorts-excluded)
- **[`outputs/cross_niche_summary.csv`](outputs/cross_niche_summary.csv)** — every model × niche,
  with `coef`, `p`, `significant`, and `supports_H1` flags.
- `outputs/no_shorts/FINDINGS.md` (finance) and `outputs/<niche>/no_shorts/FINDINGS.md`
  (gaming / tech_reviews / beauty) — plain-language writeups.
- `outputs/<niche>/no_shorts/tables/model_summaries.md` — full regression tables with CIs.
- `outputs/<niche>/plots/` — within-channel scatter + thumbnail-tile sanity panels.

> **Caveat — the snapshot limitation (see below).** All of this uses one accumulated snapshot
> per video, which is a weak instrument for a time-process like wear-out. The definitive test
> needs the longitudinal `rescrape` data (M5), which has not been started yet.

## The snapshot limitation (read this)
The YouTube Data API and yt-dlp return a **current snapshot** of each video's stats, not a
historical time series. Older videos mechanically have more accumulated views. So:
- **v1 is a snapshot panel**: each video carries accumulated stats + upload date + age.
  We control for video age everywhere and prefer the age-robust
  **engagement_rate = (likes + comments) / views**.
- **`rescrape` (M5)** re-snapshots the *same* video ids on a daily cron, accumulating the
  *true* longitudinal per-video trajectories over time. That is the proper dataset; the
  snapshot panel is the fast proof.

## Quickstart
```bash
make venv          # create .venv
make install       # install pinned deps (requirements.txt)
make smoke         # M1: collect ~10 channels, print the video panel + counts
```
No API key is needed for the default `yt_dlp` backend. To use the Data API instead, set
`collection.backend: youtube_api` in `config.yaml`, copy `.env.example` → `.env`, and add
your `YOUTUBE_API_KEY`.

## Layout
```
config.yaml         # SINGLE source of config — no magic numbers in code
run.py              # orchestrator/CLI: smoke|discover|collect|embed|features|panel|analyze|rescrape
src/
  config.py         # config loader + path helpers
  logging_setup.py  # console + per-stage logfile
  collect.py        # yt-dlp (primary) + YouTube Data API (alt) collectors, cached/retried
  seeds.py          # versioned reproducible channel seed list
  embed.py          # M2 thumbnail (CLIP) + title (MiniLM) embeddings   [stub until M2]
  features.py       # M3 homogeneity scores + engagement features        [stub until M3]
  build_panel.py    # M3 assemble video-level + channel-week panels      [stub until M3]
  analyze.py        # M4 PanelOLS w/ channel FE, direction probe, robustness [stub until M4]
  rescrape.py       # M5 daily longitudinal appender                      [stub until M5]
data/   seeds/ raw/ thumbnails/ embeddings/ panels/    (most gitignored; seeds versioned)
outputs/ tables/ plots/ logs/
docs/   data_dictionary.md
```

## Milestones
- **M1** scaffold + config + logging; smoke-collect 10 channels. ← *current*
- **M2** thumbnail + title embeddings (cached) + similarity sanity panels.
- **M3** scale to the full seed list; build both panels + data dictionary.
- **M4** full analysis: channel-FE PanelOLS, reverse-causation probe, robustness, FINDINGS.md.
- **M5** wire up `rescrape` + cron docs so the longitudinal dataset starts accumulating.

## Longitudinal rescrape (M5) — start accumulating real trajectories
The snapshot panel is one point in time per video. `rescrape` re-snapshots the *same* video ids
and appends a row per `(video_id, scrape_date)` to `data/panels/longitudinal_snapshots.parquet`
(idempotent per day; uses fresh, uncached extractions). Run it daily so per-video view/like/comment
trajectories build up:
```bash
# test once
make rescrape           # == .venv/bin/python run.py rescrape

# cron: every day at 06:00 (use absolute paths)
crontab -e
0 6 * * *  cd /Users/brighton/Documents/study1 && /Users/brighton/Documents/study1/.venv/bin/python run.py rescrape >> outputs/logs/rescrape_cron.log 2>&1
```
After a few weeks you'll have a genuine longitudinal dataset to model engagement *decay* directly,
rather than inferring it from an age-controlled snapshot.

## Reproducibility
- One config file; model versions pinned; seeds set.
- Everything cached & resumable — re-runs do **not** re-download or re-embed cached items.
- All raw API/yt-dlp responses cached as JSON under `data/raw/` keyed by id.
