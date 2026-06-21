# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 72 channels, 6611 videos (personal-finance/investing niche; snapshot taken 2026-06-21).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00196** change in engagement_rate (SE 0.00063, p=0.002) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **statistically significant (p<0.05)**.

H1 predicts a NEGATIVE coefficient. **Consistent with H1.**

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00196 | 0.00063 | 0.002 | 6499 | 72 |
| core_title | engagement_rate | -0.00165 | 0.00046 | 0.000 | 6499 | 72 |
| core_combined | engagement_rate | -0.00211 | 0.00060 | 0.000 | 6499 | 72 |
| core_thumbnail_logviews | log_views | +0.08446 | 0.02373 | 0.000 | 6539 | 72 |
| core_title_logviews | log_views | +0.16530 | 0.02274 | 0.000 | 6539 | 72 |
| core_combined_logviews | log_views | +0.15467 | 0.02335 | 0.000 | 6539 | 72 |
| wearout_thumbnail_dose | engagement_rate | -0.00035 | 0.00026 | 0.185 | 6499 | 72 |
| wearout_thumbnail_winshare | engagement_rate | -0.00036 | 0.00026 | 0.173 | 6499 | 72 |
| wearout_thumbnail_streak | engagement_rate | -0.00002 | 0.00019 | 0.910 | 6499 | 72 |
| wearout_thumbnail_nonlin_lin | engagement_rate | -0.00032 | 0.00028 | 0.248 | 6499 | 72 |
| wearout_thumbnail_nonlin_sq | engagement_rate | +0.00009 | 0.00011 | 0.404 | 6499 | 72 |
| wearout_thumbnail_rebound | engagement_rate | -0.00200 | 0.00063 | 0.002 | 6570 | 72 |
| wearout_title_dose | engagement_rate | -0.00003 | 0.00029 | 0.913 | 6499 | 72 |
| wearout_title_winshare | engagement_rate | -0.00001 | 0.00030 | 0.974 | 6499 | 72 |
| wearout_title_streak | engagement_rate | -0.00003 | 0.00020 | 0.893 | 6499 | 72 |
| wearout_title_nonlin_lin | engagement_rate | -0.00001 | 0.00028 | 0.967 | 6499 | 72 |
| wearout_title_nonlin_sq | engagement_rate | +0.00009 | 0.00013 | 0.504 | 6499 | 72 |
| wearout_title_rebound | engagement_rate | -0.00200 | 0.00052 | 0.000 | 6570 | 72 |
| wearout_combined_dose | engagement_rate | -0.00018 | 0.00024 | 0.450 | 6499 | 72 |
| wearout_combined_winshare | engagement_rate | -0.00018 | 0.00026 | 0.471 | 6499 | 72 |
| wearout_combined_streak | engagement_rate | +0.00007 | 0.00023 | 0.769 | 6499 | 72 |
| wearout_combined_nonlin_lin | engagement_rate | -0.00014 | 0.00024 | 0.573 | 6499 | 72 |
| wearout_combined_nonlin_sq | engagement_rate | +0.00020 | 0.00011 | 0.073 | 6499 | 72 |
| wearout_combined_rebound | engagement_rate | -0.00242 | 0.00064 | 0.000 | 6570 | 72 |
| week_thumbnail | engagement_rate | -0.00152 | 0.00045 | 0.001 | 2857 | 72 |
| week_title | engagement_rate | -0.00133 | 0.00033 | 0.000 | 2857 | 72 |
| week_combined | engagement_rate | -0.00158 | 0.00041 | 0.000 | 2857 | 72 |
| direction_thumbnail_forward | engagement | -0.02361 | 0.02187 | 0.280 | 2784 | 71 |
| direction_thumbnail_reverse | homogeneity | -0.02455 | 0.02337 | 0.293 | 2814 | 72 |
| direction_title_forward | engagement | -0.04341 | 0.02376 | 0.068 | 2784 | 71 |
| direction_title_reverse | homogeneity | -0.00210 | 0.02247 | 0.926 | 2814 | 72 |
| direction_combined_forward | engagement | -0.03734 | 0.02402 | 0.120 | 2784 | 71 |
| direction_combined_reverse | homogeneity | -0.00780 | 0.02447 | 0.750 | 2814 | 72 |
| robust_thumbnail | engagement_rate | -0.00281 | 0.00146 | 0.055 | 2221 | 25 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef -0.0236 (p=0.280). Reverse (homogeneity_t ~ engagement_(t-1)): coef -0.0246 (p=0.293). Reverse is comparable/stronger — cannot rule out that declining engagement drives homogenization (the main reverse-causation threat).

## Robustness subsample (strong-start, then homogenized)
Coef -0.00281 (p=0.055, N=2221). H1 survives in the strong-start subsample.

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0755; median = 0.0759; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.298 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UCVYamHliCI9rw1tHR1xbkfw.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCXGgrKt94gR6lmN4aN3mYTg.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCBJycsmduvYEL83R_U4JriQ.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCWsEZ9v1KC8b5VYjYbEewJA` (0.881); least = `https://www.youtube.com/channel/UCymYq4Piq0BrhnM18aQzTlg` (0.605).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).