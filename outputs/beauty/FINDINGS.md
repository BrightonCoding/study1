# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 77 channels, 8445 videos (personal-finance/investing niche; snapshot taken 2026-06-21).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00081** change in engagement_rate (SE 0.00066, p=0.223) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **not statistically significant (p≥0.05)**.

H1 predicts a NEGATIVE coefficient. **Not clearly supported** at conventional significance — reported honestly.

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00081 | 0.00066 | 0.223 | 8216 | 76 |
| core_title | engagement_rate | -0.00106 | 0.00058 | 0.066 | 8216 | 76 |
| core_combined | engagement_rate | -0.00126 | 0.00065 | 0.052 | 8216 | 76 |
| core_thumbnail_logviews | log_views | +0.05900 | 0.02415 | 0.015 | 8368 | 77 |
| core_title_logviews | log_views | +0.07061 | 0.02319 | 0.002 | 8368 | 77 |
| core_combined_logviews | log_views | +0.07744 | 0.02301 | 0.001 | 8368 | 77 |
| wearout_thumbnail_dose | engagement_rate | +0.00068 | 0.00049 | 0.165 | 8216 | 76 |
| wearout_thumbnail_winshare | engagement_rate | +0.00062 | 0.00050 | 0.219 | 8216 | 76 |
| wearout_thumbnail_streak | engagement_rate | +0.00055 | 0.00036 | 0.127 | 8216 | 76 |
| wearout_thumbnail_nonlin_lin | engagement_rate | +0.00069 | 0.00046 | 0.132 | 8216 | 76 |
| wearout_thumbnail_nonlin_sq | engagement_rate | +0.00003 | 0.00021 | 0.901 | 8216 | 76 |
| wearout_thumbnail_rebound | engagement_rate | -0.00070 | 0.00068 | 0.303 | 8290 | 76 |
| wearout_title_dose | engagement_rate | -0.00029 | 0.00049 | 0.555 | 8216 | 76 |
| wearout_title_winshare | engagement_rate | -0.00018 | 0.00048 | 0.713 | 8216 | 76 |
| wearout_title_streak | engagement_rate | +0.00012 | 0.00033 | 0.716 | 8216 | 76 |
| wearout_title_nonlin_lin | engagement_rate | -0.00030 | 0.00048 | 0.523 | 8216 | 76 |
| wearout_title_nonlin_sq | engagement_rate | -0.00005 | 0.00022 | 0.836 | 8216 | 76 |
| wearout_title_rebound | engagement_rate | -0.00085 | 0.00062 | 0.170 | 8290 | 76 |
| wearout_combined_dose | engagement_rate | +0.00023 | 0.00051 | 0.656 | 8216 | 76 |
| wearout_combined_winshare | engagement_rate | +0.00025 | 0.00052 | 0.632 | 8216 | 76 |
| wearout_combined_streak | engagement_rate | +0.00001 | 0.00035 | 0.988 | 8216 | 76 |
| wearout_combined_nonlin_lin | engagement_rate | +0.00023 | 0.00049 | 0.629 | 8216 | 76 |
| wearout_combined_nonlin_sq | engagement_rate | +0.00002 | 0.00024 | 0.920 | 8216 | 76 |
| wearout_combined_rebound | engagement_rate | -0.00113 | 0.00070 | 0.107 | 8290 | 76 |
| week_thumbnail | engagement_rate | -0.00030 | 0.00043 | 0.479 | 3681 | 76 |
| week_title | engagement_rate | -0.00155 | 0.00057 | 0.007 | 3681 | 76 |
| week_combined | engagement_rate | -0.00132 | 0.00050 | 0.008 | 3681 | 76 |
| direction_thumbnail_forward | engagement | -0.01696 | 0.01948 | 0.384 | 3607 | 76 |
| direction_thumbnail_reverse | homogeneity | -0.06669 | 0.02150 | 0.002 | 3642 | 76 |
| direction_title_forward | engagement | -0.03242 | 0.02072 | 0.118 | 3607 | 76 |
| direction_title_reverse | homogeneity | -0.05158 | 0.02202 | 0.019 | 3642 | 76 |
| direction_combined_forward | engagement | -0.03619 | 0.02150 | 0.092 | 3607 | 76 |
| direction_combined_reverse | homogeneity | -0.07001 | 0.02203 | 0.001 | 3642 | 76 |
| robust_thumbnail | engagement_rate | -0.00004 | 0.00158 | 0.980 | 2538 | 23 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef -0.0170 (p=0.384). Reverse (homogeneity_t ~ engagement_(t-1)): coef -0.0667 (p=0.002). Reverse is comparable/stronger — cannot rule out that declining engagement drives homogenization (the main reverse-causation threat).

## Robustness subsample (strong-start, then homogenized)
Coef -0.00004 (p=0.980, N=2538). H1 does not clearly survive here.

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0765; median = 0.0752; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.273 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UCzTKskwIc_-a0cGvCXA848Q.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCucot-Zp428OwkyRm2I7v2Q.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UC4qk9TtGhBKCkoWz5qGJcGg.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UClm9D6Std5EnJruG4XtoS7g` (0.901); least = `https://www.youtube.com/channel/UCSavnEw5et6sKtWYXLzP2cg` (0.653).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).