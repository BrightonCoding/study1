# Model summaries — Study 1 (Shorts EXCLUDED)

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0049

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00003 | 0.00026 | -0.12 | 0.903 | [-0.0005, +0.0005] |
| `log_days_since_upload` | -0.00243*** | 0.00058 | -4.17 | 0.000 | [-0.0036, -0.0013] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 20672 videos/obs across 238 channels; within-R² = 0.0054

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00069*** | 0.00021 | -3.21 | 0.001 | [-0.0011, -0.0003] |
| `log_days_since_upload` | -0.00246*** | 0.00057 | -4.31 | 0.000 | [-0.0036, -0.0013] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0052

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00051** | 0.00020 | -2.55 | 0.011 | [-0.0009, -0.0001] |
| `log_days_since_upload` | -0.00246*** | 0.00058 | -4.27 | 0.000 | [-0.0036, -0.0013] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 21041 videos/obs across 238 channels; within-R² = 0.0329

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.01539 | 0.01659 | -0.93 | 0.354 | [-0.0479, +0.0171] |
| `log_days_since_upload` | +0.24174*** | 0.02675 | +9.04 | 0.000 | [+0.1893, +0.2942] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 21042 videos/obs across 238 channels; within-R² = 0.0361

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.06951*** | 0.01613 | +4.31 | 0.000 | [+0.0379, +0.1011] |
| `log_days_since_upload` | +0.24603*** | 0.02648 | +9.29 | 0.000 | [+0.1941, +0.2979] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 21041 videos/obs across 238 channels; within-R² = 0.0336

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | +0.03639** | 0.01635 | +2.23 | 0.026 | [+0.0043, +0.0684] |
| `log_days_since_upload` | +0.24534*** | 0.02666 | +9.20 | 0.000 | [+0.1931, +0.2976] |


## 6. Wear-out: cumulative formula EXPOSURE (redesign)

Outcome = engagement_rate. Predictor = accumulated exposure to the channel's formula BEFORE the video (recency-weighted dose / window-share / streak), z-scored within channel. Channel FE; clustered SE. Wear-out => NEGATIVE coefficient.

### 6.thumbnail.dose — engagement_rate ~ dose exposure (thumbnail)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0051

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | +0.00041 | 0.00033 | +1.24 | 0.214 | [-0.0002, +0.0011] |
| `log_days_since_upload` | -0.00241*** | 0.00057 | -4.19 | 0.000 | [-0.0035, -0.0013] |

### 6.thumbnail.winshare — engagement_rate ~ winshare exposure (thumbnail)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0051

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_thumbnail_z` | +0.00041 | 0.00034 | +1.21 | 0.227 | [-0.0003, +0.0011] |
| `log_days_since_upload` | -0.00241*** | 0.00057 | -4.19 | 0.000 | [-0.0035, -0.0013] |

### 6.thumbnail.streak — engagement_rate ~ streak exposure (thumbnail)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0049

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_thumbnail_z` | +0.00004 | 0.00018 | +0.23 | 0.820 | [-0.0003, +0.0004] |
| `log_days_since_upload` | -0.00242*** | 0.00057 | -4.22 | 0.000 | [-0.0035, -0.0013] |

### 6.thumbnail.nonlinear — engagement_rate ~ dose + dose^2 (thumbnail)
_quadratic in cumulative dose; channel FE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0051

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | +0.00044 | 0.00034 | +1.29 | 0.196 | [-0.0002, +0.0011] |
| `dose_thumbnail_z_sq` | +0.00008 | 0.00012 | +0.62 | 0.534 | [-0.0002, +0.0003] |
| `log_days_since_upload` | -0.00242*** | 0.00058 | -4.20 | 0.000 | [-0.0035, -0.0013] |

### 6.thumbnail.rebound — engagement_rate ~ template_similarity (thumbnail)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 20904 videos/obs across 238 channels; within-R² = 0.0049

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_thumbnail_z` | -0.00035 | 0.00031 | -1.13 | 0.257 | [-0.0010, +0.0003] |
| `log_days_since_upload` | -0.00240*** | 0.00058 | -4.13 | 0.000 | [-0.0035, -0.0013] |

### 6.title.dose — engagement_rate ~ dose exposure (title)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 20672 videos/obs across 238 channels; within-R² = 0.0050

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | +0.00033 | 0.00036 | +0.91 | 0.362 | [-0.0004, +0.0010] |
| `log_days_since_upload` | -0.00242*** | 0.00057 | -4.23 | 0.000 | [-0.0035, -0.0013] |

### 6.title.winshare — engagement_rate ~ winshare exposure (title)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 20672 videos/obs across 238 channels; within-R² = 0.0051

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_title_z` | +0.00041 | 0.00044 | +0.93 | 0.353 | [-0.0005, +0.0013] |
| `log_days_since_upload` | -0.00242*** | 0.00057 | -4.23 | 0.000 | [-0.0035, -0.0013] |

