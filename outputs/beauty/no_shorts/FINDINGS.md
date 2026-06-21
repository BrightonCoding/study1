# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 75 channels, 5108 videos (personal-finance/investing niche; snapshot taken 2026-06-21).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00141** change in engagement_rate (SE 0.00070, p=0.044) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **statistically significant (p<0.05)**.

H1 predicts a NEGATIVE coefficient. **Consistent with H1.**

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00141 | 0.00070 | 0.044 | 4924 | 74 |
| core_title | engagement_rate | -0.00220 | 0.00075 | 0.004 | 4924 | 74 |
| core_combined | engagement_rate | -0.00229 | 0.00079 | 0.004 | 4924 | 74 |
| core_thumbnail_logviews | log_views | +0.11521 | 0.02467 | 0.000 | 5033 | 75 |
| core_title_logviews | log_views | +0.08957 | 0.02958 | 0.002 | 5033 | 75 |
| core_combined_logviews | log_views | +0.11870 | 0.02856 | 0.000 | 5033 | 75 |
| wearout_thumbnail_dose | engagement_rate | -0.00031 | 0.00059 | 0.600 | 4924 | 74 |
| wearout_thumbnail_winshare | engagement_rate | -0.00034 | 0.00065 | 0.606 | 4924 | 74 |
| wearout_thumbnail_streak | engagement_rate | -0.00010 | 0.00030 | 0.740 | 4924 | 74 |
| wearout_thumbnail_nonlin_lin | engagement_rate | -0.00021 | 0.00054 | 0.699 | 4924 | 74 |
| wearout_thumbnail_nonlin_sq | engagement_rate | +0.00021 | 0.00024 | 0.374 | 4924 | 74 |
| wearout_thumbnail_rebound | engagement_rate | -0.00119 | 0.00071 | 0.093 | 4996 | 74 |
| wearout_title_dose | engagement_rate | -0.00072 | 0.00060 | 0.234 | 4924 | 74 |
| wearout_title_winshare | engagement_rate | -0.00062 | 0.00058 | 0.287 | 4924 | 74 |
| wearout_title_streak | engagement_rate | -0.00010 | 0.00042 | 0.815 | 4924 | 74 |
| wearout_title_nonlin_lin | engagement_rate | -0.00067 | 0.00055 | 0.226 | 4924 | 74 |
| wearout_title_nonlin_sq | engagement_rate | +0.00011 | 0.00025 | 0.660 | 4924 | 74 |
| wearout_title_rebound | engagement_rate | -0.00242 | 0.00083 | 0.004 | 4996 | 74 |
| wearout_combined_dose | engagement_rate | -0.00061 | 0.00064 | 0.342 | 4924 | 74 |
| wearout_combined_winshare | engagement_rate | -0.00055 | 0.00065 | 0.398 | 4924 | 74 |
| wearout_combined_streak | engagement_rate | -0.00035 | 0.00039 | 0.366 | 4924 | 74 |
| wearout_combined_nonlin_lin | engagement_rate | -0.00053 | 0.00059 | 0.374 | 4924 | 74 |
| wearout_combined_nonlin_sq | engagement_rate | +0.00020 | 0.00024 | 0.402 | 4924 | 74 |
| wearout_combined_rebound | engagement_rate | -0.00247 | 0.00087 | 0.004 | 4996 | 74 |
| week_thumbnail | engagement_rate | -0.00151 | 0.00055 | 0.007 | 3045 | 76 |
| week_title | engagement_rate | -0.00251 | 0.00068 | 0.000 | 3045 | 76 |
| week_combined | engagement_rate | -0.00244 | 0.00065 | 0.000 | 3045 | 76 |
| direction_thumbnail_forward | engagement | +0.00008 | 0.02000 | 0.997 | 2968 | 75 |
| direction_thumbnail_reverse | homogeneity | -0.04399 | 0.02197 | 0.045 | 3019 | 76 |
| direction_title_forward | engagement | -0.02118 | 0.02144 | 0.323 | 2968 | 75 |
| direction_title_reverse | homogeneity | -0.03962 | 0.02400 | 0.099 | 3019 | 76 |
| direction_combined_forward | engagement | -0.01689 | 0.02328 | 0.468 | 2968 | 75 |
| direction_combined_reverse | homogeneity | -0.04750 | 0.02400 | 0.048 | 3019 | 76 |
| robust_thumbnail | engagement_rate | -0.00107 | 0.00121 | 0.379 | 1813 | 26 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef +0.0001 (p=0.997). Reverse (homogeneity_t ~ engagement_(t-1)): coef -0.0440 (p=0.045). Reverse is comparable/stronger — cannot rule out that declining engagement drives homogenization (the main reverse-causation threat).

## Robustness subsample (strong-start, then homogenized)
Coef -0.00107 (p=0.379, N=1813). H1 does not clearly survive here.

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0775; median = 0.0767; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.323 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UCzTKskwIc_-a0cGvCXA848Q.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCucot-Zp428OwkyRm2I7v2Q.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UC4qk9TtGhBKCkoWz5qGJcGg.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCrfr4PnqvdJO4KrYWg10CJw` (0.915); least = `https://www.youtube.com/channel/UCwv-GM0CxoTghE8t0Bin9mg` (0.628).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).