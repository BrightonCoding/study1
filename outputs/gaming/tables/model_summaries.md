# Model summaries — Study 1

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0451

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00096*** | 0.00026 | -3.64 | 0.000 | [-0.0015, -0.0004] |
| `log_days_since_upload` | -0.00312*** | 0.00046 | -6.82 | 0.000 | [-0.0040, -0.0022] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0518

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00145*** | 0.00028 | -5.17 | 0.000 | [-0.0020, -0.0009] |
| `log_days_since_upload` | -0.00313*** | 0.00046 | -6.84 | 0.000 | [-0.0040, -0.0022] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0528

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00150*** | 0.00029 | -5.19 | 0.000 | [-0.0021, -0.0009] |
| `log_days_since_upload` | -0.00316*** | 0.00046 | -6.91 | 0.000 | [-0.0041, -0.0023] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8239 videos/obs across 75 channels; within-R² = 0.0213

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | +0.02569 | 0.03621 | +0.71 | 0.478 | [-0.0453, +0.0967] |
| `log_days_since_upload` | +0.22678*** | 0.05474 | +4.14 | 0.000 | [+0.1195, +0.3341] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8239 videos/obs across 75 channels; within-R² = 0.0254

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.08798** | 0.03754 | +2.34 | 0.019 | [+0.0144, +0.1616] |
| `log_days_since_upload` | +0.22883*** | 0.05511 | +4.15 | 0.000 | [+0.1208, +0.3369] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8239 videos/obs across 75 channels; within-R² = 0.0235

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | +0.06674 | 0.04149 | +1.61 | 0.108 | [-0.0146, +0.1481] |
| `log_days_since_upload` | +0.22907*** | 0.05464 | +4.19 | 0.000 | [+0.1220, +0.3362] |


## 6. Wear-out: cumulative formula EXPOSURE (redesign)

Outcome = engagement_rate. Predictor = accumulated exposure to the channel's formula BEFORE the video (recency-weighted dose / window-share / streak), z-scored within channel. Channel FE; clustered SE. Wear-out => NEGATIVE coefficient.

### 6.thumbnail.dose — engagement_rate ~ dose exposure (thumbnail)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0409

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00047* | 0.00025 | -1.88 | 0.060 | [-0.0010, +0.0000] |
| `log_days_since_upload` | -0.00307*** | 0.00046 | -6.70 | 0.000 | [-0.0040, -0.0022] |

### 6.thumbnail.winshare — engagement_rate ~ winshare exposure (thumbnail)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0413

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_thumbnail_z` | -0.00053** | 0.00023 | -2.33 | 0.020 | [-0.0010, -0.0001] |
| `log_days_since_upload` | -0.00307*** | 0.00046 | -6.72 | 0.000 | [-0.0040, -0.0022] |

### 6.thumbnail.streak — engagement_rate ~ streak exposure (thumbnail)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0399

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_thumbnail_z` | -0.00020 | 0.00019 | -1.06 | 0.291 | [-0.0006, +0.0002] |
| `log_days_since_upload` | -0.00308*** | 0.00046 | -6.68 | 0.000 | [-0.0040, -0.0022] |

### 6.thumbnail.nonlinear — engagement_rate ~ dose + dose^2 (thumbnail)
_quadratic in cumulative dose; channel FE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0412

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00040 | 0.00025 | -1.60 | 0.111 | [-0.0009, +0.0001] |
| `dose_thumbnail_z_sq` | +0.00013 | 0.00010 | +1.29 | 0.198 | [-0.0001, +0.0003] |
| `log_days_since_upload` | -0.00307*** | 0.00046 | -6.70 | 0.000 | [-0.0040, -0.0022] |

### 6.thumbnail.rebound — engagement_rate ~ template_similarity (thumbnail)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8159 videos/obs across 74 channels; within-R² = 0.0465

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_thumbnail_z` | -0.00108*** | 0.00027 | -3.99 | 0.000 | [-0.0016, -0.0006] |
| `log_days_since_upload` | -0.00304*** | 0.00046 | -6.66 | 0.000 | [-0.0039, -0.0021] |

### 6.title.dose — engagement_rate ~ dose exposure (title)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0431

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00077*** | 0.00026 | -3.02 | 0.003 | [-0.0013, -0.0003] |
| `log_days_since_upload` | -0.00308*** | 0.00046 | -6.73 | 0.000 | [-0.0040, -0.0022] |

### 6.title.winshare — engagement_rate ~ winshare exposure (title)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0422

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_title_z` | -0.00066*** | 0.00024 | -2.69 | 0.007 | [-0.0011, -0.0002] |
| `log_days_since_upload` | -0.00308*** | 0.00046 | -6.73 | 0.000 | [-0.0040, -0.0022] |

