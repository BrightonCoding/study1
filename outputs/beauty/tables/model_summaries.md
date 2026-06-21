# Model summaries — Study 1

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0170

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00081 | 0.00066 | -1.22 | 0.223 | [-0.0021, +0.0005] |
| `log_days_since_upload` | -0.00302*** | 0.00066 | -4.56 | 0.000 | [-0.0043, -0.0017] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0180

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00106* | 0.00058 | -1.84 | 0.066 | [-0.0022, +0.0001] |
| `log_days_since_upload` | -0.00298*** | 0.00066 | -4.56 | 0.000 | [-0.0043, -0.0017] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0190

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00126* | 0.00065 | -1.94 | 0.052 | [-0.0025, +0.0000] |
| `log_days_since_upload` | -0.00300*** | 0.00066 | -4.57 | 0.000 | [-0.0043, -0.0017] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8368 videos/obs across 77 channels; within-R² = 0.0495

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | +0.05900** | 0.02415 | +2.44 | 0.015 | [+0.0117, +0.1063] |
| `log_days_since_upload` | +0.26324*** | 0.04539 | +5.80 | 0.000 | [+0.1743, +0.3522] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8368 videos/obs across 77 channels; within-R² = 0.0508

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.07061*** | 0.02319 | +3.05 | 0.002 | [+0.0252, +0.1161] |
| `log_days_since_upload` | +0.26063*** | 0.04517 | +5.77 | 0.000 | [+0.1721, +0.3492] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8368 videos/obs across 77 channels; within-R² = 0.0516

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | +0.07744*** | 0.02301 | +3.37 | 0.001 | [+0.0323, +0.1225] |
| `log_days_since_upload` | +0.26181*** | 0.04508 | +5.81 | 0.000 | [+0.1734, +0.3502] |


## 6. Wear-out: cumulative formula EXPOSURE (redesign)

Outcome = engagement_rate. Predictor = accumulated exposure to the channel's formula BEFORE the video (recency-weighted dose / window-share / streak), z-scored within channel. Channel FE; clustered SE. Wear-out => NEGATIVE coefficient.

### 6.thumbnail.dose — engagement_rate ~ dose exposure (thumbnail)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0166

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | +0.00068 | 0.00049 | +1.39 | 0.165 | [-0.0003, +0.0016] |
| `log_days_since_upload` | -0.00305*** | 0.00066 | -4.62 | 0.000 | [-0.0043, -0.0018] |

### 6.thumbnail.winshare — engagement_rate ~ winshare exposure (thumbnail)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0164

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_thumbnail_z` | +0.00062 | 0.00050 | +1.23 | 0.219 | [-0.0004, +0.0016] |
| `log_days_since_upload` | -0.00304*** | 0.00066 | -4.62 | 0.000 | [-0.0043, -0.0018] |

### 6.thumbnail.streak — engagement_rate ~ streak exposure (thumbnail)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0163

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_thumbnail_z` | +0.00055 | 0.00036 | +1.53 | 0.127 | [-0.0002, +0.0013] |
| `log_days_since_upload` | -0.00301*** | 0.00066 | -4.56 | 0.000 | [-0.0043, -0.0017] |

### 6.thumbnail.nonlinear — engagement_rate ~ dose + dose^2 (thumbnail)
_quadratic in cumulative dose; channel FE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0166

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | +0.00069 | 0.00046 | +1.51 | 0.132 | [-0.0002, +0.0016] |
| `dose_thumbnail_z_sq` | +0.00003 | 0.00021 | +0.12 | 0.901 | [-0.0004, +0.0004] |
| `log_days_since_upload` | -0.00305*** | 0.00066 | -4.59 | 0.000 | [-0.0043, -0.0017] |

### 6.thumbnail.rebound — engagement_rate ~ template_similarity (thumbnail)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8290 videos/obs across 76 channels; within-R² = 0.0166

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_thumbnail_z` | -0.00070 | 0.00068 | -1.03 | 0.303 | [-0.0020, +0.0006] |
| `log_days_since_upload` | -0.00298*** | 0.00065 | -4.58 | 0.000 | [-0.0042, -0.0017] |

### 6.title.dose — engagement_rate ~ dose exposure (title)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0158

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00029 | 0.00049 | -0.59 | 0.555 | [-0.0013, +0.0007] |
| `log_days_since_upload` | -0.00299*** | 0.00065 | -4.58 | 0.000 | [-0.0043, -0.0017] |

### 6.title.winshare — engagement_rate ~ winshare exposure (title)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0157

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_title_z` | -0.00018 | 0.00048 | -0.37 | 0.713 | [-0.0011, +0.0008] |
| `log_days_since_upload` | -0.00300*** | 0.00065 | -4.58 | 0.000 | [-0.0043, -0.0017] |