### 6.title.streak — engagement_rate ~ streak exposure (title)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 20672 videos/obs across 238 channels; within-R² = 0.0051

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_title_z` | +0.00037 | 0.00028 | +1.32 | 0.187 | [-0.0002, +0.0009] |
| `log_days_since_upload` | -0.00242*** | 0.00057 | -4.23 | 0.000 | [-0.0035, -0.0013] |

### 6.title.nonlinear — engagement_rate ~ dose + dose^2 (title)
_quadratic in cumulative dose; channel FE_

N = 20672 videos/obs across 238 channels; within-R² = 0.0050

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | +0.00032 | 0.00037 | +0.88 | 0.377 | [-0.0004, +0.0010] |
| `dose_title_z_sq` | -0.00003 | 0.00009 | -0.30 | 0.766 | [-0.0002, +0.0002] |
| `log_days_since_upload` | -0.00242*** | 0.00057 | -4.22 | 0.000 | [-0.0035, -0.0013] |

### 6.title.rebound — engagement_rate ~ template_similarity (title)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 20904 videos/obs across 238 channels; within-R² = 0.0057

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_title_z` | -0.00094*** | 0.00028 | -3.39 | 0.001 | [-0.0015, -0.0004] |
| `log_days_since_upload` | -0.00239*** | 0.00058 | -4.13 | 0.000 | [-0.0035, -0.0013] |

### 6.combined.dose — engagement_rate ~ dose exposure (combined)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0053

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | +0.00062* | 0.00037 | +1.70 | 0.089 | [-0.0001, +0.0013] |
| `log_days_since_upload` | -0.00241*** | 0.00057 | -4.20 | 0.000 | [-0.0035, -0.0013] |

### 6.combined.winshare — engagement_rate ~ winshare exposure (combined)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0054

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_combined_z` | +0.00069* | 0.00042 | +1.65 | 0.099 | [-0.0001, +0.0015] |
| `log_days_since_upload` | -0.00240*** | 0.00057 | -4.20 | 0.000 | [-0.0035, -0.0013] |

### 6.combined.streak — engagement_rate ~ streak exposure (combined)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0049

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_combined_z` | +0.00007 | 0.00019 | +0.35 | 0.726 | [-0.0003, +0.0004] |
| `log_days_since_upload` | -0.00242*** | 0.00057 | -4.22 | 0.000 | [-0.0035, -0.0013] |

### 6.combined.nonlinear — engagement_rate ~ dose + dose^2 (combined)
_quadratic in cumulative dose; channel FE_

N = 20671 videos/obs across 238 channels; within-R² = 0.0053

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | +0.00063* | 0.00037 | +1.70 | 0.089 | [-0.0001, +0.0014] |
| `dose_combined_z_sq` | +0.00002 | 0.00012 | +0.16 | 0.872 | [-0.0002, +0.0002] |
| `log_days_since_upload` | -0.00241*** | 0.00057 | -4.21 | 0.000 | [-0.0035, -0.0013] |

### 6.combined.rebound — engagement_rate ~ template_similarity (combined)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 20904 videos/obs across 238 channels; within-R² = 0.0055

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_combined_z` | -0.00087*** | 0.00032 | -2.76 | 0.006 | [-0.0015, -0.0003] |
| `log_days_since_upload` | -0.00239*** | 0.00058 | -4.13 | 0.000 | [-0.0035, -0.0013] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 10648 videos/obs across 234 channels; within-R² = 0.0002

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | +0.00040 | 0.00037 | +1.11 | 0.268 | [-0.0003, +0.0011] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 10648 videos/obs across 234 channels; within-R² = 0.0007

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00071* | 0.00042 | -1.67 | 0.096 | [-0.0015, +0.0001] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 10648 videos/obs across 234 channels; within-R² = 0.0001

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00031 | 0.00040 | -0.78 | 0.436 | [-0.0011, +0.0005] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 10416 videos/obs across 234 channels; within-R² = 0.0001

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | +0.01177 | 0.01133 | +1.04 | 0.299 | [-0.0104, +0.0340] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 10528 videos/obs across 234 channels; within-R² = 0.0003

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.01778 | 0.01243 | +1.43 | 0.153 | [-0.0066, +0.0421] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 10416 videos/obs across 234 channels; within-R² = 0.0000

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.00089 | 0.01193 | -0.07 | 0.940 | [-0.0243, +0.0225] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 10528 videos/obs across 234 channels; within-R² = 0.0000

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.00201 | 0.01137 | +0.18 | 0.860 | [-0.0203, +0.0243] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 10416 videos/obs across 234 channels; within-R² = 0.0001

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | +0.00718 | 0.01135 | +0.63 | 0.527 | [-0.0151, +0.0294] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 10528 videos/obs across 234 channels; within-R² = 0.0001

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.01077 | 0.01217 | +0.88 | 0.376 | [-0.0131, +0.0346] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 77 channels meet 'strong start + later homogenized'.

### 4.thumbnail — engagement_rate ~ formula_adherence (subsample)
_same spec as Model 1, restricted sample_

N = 6818 videos/obs across 77 channels; within-R² = 0.0023

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | +0.00031 | 0.00062 | +0.49 | 0.622 | [-0.0009, +0.0015] |
| `log_days_since_upload` | -0.00239 | 0.00155 | -1.54 | 0.123 | [-0.0054, +0.0007] |


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0838; median = 0.0798; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.246 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_Erika2.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UC9vUu4vlIlMC0dHQCTvQPbg.png`, `sanity_thumbnail_GrahamStephan.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UC9JYZbC-3QoAQVo6GHjKznw` (0.999); least = `https://www.youtube.com/channel/UCvJJ_dzjViJCoLf5uKUTwoA` (0.565).
