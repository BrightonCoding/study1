# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 14 channels, 1023 videos (personal-finance/investing niche; snapshot taken 2026-06-20).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00020** change in engagement_rate (SE 0.00021, p=0.341) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **not statistically significant (p≥0.05)**.

H1 predicts a NEGATIVE coefficient. **Not clearly supported** at conventional significance — reported honestly.

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00020 | 0.00021 | 0.341 | 1009 | 14 |
| core_title | engagement_rate | -0.00116 | 0.00052 | 0.028 | 1009 | 14 |
| core_combined | engagement_rate | -0.00088 | 0.00046 | 0.057 | 1009 | 14 |
| core_thumbnail_logviews | log_views | -0.00743 | 0.05031 | 0.883 | 1009 | 14 |
| core_title_logviews | log_views | +0.06570 | 0.05395 | 0.224 | 1009 | 14 |
| core_combined_logviews | log_views | +0.04292 | 0.04565 | 0.347 | 1009 | 14 |
| week_thumbnail | engagement_rate | -0.00048 | 0.00020 | 0.019 | 792 | 14 |
| week_title | engagement_rate | -0.00114 | 0.00054 | 0.036 | 792 | 14 |
| week_combined | engagement_rate | -0.00095 | 0.00043 | 0.029 | 792 | 14 |
| direction_thumbnail_forward | engagement | -0.03817 | 0.04449 | 0.391 | 778 | 14 |
| direction_thumbnail_reverse | homogeneity | -0.00200 | 0.02717 | 0.941 | 790 | 14 |
| direction_title_forward | engagement | -0.03386 | 0.04621 | 0.464 | 778 | 14 |
| direction_title_reverse | homogeneity | +0.01972 | 0.03935 | 0.616 | 790 | 14 |
| direction_combined_forward | engagement | -0.04033 | 0.05328 | 0.449 | 778 | 14 |
| direction_combined_reverse | homogeneity | +0.01185 | 0.03771 | 0.753 | 790 | 14 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef -0.0382 (p=0.391). Reverse (homogeneity_t ~ engagement_(t-1)): coef -0.0020 (p=0.941). Forward stronger than reverse — weakly consistent with homogeneity→engagement.

## Robustness subsample (strong-start, then homogenized)
_Subsample too small to estimate._

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0755; median = 0.0758; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.229 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_ThePlainBagel.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCIbslwukNCyVp-XMz_2-gmw.png`, `sanity_thumbnail_BenFelixCSI.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCGy7SkBjcIAgTiwkXEtPnYg` (0.777); least = `https://www.youtube.com/channel/UCFBpVaKCC0ajGps1vf0AgBg` (0.622).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).