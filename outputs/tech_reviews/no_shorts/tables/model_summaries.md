# Model summaries — Study 1 (Shorts EXCLUDED)

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0414

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00196*** | 0.00063 | -3.13 | 0.002 | [-0.0032, -0.0007] |
| `log_days_since_upload` | -0.00289*** | 0.00047 | -6.16 | 0.000 | [-0.0038, -0.0020] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0368

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00165*** | 0.00046 | -3.55 | 0.000 | [-0.0026, -0.0007] |
| `log_days_since_upload` | -0.00281*** | 0.00045 | -6.29 | 0.000 | [-0.0037, -0.0019] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0440

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00211*** | 0.00060 | -3.51 | 0.000 | [-0.0033, -0.0009] |
| `log_days_since_upload` | -0.00286*** | 0.00046 | -6.27 | 0.000 | [-0.0038, -0.0020] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6539 videos/obs across 72 channels; within-R² = 0.0504

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | +0.08446*** | 0.02373 | +3.56 | 0.000 | [+0.0379, +0.1310] |
| `log_days_since_upload` | +0.27181*** | 0.02993 | +9.08 | 0.000 | [+0.2131, +0.3305] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6539 videos/obs across 72 channels; within-R² = 0.0665

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.16530*** | 0.02274 | +7.27 | 0.000 | [+0.1207, +0.2099] |
| `log_days_since_upload` | +0.26735*** | 0.02932 | +9.12 | 0.000 | [+0.2099, +0.3248] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 6539 videos/obs across 72 channels; within-R² = 0.0638

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | +0.15467*** | 0.02335 | +6.62 | 0.000 | [+0.1089, +0.2004] |
| `log_days_since_upload` | +0.27170*** | 0.02973 | +9.14 | 0.000 | [+0.2134, +0.3300] |


## 6. Wear-out: cumulative formula EXPOSURE (redesign)

Outcome = engagement_rate. Predictor = accumulated exposure to the channel's formula BEFORE the video (recency-weighted dose / window-share / streak), z-scored within channel. Channel FE; clustered SE. Wear-out => NEGATIVE coefficient.

### 6.thumbnail.dose — engagement_rate ~ dose exposure (thumbnail)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0261

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00035 | 0.00026 | -1.33 | 0.185 | [-0.0009, +0.0002] |
| `log_days_since_upload` | -0.00281*** | 0.00046 | -6.14 | 0.000 | [-0.0037, -0.0019] |

### 6.thumbnail.winshare — engagement_rate ~ winshare exposure (thumbnail)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0261

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_thumbnail_z` | -0.00036 | 0.00026 | -1.36 | 0.173 | [-0.0009, +0.0002] |
| `log_days_since_upload` | -0.00281*** | 0.00046 | -6.14 | 0.000 | [-0.0037, -0.0019] |

### 6.thumbnail.streak — engagement_rate ~ streak exposure (thumbnail)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0256

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_thumbnail_z` | -0.00002 | 0.00019 | -0.11 | 0.910 | [-0.0004, +0.0004] |
| `log_days_since_upload` | -0.00282*** | 0.00045 | -6.23 | 0.000 | [-0.0037, -0.0019] |

### 6.thumbnail.nonlinear — engagement_rate ~ dose + dose^2 (thumbnail)
_quadratic in cumulative dose; channel FE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0262

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00032 | 0.00028 | -1.16 | 0.248 | [-0.0009, +0.0002] |
| `dose_thumbnail_z_sq` | +0.00009 | 0.00011 | +0.83 | 0.404 | [-0.0001, +0.0003] |
| `log_days_since_upload` | -0.00283*** | 0.00046 | -6.16 | 0.000 | [-0.0037, -0.0019] |

### 6.thumbnail.rebound — engagement_rate ~ template_similarity (thumbnail)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 6570 videos/obs across 72 channels; within-R² = 0.0419

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_thumbnail_z` | -0.00200*** | 0.00063 | -3.17 | 0.002 | [-0.0032, -0.0008] |
| `log_days_since_upload` | -0.00274*** | 0.00046 | -5.97 | 0.000 | [-0.0036, -0.0018] |

### 6.title.dose — engagement_rate ~ dose exposure (title)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0256

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00003 | 0.00029 | -0.11 | 0.913 | [-0.0006, +0.0005] |
| `log_days_since_upload` | -0.00282*** | 0.00046 | -6.09 | 0.000 | [-0.0037, -0.0019] |

### 6.title.winshare — engagement_rate ~ winshare exposure (title)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0256

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_title_z` | -0.00001 | 0.00030 | -0.03 | 0.974 | [-0.0006, +0.0006] |
| `log_days_since_upload` | -0.00282*** | 0.00046 | -6.09 | 0.000 | [-0.0037, -0.0019] |

