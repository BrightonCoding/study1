# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 75 channels, 8314 videos (personal-finance/investing niche; snapshot taken 2026-06-21).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00096** change in engagement_rate (SE 0.00026, p=0.000) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **statistically significant (p<0.05)**.

H1 predicts a NEGATIVE coefficient. **Consistent with H1.**

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00096 | 0.00026 | 0.000 | 8089 | 74 |
| core_title | engagement_rate | -0.00145 | 0.00028 | 0.000 | 8089 | 74 |
| core_combined | engagement_rate | -0.00150 | 0.00029 | 0.000 | 8089 | 74 |
| core_thumbnail_logviews | log_views | +0.02569 | 0.03621 | 0.478 | 8239 | 75 |
| core_title_logviews | log_views | +0.08798 | 0.03754 | 0.019 | 8239 | 75 |
| core_combined_logviews | log_views | +0.06674 | 0.04149 | 0.108 | 8239 | 75 |
| wearout_thumbnail_dose | engagement_rate | -0.00047 | 0.00025 | 0.060 | 8089 | 74 |
| wearout_thumbnail_winshare | engagement_rate | -0.00053 | 0.00023 | 0.020 | 8089 | 74 |
| wearout_thumbnail_streak | engagement_rate | -0.00020 | 0.00019 | 0.291 | 8089 | 74 |
| wearout_thumbnail_nonlin_lin | engagement_rate | -0.00040 | 0.00025 | 0.111 | 8089 | 74 |
| wearout_thumbnail_nonlin_sq | engagement_rate | +0.00013 | 0.00010 | 0.198 | 8089 | 74 |
| wearout_thumbnail_rebound | engagement_rate | -0.00108 | 0.00027 | 0.000 | 8159 | 74 |
| wearout_title_dose | engagement_rate | -0.00077 | 0.00026 | 0.003 | 8089 | 74 |
| wearout_title_winshare | engagement_rate | -0.00066 | 0.00024 | 0.007 | 8089 | 74 |
| wearout_title_streak | engagement_rate | -0.00046 | 0.00019 | 0.013 | 8089 | 74 |
| wearout_title_nonlin_lin | engagement_rate | -0.00079 | 0.00027 | 0.003 | 8089 | 74 |
| wearout_title_nonlin_sq | engagement_rate | -0.00004 | 0.00010 | 0.676 | 8089 | 74 |
| wearout_title_rebound | engagement_rate | -0.00192 | 0.00031 | 0.000 | 8159 | 74 |
| wearout_combined_dose | engagement_rate | -0.00073 | 0.00027 | 0.007 | 8089 | 74 |
| wearout_combined_winshare | engagement_rate | -0.00069 | 0.00025 | 0.007 | 8089 | 74 |
| wearout_combined_streak | engagement_rate | -0.00046 | 0.00019 | 0.014 | 8089 | 74 |
| wearout_combined_nonlin_lin | engagement_rate | -0.00076 | 0.00029 | 0.008 | 8089 | 74 |
| wearout_combined_nonlin_sq | engagement_rate | -0.00005 | 0.00012 | 0.661 | 8089 | 74 |
| wearout_combined_rebound | engagement_rate | -0.00195 | 0.00031 | 0.000 | 8159 | 74 |
| week_thumbnail | engagement_rate | -0.00088 | 0.00032 | 0.005 | 3090 | 71 |
| week_title | engagement_rate | -0.00180 | 0.00035 | 0.000 | 3090 | 71 |
| week_combined | engagement_rate | -0.00163 | 0.00033 | 0.000 | 3090 | 71 |
| direction_thumbnail_forward | engagement | -0.00488 | 0.02064 | 0.813 | 3015 | 66 |
| direction_thumbnail_reverse | homogeneity | -0.03422 | 0.02140 | 0.110 | 3040 | 67 |
| direction_title_forward | engagement | -0.04367 | 0.02025 | 0.031 | 3015 | 66 |
| direction_title_reverse | homogeneity | -0.02771 | 0.02209 | 0.210 | 3040 | 67 |
| direction_combined_forward | engagement | -0.03034 | 0.01977 | 0.125 | 3015 | 66 |
| direction_combined_reverse | homogeneity | -0.03535 | 0.02102 | 0.093 | 3040 | 67 |
| robust_thumbnail | engagement_rate | -0.00086 | 0.00058 | 0.138 | 2850 | 26 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef -0.0049 (p=0.813). Reverse (homogeneity_t ~ engagement_(t-1)): coef -0.0342 (p=0.110). Reverse is comparable/stronger — cannot rule out that declining engagement drives homogenization (the main reverse-causation threat).

## Robustness subsample (strong-start, then homogenized)
Coef -0.00086 (p=0.138, N=2850). H1 does not clearly survive here.

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0794; median = 0.0770; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.323 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UC7_YxT-KID8kRbqZo7MyscQ.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCKqH_9mk1waLgBiL2vT5b9g.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCcV_JGdn_Aw99JW7J2SRBzA.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCupOeAF8co65kZ-N6zoVxmw` (0.907); least = `https://www.youtube.com/channel/UC--i2rV5NCxiEIPefr3l-zQ` (0.646).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).