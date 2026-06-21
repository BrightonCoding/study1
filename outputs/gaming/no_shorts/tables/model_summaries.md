# Model summaries — Study 1 (Shorts EXCLUDED)

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0621

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00145*** | 0.00026 | -5.63 | 0.000 | [-0.0019, -0.0009] |
| `log_days_since_upload` | -0.00340*** | 0.00053 | -6.47 | 0.000 | [-0.0044, -0.0024] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0704

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00187*** | 0.00028 | -6.67 | 0.000 | [-0.0024, -0.0013] |
| `log_days_since_upload` | -0.00336*** | 0.00052 | -6.41 | 0.000 | [-0.0044, -0.0023] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0736

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00201*** | 0.00029 | -7.00 | 0.000 | [-0.0026, -0.0014] |
| `log_days_since_upload` | -0.00341*** | 0.00052 | -6.52 | 0.000 | [-0.0044, -0.0024] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6358 videos/obs across 73 channels; within-R² = 0.0216

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | +0.05753 | 0.03575 | +1.61 | 0.108 | [-0.0125, +0.1276] |
| `log_days_since_upload` | +0.21194*** | 0.05009 | +4.23 | 0.000 | [+0.1137, +0.3101] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6358 videos/obs across 73 channels; within-R² = 0.0238

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.08389** | 0.03790 | +2.21 | 0.027 | [+0.0096, +0.1582] |
| `log_days_since_upload` | +0.21067*** | 0.05033 | +4.19 | 0.000 | [+0.1120, +0.3093] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6358 videos/obs across 73 channels; within-R² = 0.0235

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | +0.08076* | 0.04152 | +1.94 | 0.052 | [-0.0006, +0.1622] |
| `log_days_since_upload` | +0.21271*** | 0.04991 | +4.26 | 0.000 | [+0.1149, +0.3106] |


## 6. Wear-out: cumulative formula EXPOSURE (redesign)

Outcome = engagement_rate. Predictor = accumulated exposure to the channel's formula BEFORE the video (recency-weighted dose / window-share / streak), z-scored within channel. Channel FE; clustered SE. Wear-out => NEGATIVE coefficient.

### 6.thumbnail.dose — engagement_rate ~ dose exposure (thumbnail)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0528

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00072*** | 0.00028 | -2.63 | 0.009 | [-0.0013, -0.0002] |
| `log_days_since_upload` | -0.00335*** | 0.00052 | -6.42 | 0.000 | [-0.0044, -0.0023] |

### 6.thumbnail.winshare — engagement_rate ~ winshare exposure (thumbnail)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0531

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_thumbnail_z` | -0.00076*** | 0.00026 | -2.90 | 0.004 | [-0.0013, -0.0002] |
| `log_days_since_upload` | -0.00335*** | 0.00052 | -6.45 | 0.000 | [-0.0044, -0.0023] |

### 6.thumbnail.streak — engagement_rate ~ streak exposure (thumbnail)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0506

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_thumbnail_z` | -0.00039* | 0.00021 | -1.91 | 0.056 | [-0.0008, +0.0000] |
| `log_days_since_upload` | -0.00334*** | 0.00053 | -6.31 | 0.000 | [-0.0044, -0.0023] |

### 6.thumbnail.nonlinear — engagement_rate ~ dose + dose^2 (thumbnail)
_quadratic in cumulative dose; channel FE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0531

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00066** | 0.00027 | -2.44 | 0.015 | [-0.0012, -0.0001] |
| `dose_thumbnail_z_sq` | +0.00014 | 0.00010 | +1.44 | 0.150 | [-0.0001, +0.0003] |
| `log_days_since_upload` | -0.00336*** | 0.00052 | -6.43 | 0.000 | [-0.0044, -0.0023] |

### 6.thumbnail.rebound — engagement_rate ~ template_similarity (thumbnail)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 6350 videos/obs across 72 channels; within-R² = 0.0638

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_thumbnail_z` | -0.00155*** | 0.00026 | -5.89 | 0.000 | [-0.0021, -0.0010] |
| `log_days_since_upload` | -0.00331*** | 0.00052 | -6.35 | 0.000 | [-0.0043, -0.0023] |

### 6.title.dose — engagement_rate ~ dose exposure (title)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0558

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00101*** | 0.00026 | -3.95 | 0.000 | [-0.0015, -0.0005] |
| `log_days_since_upload` | -0.00330*** | 0.00052 | -6.32 | 0.000 | [-0.0043, -0.0023] |

### 6.title.winshare — engagement_rate ~ winshare exposure (title)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0543

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_title_z` | -0.00088*** | 0.00023 | -3.78 | 0.000 | [-0.0013, -0.0004] |
| `log_days_since_upload` | -0.00331*** | 0.00052 | -6.33 | 0.000 | [-0.0043, -0.0023] |

