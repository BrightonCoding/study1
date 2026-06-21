# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 73 channels, 6431 videos (personal-finance/investing niche; snapshot taken 2026-06-21).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00145** change in engagement_rate (SE 0.00026, p=0.000) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **statistically significant (p<0.05)**.

H1 predicts a NEGATIVE coefficient. **Consistent with H1.**

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00145 | 0.00026 | 0.000 | 6280 | 72 |
| core_title | engagement_rate | -0.00187 | 0.00028 | 0.000 | 6280 | 72 |
| core_combined | engagement_rate | -0.00201 | 0.00029 | 0.000 | 6280 | 72 |
| core_thumbnail_logviews | log_views | +0.05753 | 0.03575 | 0.108 | 6358 | 73 |
| core_title_logviews | log_views | +0.08389 | 0.03790 | 0.027 | 6358 | 73 |
| core_combined_logviews | log_views | +0.08076 | 0.04152 | 0.052 | 6358 | 73 |
| wearout_thumbnail_dose | engagement_rate | -0.00072 | 0.00028 | 0.009 | 6280 | 72 |
| wearout_thumbnail_winshare | engagement_rate | -0.00076 | 0.00026 | 0.004 | 6280 | 72 |
| wearout_thumbnail_streak | engagement_rate | -0.00039 | 0.00021 | 0.056 | 6280 | 72 |
| wearout_thumbnail_nonlin_lin | engagement_rate | -0.00066 | 0.00027 | 0.015 | 6280 | 72 |
| wearout_thumbnail_nonlin_sq | engagement_rate | +0.00014 | 0.00010 | 0.150 | 6280 | 72 |
| wearout_thumbnail_rebound | engagement_rate | -0.00155 | 0.00026 | 0.000 | 6350 | 72 |
| wearout_title_dose | engagement_rate | -0.00101 | 0.00026 | 0.000 | 6280 | 72 |
| wearout_title_winshare | engagement_rate | -0.00088 | 0.00023 | 0.000 | 6280 | 72 |
| wearout_title_streak | engagement_rate | -0.00069 | 0.00021 | 0.001 | 6280 | 72 |
| wearout_title_nonlin_lin | engagement_rate | -0.00104 | 0.00028 | 0.000 | 6280 | 72 |
| wearout_title_nonlin_sq | engagement_rate | -0.00006 | 0.00010 | 0.540 | 6280 | 72 |
| wearout_title_rebound | engagement_rate | -0.00228 | 0.00032 | 0.000 | 6350 | 72 |
| wearout_combined_dose | engagement_rate | -0.00100 | 0.00028 | 0.000 | 6280 | 72 |
| wearout_combined_winshare | engagement_rate | -0.00093 | 0.00026 | 0.000 | 6280 | 72 |
| wearout_combined_streak | engagement_rate | -0.00063 | 0.00022 | 0.004 | 6280 | 72 |
| wearout_combined_nonlin_lin | engagement_rate | -0.00103 | 0.00030 | 0.001 | 6280 | 72 |
| wearout_combined_nonlin_sq | engagement_rate | -0.00006 | 0.00010 | 0.569 | 6280 | 72 |
| wearout_combined_rebound | engagement_rate | -0.00241 | 0.00033 | 0.000 | 6350 | 72 |
| week_thumbnail | engagement_rate | -0.00110 | 0.00032 | 0.001 | 2874 | 71 |
| week_title | engagement_rate | -0.00181 | 0.00034 | 0.000 | 2874 | 71 |
| week_combined | engagement_rate | -0.00172 | 0.00034 | 0.000 | 2874 | 71 |
| direction_thumbnail_forward | engagement | -0.01081 | 0.02210 | 0.625 | 2799 | 66 |
| direction_thumbnail_reverse | homogeneity | -0.04650 | 0.01994 | 0.020 | 2831 | 67 |
| direction_title_forward | engagement | -0.05107 | 0.02226 | 0.022 | 2799 | 66 |
| direction_title_reverse | homogeneity | -0.05721 | 0.02349 | 0.015 | 2831 | 67 |
| direction_combined_forward | engagement | -0.03729 | 0.02250 | 0.098 | 2799 | 66 |
| direction_combined_reverse | homogeneity | -0.06001 | 0.02230 | 0.007 | 2831 | 67 |
| robust_thumbnail | engagement_rate | -0.00141 | 0.00052 | 0.007 | 2064 | 22 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef -0.0108 (p=0.625). Reverse (homogeneity_t ~ engagement_(t-1)): coef -0.0465 (p=0.020). Reverse is comparable/stronger — cannot rule out that declining engagement drives homogenization (the main reverse-causation threat).

## Robustness subsample (strong-start, then homogenized)
Coef -0.00141 (p=0.007, N=2064). H1 survives in the strong-start subsample.

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0815; median = 0.0765; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.342 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UC7_YxT-KID8kRbqZo7MyscQ.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCKqH_9mk1waLgBiL2vT5b9g.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCcV_JGdn_Aw99JW7J2SRBzA.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UC7VWLs_Ivccq22rM2_xo0Rg` (0.917); least = `https://www.youtube.com/channel/UCKy1dAqELo0zrOtPkf0eTMw` (0.648).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).