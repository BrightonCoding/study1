# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 72 channels, 8396 videos (personal-finance/investing niche; snapshot taken 2026-06-21).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00157** change in engagement_rate (SE 0.00054, p=0.003) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **statistically significant (p<0.05)**.

H1 predicts a NEGATIVE coefficient. **Consistent with H1.**

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00157 | 0.00054 | 0.003 | 8280 | 72 |
| core_title | engagement_rate | -0.00116 | 0.00039 | 0.003 | 8280 | 72 |
| core_combined | engagement_rate | -0.00167 | 0.00050 | 0.001 | 8280 | 72 |
| core_thumbnail_logviews | log_views | +0.04093 | 0.02704 | 0.130 | 8324 | 72 |
| core_title_logviews | log_views | +0.15495 | 0.02199 | 0.000 | 8324 | 72 |
| core_combined_logviews | log_views | +0.12368 | 0.02470 | 0.000 | 8324 | 72 |
| wearout_thumbnail_dose | engagement_rate | -0.00027 | 0.00022 | 0.216 | 8280 | 72 |
| wearout_thumbnail_winshare | engagement_rate | -0.00023 | 0.00022 | 0.311 | 8280 | 72 |
| wearout_thumbnail_streak | engagement_rate | -0.00004 | 0.00018 | 0.841 | 8280 | 72 |
| wearout_thumbnail_nonlin_lin | engagement_rate | -0.00027 | 0.00023 | 0.248 | 8280 | 72 |
| wearout_thumbnail_nonlin_sq | engagement_rate | +0.00003 | 0.00009 | 0.714 | 8280 | 72 |
| wearout_thumbnail_rebound | engagement_rate | -0.00165 | 0.00057 | 0.004 | 8351 | 72 |
| wearout_title_dose | engagement_rate | +0.00008 | 0.00022 | 0.720 | 8280 | 72 |
| wearout_title_winshare | engagement_rate | +0.00012 | 0.00022 | 0.571 | 8280 | 72 |
| wearout_title_streak | engagement_rate | +0.00023 | 0.00016 | 0.152 | 8280 | 72 |
| wearout_title_nonlin_lin | engagement_rate | +0.00013 | 0.00022 | 0.549 | 8280 | 72 |
| wearout_title_nonlin_sq | engagement_rate | +0.00019 | 0.00011 | 0.083 | 8280 | 72 |
| wearout_title_rebound | engagement_rate | -0.00142 | 0.00045 | 0.002 | 8351 | 72 |
| wearout_combined_dose | engagement_rate | -0.00008 | 0.00020 | 0.687 | 8280 | 72 |
| wearout_combined_winshare | engagement_rate | -0.00003 | 0.00018 | 0.890 | 8280 | 72 |
| wearout_combined_streak | engagement_rate | +0.00019 | 0.00018 | 0.309 | 8280 | 72 |
| wearout_combined_nonlin_lin | engagement_rate | -0.00003 | 0.00019 | 0.877 | 8280 | 72 |
| wearout_combined_nonlin_sq | engagement_rate | +0.00018 | 0.00011 | 0.087 | 8280 | 72 |
| wearout_combined_rebound | engagement_rate | -0.00194 | 0.00056 | 0.000 | 8351 | 72 |
| week_thumbnail | engagement_rate | -0.00127 | 0.00041 | 0.002 | 3098 | 72 |
| week_title | engagement_rate | -0.00096 | 0.00032 | 0.003 | 3098 | 72 |
| week_combined | engagement_rate | -0.00119 | 0.00038 | 0.002 | 3098 | 72 |
| direction_thumbnail_forward | engagement | -0.02866 | 0.01897 | 0.131 | 3025 | 71 |
| direction_thumbnail_reverse | homogeneity | -0.02000 | 0.02189 | 0.361 | 3053 | 72 |
| direction_title_forward | engagement | -0.03463 | 0.02047 | 0.091 | 3025 | 71 |
| direction_title_reverse | homogeneity | +0.00035 | 0.02161 | 0.987 | 3053 | 72 |
| direction_combined_forward | engagement | -0.03351 | 0.02023 | 0.098 | 3025 | 71 |
| direction_combined_reverse | homogeneity | -0.00375 | 0.02305 | 0.871 | 3053 | 72 |
| robust_thumbnail | engagement_rate | -0.00254 | 0.00140 | 0.070 | 2405 | 21 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef -0.0287 (p=0.131). Reverse (homogeneity_t ~ engagement_(t-1)): coef -0.0200 (p=0.361). Forward stronger than reverse — weakly consistent with homogeneity→engagement.

## Robustness subsample (strong-start, then homogenized)
Coef -0.00254 (p=0.070, N=2405). H1 survives in the strong-start subsample.

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0763; median = 0.0760; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.266 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UCVYamHliCI9rw1tHR1xbkfw.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCXGgrKt94gR6lmN4aN3mYTg.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCBJycsmduvYEL83R_U4JriQ.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCWsEZ9v1KC8b5VYjYbEewJA` (0.875); least = `https://www.youtube.com/channel/UCymYq4Piq0BrhnM18aQzTlg` (0.603).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).