### 6.title.streak — engagement_rate ~ streak exposure (title)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0525

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_title_z` | -0.00069*** | 0.00021 | -3.27 | 0.001 | [-0.0011, -0.0003] |
| `log_days_since_upload` | -0.00334*** | 0.00053 | -6.33 | 0.000 | [-0.0044, -0.0023] |

### 6.title.nonlinear — engagement_rate ~ dose + dose^2 (title)
_quadratic in cumulative dose; channel FE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0558

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00104*** | 0.00028 | -3.77 | 0.000 | [-0.0016, -0.0005] |
| `dose_title_z_sq` | -0.00006 | 0.00010 | -0.61 | 0.540 | [-0.0002, +0.0001] |
| `log_days_since_upload` | -0.00330*** | 0.00053 | -6.27 | 0.000 | [-0.0043, -0.0023] |

### 6.title.rebound — engagement_rate ~ template_similarity (title)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 6350 videos/obs across 72 channels; within-R² = 0.0804

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_title_z` | -0.00228*** | 0.00032 | -7.15 | 0.000 | [-0.0029, -0.0017] |
| `log_days_since_upload` | -0.00324*** | 0.00052 | -6.23 | 0.000 | [-0.0043, -0.0022] |

### 6.combined.dose — engagement_rate ~ dose exposure (combined)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0556

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00100*** | 0.00028 | -3.55 | 0.000 | [-0.0016, -0.0004] |
| `log_days_since_upload` | -0.00333*** | 0.00052 | -6.41 | 0.000 | [-0.0044, -0.0023] |

### 6.combined.winshare — engagement_rate ~ winshare exposure (combined)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0548

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_combined_z` | -0.00093*** | 0.00026 | -3.62 | 0.000 | [-0.0014, -0.0004] |
| `log_days_since_upload` | -0.00334*** | 0.00052 | -6.43 | 0.000 | [-0.0044, -0.0023] |

### 6.combined.streak — engagement_rate ~ streak exposure (combined)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0521

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_combined_z` | -0.00063*** | 0.00022 | -2.92 | 0.004 | [-0.0011, -0.0002] |
| `log_days_since_upload` | -0.00334*** | 0.00053 | -6.34 | 0.000 | [-0.0044, -0.0023] |

### 6.combined.nonlinear — engagement_rate ~ dose + dose^2 (combined)
_quadratic in cumulative dose; channel FE_

N = 6280 videos/obs across 72 channels; within-R² = 0.0556

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00103*** | 0.00030 | -3.41 | 0.001 | [-0.0016, -0.0004] |
| `dose_combined_z_sq` | -0.00006 | 0.00010 | -0.57 | 0.569 | [-0.0003, +0.0001] |
| `log_days_since_upload` | -0.00333*** | 0.00052 | -6.38 | 0.000 | [-0.0044, -0.0023] |

### 6.combined.rebound — engagement_rate ~ template_similarity (combined)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 6350 videos/obs across 72 channels; within-R² = 0.0840

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_combined_z` | -0.00241*** | 0.00033 | -7.40 | 0.000 | [-0.0031, -0.0018] |
| `log_days_since_upload` | -0.00325*** | 0.00052 | -6.27 | 0.000 | [-0.0043, -0.0022] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 2874 videos/obs across 71 channels; within-R² = 0.0076

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | -0.00110*** | 0.00032 | -3.43 | 0.001 | [-0.0017, -0.0005] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 2874 videos/obs across 71 channels; within-R² = 0.0203

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00181*** | 0.00034 | -5.33 | 0.000 | [-0.0025, -0.0011] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 2874 videos/obs across 71 channels; within-R² = 0.0184

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00172*** | 0.00034 | -5.12 | 0.000 | [-0.0024, -0.0011] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2799 videos/obs across 66 channels; within-R² = 0.0001

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.01081 | 0.02210 | -0.49 | 0.625 | [-0.0541, +0.0325] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 2831 videos/obs across 67 channels; within-R² = 0.0022

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.04650** | 0.01994 | -2.33 | 0.020 | [-0.0856, -0.0074] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2799 videos/obs across 66 channels; within-R² = 0.0026

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.05107** | 0.02226 | -2.29 | 0.022 | [-0.0947, -0.0074] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 2831 videos/obs across 67 channels; within-R² = 0.0033

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.05721** | 0.02349 | -2.44 | 0.015 | [-0.1033, -0.0111] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2799 videos/obs across 66 channels; within-R² = 0.0014

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03729* | 0.02250 | -1.66 | 0.098 | [-0.0814, +0.0068] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 2831 videos/obs across 67 channels; within-R² = 0.0036

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.06001*** | 0.02230 | -2.69 | 0.007 | [-0.1037, -0.0163] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 22 channels meet 'strong start + later homogenized'.

### 4.thumbnail — engagement_rate ~ formula_adherence (subsample)
_same spec as Model 1, restricted sample_

N = 2064 videos/obs across 22 channels; within-R² = 0.0354

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00141*** | 0.00052 | -2.71 | 0.007 | [-0.0024, -0.0004] |
| `log_days_since_upload` | -0.00278*** | 0.00092 | -3.01 | 0.003 | [-0.0046, -0.0010] |


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0815; median = 0.0765; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.342 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UC7_YxT-KID8kRbqZo7MyscQ.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCKqH_9mk1waLgBiL2vT5b9g.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCcV_JGdn_Aw99JW7J2SRBzA.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UC7VWLs_Ivccq22rM2_xo0Rg` (0.917); least = `https://www.youtube.com/channel/UCKy1dAqELo0zrOtPkf0eTMw` (0.648).