### 6.title.streak — engagement_rate ~ streak exposure (title)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0156

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_title_z` | +0.00012 | 0.00033 | +0.36 | 0.716 | [-0.0005, +0.0008] |
| `log_days_since_upload` | -0.00301*** | 0.00066 | -4.60 | 0.000 | [-0.0043, -0.0017] |

### 6.title.nonlinear — engagement_rate ~ dose + dose^2 (title)
_quadratic in cumulative dose; channel FE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0158

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00030 | 0.00048 | -0.64 | 0.523 | [-0.0012, +0.0006] |
| `dose_title_z_sq` | -0.00005 | 0.00022 | -0.21 | 0.836 | [-0.0005, +0.0004] |
| `log_days_since_upload` | -0.00299*** | 0.00066 | -4.55 | 0.000 | [-0.0043, -0.0017] |

### 6.title.rebound — engagement_rate ~ template_similarity (title)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8290 videos/obs across 76 channels; within-R² = 0.0171

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_title_z` | -0.00085 | 0.00062 | -1.37 | 0.170 | [-0.0021, +0.0004] |
| `log_days_since_upload` | -0.00296*** | 0.00065 | -4.57 | 0.000 | [-0.0042, -0.0017] |

### 6.combined.dose — engagement_rate ~ dose exposure (combined)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0157

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | +0.00023 | 0.00051 | +0.44 | 0.656 | [-0.0008, +0.0012] |
| `log_days_since_upload` | -0.00303*** | 0.00065 | -4.63 | 0.000 | [-0.0043, -0.0017] |

### 6.combined.winshare — engagement_rate ~ winshare exposure (combined)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0157

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_combined_z` | +0.00025 | 0.00052 | +0.48 | 0.632 | [-0.0008, +0.0013] |
| `log_days_since_upload` | -0.00303*** | 0.00065 | -4.63 | 0.000 | [-0.0043, -0.0017] |

### 6.combined.streak — engagement_rate ~ streak exposure (combined)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0156

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_combined_z` | +0.00001 | 0.00035 | +0.02 | 0.988 | [-0.0007, +0.0007] |
| `log_days_since_upload` | -0.00301*** | 0.00066 | -4.57 | 0.000 | [-0.0043, -0.0017] |

### 6.combined.nonlinear — engagement_rate ~ dose + dose^2 (combined)
_quadratic in cumulative dose; channel FE_

N = 8216 videos/obs across 76 channels; within-R² = 0.0157

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | +0.00023 | 0.00049 | +0.48 | 0.629 | [-0.0007, +0.0012] |
| `dose_combined_z_sq` | +0.00002 | 0.00024 | +0.10 | 0.920 | [-0.0004, +0.0005] |
| `log_days_since_upload` | -0.00303*** | 0.00065 | -4.62 | 0.000 | [-0.0043, -0.0017] |

### 6.combined.rebound — engagement_rate ~ template_similarity (combined)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8290 videos/obs across 76 channels; within-R² = 0.0183

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_combined_z` | -0.00113 | 0.00070 | -1.61 | 0.107 | [-0.0025, +0.0002] |
| `log_days_since_upload` | -0.00293*** | 0.00064 | -4.57 | 0.000 | [-0.0042, -0.0017] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3681 videos/obs across 76 channels; within-R² = 0.0003

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | -0.00030 | 0.00043 | -0.71 | 0.479 | [-0.0011, +0.0005] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3681 videos/obs across 76 channels; within-R² = 0.0086

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00155*** | 0.00057 | -2.72 | 0.007 | [-0.0027, -0.0004] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3681 videos/obs across 76 channels; within-R² = 0.0062

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00132*** | 0.00050 | -2.66 | 0.008 | [-0.0023, -0.0003] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3607 videos/obs across 76 channels; within-R² = 0.0003

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.01696 | 0.01948 | -0.87 | 0.384 | [-0.0552, +0.0212] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3642 videos/obs across 76 channels; within-R² = 0.0045

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.06669*** | 0.02150 | -3.10 | 0.002 | [-0.1088, -0.0245] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3607 videos/obs across 76 channels; within-R² = 0.0011

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03242 | 0.02072 | -1.56 | 0.118 | [-0.0731, +0.0082] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3642 videos/obs across 76 channels; within-R² = 0.0027

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.05158** | 0.02202 | -2.34 | 0.019 | [-0.0947, -0.0084] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3607 videos/obs across 76 channels; within-R² = 0.0013

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03619* | 0.02150 | -1.68 | 0.092 | [-0.0783, +0.0060] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3642 videos/obs across 76 channels; within-R² = 0.0049

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.07001*** | 0.02203 | -3.18 | 0.001 | [-0.1132, -0.0268] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 23 channels meet 'strong start + later homogenized'.

### 4.thumbnail — engagement_rate ~ formula_adherence (subsample)
_same spec as Model 1, restricted sample_

N = 2538 videos/obs across 23 channels; within-R² = 0.0041

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00004 | 0.00158 | -0.03 | 0.980 | [-0.0031, +0.0031] |
| `log_days_since_upload` | -0.00206 | 0.00136 | -1.52 | 0.129 | [-0.0047, +0.0006] |


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0765; median = 0.0752; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.273 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UCzTKskwIc_-a0cGvCXA848Q.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCucot-Zp428OwkyRm2I7v2Q.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UC4qk9TtGhBKCkoWz5qGJcGg.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UClm9D6Std5EnJruG4XtoS7g` (0.901); least = `https://www.youtube.com/channel/UCSavnEw5et6sKtWYXLzP2cg` (0.653).