### 6.title.streak — engagement_rate ~ streak exposure (title)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0256

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_title_z` | -0.00003 | 0.00020 | -0.13 | 0.893 | [-0.0004, +0.0004] |
| `log_days_since_upload` | -0.00282*** | 0.00046 | -6.18 | 0.000 | [-0.0037, -0.0019] |

### 6.title.nonlinear — engagement_rate ~ dose + dose^2 (title)
_quadratic in cumulative dose; channel FE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0257

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00001 | 0.00028 | -0.04 | 0.967 | [-0.0006, +0.0005] |
| `dose_title_z_sq` | +0.00009 | 0.00013 | +0.67 | 0.504 | [-0.0002, +0.0003] |
| `log_days_since_upload` | -0.00284*** | 0.00046 | -6.18 | 0.000 | [-0.0037, -0.0019] |

### 6.title.rebound — engagement_rate ~ template_similarity (title)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 6570 videos/obs across 72 channels; within-R² = 0.0417

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_title_z` | -0.00200*** | 0.00052 | -3.84 | 0.000 | [-0.0030, -0.0010] |
| `log_days_since_upload` | -0.00269*** | 0.00043 | -6.20 | 0.000 | [-0.0035, -0.0018] |

### 6.combined.dose — engagement_rate ~ dose exposure (combined)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0257

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00018 | 0.00024 | -0.76 | 0.450 | [-0.0007, +0.0003] |
| `log_days_since_upload` | -0.00281*** | 0.00046 | -6.10 | 0.000 | [-0.0037, -0.0019] |

### 6.combined.winshare — engagement_rate ~ winshare exposure (combined)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0257

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_combined_z` | -0.00018 | 0.00026 | -0.72 | 0.471 | [-0.0007, +0.0003] |
| `log_days_since_upload` | -0.00281*** | 0.00046 | -6.09 | 0.000 | [-0.0037, -0.0019] |

### 6.combined.streak — engagement_rate ~ streak exposure (combined)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0256

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_combined_z` | +0.00007 | 0.00023 | +0.29 | 0.769 | [-0.0004, +0.0005] |
| `log_days_since_upload` | -0.00283*** | 0.00045 | -6.22 | 0.000 | [-0.0037, -0.0019] |

### 6.combined.nonlinear — engagement_rate ~ dose + dose^2 (combined)
_quadratic in cumulative dose; channel FE_

N = 6499 videos/obs across 72 channels; within-R² = 0.0262

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00014 | 0.00024 | -0.56 | 0.573 | [-0.0006, +0.0003] |
| `dose_combined_z_sq` | +0.00020* | 0.00011 | +1.79 | 0.073 | [-0.0000, +0.0004] |
| `log_days_since_upload` | -0.00285*** | 0.00046 | -6.24 | 0.000 | [-0.0037, -0.0020] |

### 6.combined.rebound — engagement_rate ~ template_similarity (combined)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 6570 videos/obs across 72 channels; within-R² = 0.0493

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_combined_z` | -0.00242*** | 0.00064 | -3.76 | 0.000 | [-0.0037, -0.0012] |
| `log_days_since_upload` | -0.00268*** | 0.00044 | -6.09 | 0.000 | [-0.0035, -0.0018] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 2857 videos/obs across 72 channels; within-R² = 0.0158

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | -0.00152*** | 0.00045 | -3.38 | 0.001 | [-0.0024, -0.0006] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 2857 videos/obs across 72 channels; within-R² = 0.0121

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00133*** | 0.00033 | -4.07 | 0.000 | [-0.0020, -0.0007] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 2857 videos/obs across 72 channels; within-R² = 0.0171

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00158*** | 0.00041 | -3.90 | 0.000 | [-0.0024, -0.0008] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2784 videos/obs across 71 channels; within-R² = 0.0006

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.02361 | 0.02187 | -1.08 | 0.280 | [-0.0665, +0.0193] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 2814 videos/obs across 72 channels; within-R² = 0.0006

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.02455 | 0.02337 | -1.05 | 0.293 | [-0.0704, +0.0213] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2784 videos/obs across 71 channels; within-R² = 0.0019

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.04341* | 0.02376 | -1.83 | 0.068 | [-0.0900, +0.0032] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 2814 videos/obs across 72 channels; within-R² = 0.0000

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.00210 | 0.02247 | -0.09 | 0.926 | [-0.0462, +0.0420] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2784 videos/obs across 71 channels; within-R² = 0.0014

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03734 | 0.02402 | -1.55 | 0.120 | [-0.0844, +0.0098] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 2814 videos/obs across 72 channels; within-R² = 0.0001

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.00780 | 0.02447 | -0.32 | 0.750 | [-0.0558, +0.0402] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 25 channels meet 'strong start + later homogenized'.

### 4.thumbnail — engagement_rate ~ formula_adherence (subsample)
_same spec as Model 1, restricted sample_

N = 2221 videos/obs across 25 channels; within-R² = 0.0509

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00281* | 0.00146 | -1.92 | 0.055 | [-0.0057, +0.0001] |
| `log_days_since_upload` | -0.00357*** | 0.00105 | -3.38 | 0.001 | [-0.0056, -0.0015] |


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0755; median = 0.0759; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.298 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UCVYamHliCI9rw1tHR1xbkfw.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCXGgrKt94gR6lmN4aN3mYTg.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCBJycsmduvYEL83R_U4JriQ.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCWsEZ9v1KC8b5VYjYbEewJA` (0.881); least = `https://www.youtube.com/channel/UCymYq4Piq0BrhnM18aQzTlg` (0.605).
