# Study 1 — Stylistic homogeneity → engagement wear-out on YouTube

Observational test of whether a YouTube channel becoming more **stylistically homogeneous**
over time (converging on one thumbnail/title "formula") predicts **faster subsequent
engagement decay** than per-video novelty would predict — measured *within* channels.

> **This is observational.** We do not claim clean causality. A known reverse-causation
> threat (a declining channel may chase the formula *because* it is losing engagement) is
> probed explicitly, not assumed away. See `outputs/FINDINGS.md` (produced in M4).

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