### 6.title.streak — engagement_rate ~ streak exposure (title)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0409

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_title_z` | -0.00046** | 0.00019 | -2.50 | 0.013 | [-0.0008, -0.0001] |
| `log_days_since_upload` | -0.00309*** | 0.00046 | -6.71 | 0.000 | [-0.0040, -0.0022] |

### 6.title.nonlinear — engagement_rate ~ dose + dose^2 (title)
_quadratic in cumulative dose; channel FE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0431

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00079*** | 0.00027 | -2.94 | 0.003 | [-0.0013, -0.0003] |
| `dose_title_z_sq` | -0.00004 | 0.00010 | -0.42 | 0.676 | [-0.0002, +0.0001] |
| `log_days_since_upload` | -0.00308*** | 0.00046 | -6.71 | 0.000 | [-0.0040, -0.0022] |

### 6.title.rebound — engagement_rate ~ template_similarity (title)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8159 videos/obs across 74 channels; within-R² = 0.0610

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_title_z` | -0.00192*** | 0.00031 | -6.19 | 0.000 | [-0.0025, -0.0013] |
| `log_days_since_upload` | -0.00303*** | 0.00046 | -6.64 | 0.000 | [-0.0039, -0.0021] |

### 6.combined.dose — engagement_rate ~ dose exposure (combined)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0428

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00073*** | 0.00027 | -2.71 | 0.007 | [-0.0013, -0.0002] |
| `log_days_since_upload` | -0.00305*** | 0.00046 | -6.70 | 0.000 | [-0.0039, -0.0022] |

### 6.combined.winshare — engagement_rate ~ winshare exposure (combined)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0424

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_combined_z` | -0.00069*** | 0.00025 | -2.71 | 0.007 | [-0.0012, -0.0002] |
| `log_days_since_upload` | -0.00306*** | 0.00046 | -6.70 | 0.000 | [-0.0040, -0.0022] |

### 6.combined.streak — engagement_rate ~ streak exposure (combined)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0409

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_combined_z` | -0.00046** | 0.00019 | -2.45 | 0.014 | [-0.0008, -0.0001] |
| `log_days_since_upload` | -0.00308*** | 0.00046 | -6.72 | 0.000 | [-0.0040, -0.0022] |

### 6.combined.nonlinear — engagement_rate ~ dose + dose^2 (combined)
_quadratic in cumulative dose; channel FE_

N = 8089 videos/obs across 74 channels; within-R² = 0.0428

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00076*** | 0.00029 | -2.67 | 0.008 | [-0.0013, -0.0002] |
| `dose_combined_z_sq` | -0.00005 | 0.00012 | -0.44 | 0.661 | [-0.0003, +0.0002] |
| `log_days_since_upload` | -0.00305*** | 0.00046 | -6.68 | 0.000 | [-0.0039, -0.0022] |

### 6.combined.rebound — engagement_rate ~ template_similarity (combined)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8159 videos/obs across 74 channels; within-R² = 0.0617

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_combined_z` | -0.00195*** | 0.00031 | -6.36 | 0.000 | [-0.0025, -0.0013] |
| `log_days_since_upload` | -0.00299*** | 0.00045 | -6.59 | 0.000 | [-0.0039, -0.0021] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3090 videos/obs across 71 channels; within-R² = 0.0045

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | -0.00088*** | 0.00032 | -2.78 | 0.005 | [-0.0015, -0.0003] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3090 videos/obs across 71 channels; within-R² = 0.0186

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00180*** | 0.00035 | -5.13 | 0.000 | [-0.0025, -0.0011] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3090 videos/obs across 71 channels; within-R² = 0.0152

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00163*** | 0.00033 | -4.92 | 0.000 | [-0.0023, -0.0010] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3015 videos/obs across 66 channels; within-R² = 0.0000

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.00488 | 0.02064 | -0.24 | 0.813 | [-0.0454, +0.0356] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3040 videos/obs across 67 channels; within-R² = 0.0012

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.03422 | 0.02140 | -1.60 | 0.110 | [-0.0762, +0.0077] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3015 videos/obs across 66 channels; within-R² = 0.0019

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.04367** | 0.02025 | -2.16 | 0.031 | [-0.0834, -0.0040] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3040 videos/obs across 67 channels; within-R² = 0.0008

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.02771 | 0.02209 | -1.25 | 0.210 | [-0.0710, +0.0156] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3015 videos/obs across 66 channels; within-R² = 0.0009

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03034 | 0.01977 | -1.53 | 0.125 | [-0.0691, +0.0084] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3040 videos/obs across 67 channels; within-R² = 0.0013

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.03535* | 0.02102 | -1.68 | 0.093 | [-0.0766, +0.0059] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 26 channels meet 'strong start + later homogenized'.

### 4.thumbnail — engagement_rate ~ formula_adherence (subsample)
_same spec as Model 1, restricted sample_

N = 2850 videos/obs across 26 channels; within-R² = 0.0257

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00086 | 0.00058 | -1.48 | 0.138 | [-0.0020, +0.0003] |
| `log_days_since_upload` | -0.00267*** | 0.00079 | -3.37 | 0.001 | [-0.0042, -0.0011] |


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0794; median = 0.0770; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.323 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UC7_YxT-KID8kRbqZo7MyscQ.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCKqH_9mk1waLgBiL2vT5b9g.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCcV_JGdn_Aw99JW7J2SRBzA.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCupOeAF8co65kZ-N6zoVxmw` (0.907); least = `https://www.youtube.com/channel/UC--i2rV5NCxiEIPefr3l-zQ` (0.646).
