# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 238 channels, 21280 videos (personal-finance/investing niche; snapshot taken 2026-06-21).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00003** change in engagement_rate (SE 0.00026, p=0.903) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **not statistically significant (p≥0.05)**.

H1 predicts a NEGATIVE coefficient. **Not clearly supported** at conventional significance — reported honestly.

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00003 | 0.00026 | 0.903 | 20671 | 238 |
| core_title | engagement_rate | -0.00069 | 0.00021 | 0.001 | 20672 | 238 |
| core_combined | engagement_rate | -0.00051 | 0.00020 | 0.011 | 20671 | 238 |
| core_thumbnail_logviews | log_views | -0.01539 | 0.01659 | 0.354 | 21041 | 238 |
| core_title_logviews | log_views | +0.06951 | 0.01613 | 0.000 | 21042 | 238 |
| core_combined_logviews | log_views | +0.03639 | 0.01635 | 0.026 | 21041 | 238 |
| wearout_thumbnail_dose | engagement_rate | +0.00041 | 0.00033 | 0.214 | 20671 | 238 |
| wearout_thumbnail_winshare | engagement_rate | +0.00041 | 0.00034 | 0.227 | 20671 | 238 |
| wearout_thumbnail_streak | engagement_rate | +0.00004 | 0.00018 | 0.820 | 20671 | 238 |
| wearout_thumbnail_nonlin_lin | engagement_rate | +0.00044 | 0.00034 | 0.196 | 20671 | 238 |
| wearout_thumbnail_nonlin_sq | engagement_rate | +0.00008 | 0.00012 | 0.534 | 20671 | 238 |
| wearout_thumbnail_rebound | engagement_rate | -0.00035 | 0.00031 | 0.257 | 20904 | 238 |
| wearout_title_dose | engagement_rate | +0.00033 | 0.00036 | 0.362 | 20672 | 238 |
| wearout_title_winshare | engagement_rate | +0.00041 | 0.00044 | 0.353 | 20672 | 238 |
| wearout_title_streak | engagement_rate | +0.00037 | 0.00028 | 0.187 | 20672 | 238 |
| wearout_title_nonlin_lin | engagement_rate | +0.00032 | 0.00037 | 0.377 | 20672 | 238 |
| wearout_title_nonlin_sq | engagement_rate | -0.00003 | 0.00009 | 0.766 | 20672 | 238 |
| wearout_title_rebound | engagement_rate | -0.00094 | 0.00028 | 0.001 | 20904 | 238 |
| wearout_combined_dose | engagement_rate | +0.00062 | 0.00037 | 0.089 | 20671 | 238 |
| wearout_combined_winshare | engagement_rate | +0.00069 | 0.00042 | 0.099 | 20671 | 238 |
| wearout_combined_streak | engagement_rate | +0.00007 | 0.00019 | 0.726 | 20671 | 238 |
| wearout_combined_nonlin_lin | engagement_rate | +0.00063 | 0.00037 | 0.089 | 20671 | 238 |
| wearout_combined_nonlin_sq | engagement_rate | +0.00002 | 0.00012 | 0.872 | 20671 | 238 |
| wearout_combined_rebound | engagement_rate | -0.00087 | 0.00032 | 0.006 | 20904 | 238 |
| week_thumbnail | engagement_rate | +0.00040 | 0.00037 | 0.268 | 10648 | 234 |
| week_title | engagement_rate | -0.00071 | 0.00042 | 0.096 | 10648 | 234 |
| week_combined | engagement_rate | -0.00031 | 0.00040 | 0.436 | 10648 | 234 |
| direction_thumbnail_forward | engagement | +0.01177 | 0.01133 | 0.299 | 10416 | 234 |
| direction_thumbnail_reverse | homogeneity | +0.01778 | 0.01243 | 0.153 | 10528 | 234 |
| direction_title_forward | engagement | -0.00089 | 0.01193 | 0.940 | 10416 | 234 |
| direction_title_reverse | homogeneity | +0.00201 | 0.01137 | 0.860 | 10528 | 234 |
| direction_combined_forward | engagement | +0.00718 | 0.01135 | 0.527 | 10416 | 234 |
| direction_combined_reverse | homogeneity | +0.01077 | 0.01217 | 0.376 | 10528 | 234 |
| robust_thumbnail | engagement_rate | +0.00031 | 0.00062 | 0.622 | 6818 | 77 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef +0.0118 (p=0.299). Reverse (homogeneity_t ~ engagement_(t-1)): coef +0.0178 (p=0.153). Reverse is comparable/stronger — cannot rule out that declining engagement drives homogenization (the main reverse-causation threat).

## Robustness subsample (strong-start, then homogenized)
Coef +0.00031 (p=0.622, N=6818). H1 does not clearly survive here.

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0838; median = 0.0798; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.246 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_Erika2.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UC9vUu4vlIlMC0dHQCTvQPbg.png`, `sanity_thumbnail_GrahamStephan.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UC9JYZbC-3QoAQVo6GHjKznw` (0.999); least = `https://www.youtube.com/channel/UCvJJ_dzjViJCoLf5uKUTwoA` (0.565).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).