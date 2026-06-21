# Model summaries — Study 1 (Shorts EXCLUDED)

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0450

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00141** | 0.00070 | -2.01 | 0.044 | [-0.0028, -0.0000] |
| `log_days_since_upload` | -0.00450*** | 0.00062 | -7.24 | 0.000 | [-0.0057, -0.0033] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0519

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00220*** | 0.00075 | -2.92 | 0.004 | [-0.0037, -0.0007] |
| `log_days_since_upload` | -0.00444*** | 0.00062 | -7.16 | 0.000 | [-0.0057, -0.0032] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0528

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00229*** | 0.00079 | -2.92 | 0.004 | [-0.0038, -0.0008] |
| `log_days_since_upload` | -0.00450*** | 0.00062 | -7.27 | 0.000 | [-0.0057, -0.0033] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 5033 videos/obs across 75 channels; within-R² = 0.0553

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | +0.11521*** | 0.02467 | +4.67 | 0.000 | [+0.0668, +0.1636] |
| `log_days_since_upload` | +0.24185*** | 0.04943 | +4.89 | 0.000 | [+0.1449, +0.3388] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 5033 videos/obs across 75 channels; within-R² = 0.0505

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.08957*** | 0.02958 | +3.03 | 0.002 | [+0.0316, +0.1476] |
| `log_days_since_upload` | +0.23800*** | 0.05028 | +4.73 | 0.000 | [+0.1394, +0.3366] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 5033 videos/obs across 75 channels; within-R² = 0.0561

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | +0.11870*** | 0.02856 | +4.16 | 0.000 | [+0.0627, +0.1747] |
| `log_days_since_upload` | +0.24082*** | 0.04957 | +4.86 | 0.000 | [+0.1436, +0.3380] |


## 6. Wear-out: cumulative formula EXPOSURE (redesign)

Outcome = engagement_rate. Predictor = accumulated exposure to the channel's formula BEFORE the video (recency-weighted dose / window-share / streak), z-scored within channel. Channel FE; clustered SE. Wear-out => NEGATIVE coefficient.

### 6.thumbnail.dose — engagement_rate ~ dose exposure (thumbnail)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0404

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00031 | 0.00059 | -0.52 | 0.600 | [-0.0015, +0.0008] |
| `log_days_since_upload` | -0.00444*** | 0.00061 | -7.24 | 0.000 | [-0.0056, -0.0032] |

### 6.thumbnail.winshare — engagement_rate ~ winshare exposure (thumbnail)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0405

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_thumbnail_z` | -0.00034 | 0.00065 | -0.52 | 0.606 | [-0.0016, +0.0009] |
| `log_days_since_upload` | -0.00444*** | 0.00061 | -7.31 | 0.000 | [-0.0056, -0.0032] |

### 6.thumbnail.streak — engagement_rate ~ streak exposure (thumbnail)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0402

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_thumbnail_z` | -0.00010 | 0.00030 | -0.33 | 0.740 | [-0.0007, +0.0005] |
| `log_days_since_upload` | -0.00446*** | 0.00063 | -7.06 | 0.000 | [-0.0057, -0.0032] |

### 6.thumbnail.nonlinear — engagement_rate ~ dose + dose^2 (thumbnail)
_quadratic in cumulative dose; channel FE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0407

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00021 | 0.00054 | -0.39 | 0.699 | [-0.0013, +0.0008] |
| `dose_thumbnail_z_sq` | +0.00021 | 0.00024 | +0.89 | 0.374 | [-0.0003, +0.0007] |
| `log_days_since_upload` | -0.00447*** | 0.00063 | -7.13 | 0.000 | [-0.0057, -0.0032] |

### 6.thumbnail.rebound — engagement_rate ~ template_similarity (thumbnail)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 4996 videos/obs across 74 channels; within-R² = 0.0438

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_thumbnail_z` | -0.00119* | 0.00071 | -1.68 | 0.093 | [-0.0026, +0.0002] |
| `log_days_since_upload` | -0.00441*** | 0.00062 | -7.13 | 0.000 | [-0.0056, -0.0032] |

### 6.title.dose — engagement_rate ~ dose exposure (title)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0414

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00072 | 0.00060 | -1.19 | 0.234 | [-0.0019, +0.0005] |
| `log_days_since_upload` | -0.00444*** | 0.00062 | -7.16 | 0.000 | [-0.0057, -0.0032] |

### 6.title.winshare — engagement_rate ~ winshare exposure (title)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0411

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_title_z` | -0.00062 | 0.00058 | -1.06 | 0.287 | [-0.0018, +0.0005] |
| `log_days_since_upload` | -0.00444*** | 0.00062 | -7.15 | 0.000 | [-0.0057, -0.0032] |

### 6.title.streak — engagement_rate ~ streak exposure (title)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0402

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_title_z` | -0.00010 | 0.00042 | -0.23 | 0.815 | [-0.0009, +0.0007] |
| `log_days_since_upload` | -0.00446*** | 0.00063 | -7.08 | 0.000 | [-0.0057, -0.0032] |

### 6.title.nonlinear — engagement_rate ~ dose + dose^2 (title)
_quadratic in cumulative dose; channel FE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0415

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | -0.00067 | 0.00055 | -1.21 | 0.226 | [-0.0017, +0.0004] |
| `dose_title_z_sq` | +0.00011 | 0.00025 | +0.44 | 0.660 | [-0.0004, +0.0006] |
| `log_days_since_upload` | -0.00445*** | 0.00063 | -7.06 | 0.000 | [-0.0057, -0.0032] |

### 6.title.rebound — engagement_rate ~ template_similarity (title)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 4996 videos/obs across 74 channels; within-R² = 0.0545

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_title_z` | -0.00242*** | 0.00083 | -2.92 | 0.004 | [-0.0041, -0.0008] |
| `log_days_since_upload` | -0.00437*** | 0.00062 | -7.05 | 0.000 | [-0.0056, -0.0032] |

### 6.combined.dose — engagement_rate ~ dose exposure (combined)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0411

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00061 | 0.00064 | -0.95 | 0.342 | [-0.0019, +0.0006] |
| `log_days_since_upload` | -0.00444*** | 0.00062 | -7.20 | 0.000 | [-0.0057, -0.0032] |

### 6.combined.winshare — engagement_rate ~ winshare exposure (combined)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0409

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_combined_z` | -0.00055 | 0.00065 | -0.84 | 0.398 | [-0.0018, +0.0007] |
| `log_days_since_upload` | -0.00445*** | 0.00062 | -7.18 | 0.000 | [-0.0057, -0.0032] |

### 6.combined.streak — engagement_rate ~ streak exposure (combined)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0405

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_combined_z` | -0.00035 | 0.00039 | -0.90 | 0.366 | [-0.0011, +0.0004] |
| `log_days_since_upload` | -0.00446*** | 0.00063 | -7.10 | 0.000 | [-0.0057, -0.0032] |

### 6.combined.nonlinear — engagement_rate ~ dose + dose^2 (combined)
_quadratic in cumulative dose; channel FE_

N = 4924 videos/obs across 74 channels; within-R² = 0.0413

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00053 | 0.00059 | -0.89 | 0.374 | [-0.0017, +0.0006] |
| `dose_combined_z_sq` | +0.00020 | 0.00024 | +0.84 | 0.402 | [-0.0003, +0.0007] |
| `log_days_since_upload` | -0.00446*** | 0.00062 | -7.14 | 0.000 | [-0.0057, -0.0032] |

### 6.combined.rebound — engagement_rate ~ template_similarity (combined)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 4996 videos/obs across 74 channels; within-R² = 0.0551

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_combined_z` | -0.00247*** | 0.00087 | -2.86 | 0.004 | [-0.0042, -0.0008] |
| `log_days_since_upload` | -0.00435*** | 0.00061 | -7.13 | 0.000 | [-0.0055, -0.0032] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3045 videos/obs across 76 channels; within-R² = 0.0077

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | -0.00151*** | 0.00055 | -2.72 | 0.007 | [-0.0026, -0.0004] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3045 videos/obs across 76 channels; within-R² = 0.0214

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00251*** | 0.00068 | -3.69 | 0.000 | [-0.0038, -0.0012] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3045 videos/obs across 76 channels; within-R² = 0.0203

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00244*** | 0.00065 | -3.75 | 0.000 | [-0.0037, -0.0012] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2968 videos/obs across 75 channels; within-R² = 0.0000

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | +0.00008 | 0.02000 | +0.00 | 0.997 | [-0.0391, +0.0393] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3019 videos/obs across 76 channels; within-R² = 0.0020

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.04399** | 0.02197 | -2.00 | 0.045 | [-0.0871, -0.0009] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2968 videos/obs across 75 channels; within-R² = 0.0005

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.02118 | 0.02144 | -0.99 | 0.323 | [-0.0632, +0.0209] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3019 videos/obs across 76 channels; within-R² = 0.0016

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.03962* | 0.02400 | -1.65 | 0.099 | [-0.0867, +0.0074] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 2968 videos/obs across 75 channels; within-R² = 0.0003

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.01689 | 0.02328 | -0.73 | 0.468 | [-0.0625, +0.0288] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3019 videos/obs across 76 channels; within-R² = 0.0023

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.04750** | 0.02400 | -1.98 | 0.048 | [-0.0946, -0.0004] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 26 channels meet 'strong start + later homogenized'.

### 4.thumbnail — engagement_rate ~ formula_adherence (subsample)
_same spec as Model 1, restricted sample_

N = 1813 videos/obs across 26 channels; within-R² = 0.0178

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00107 | 0.00121 | -0.88 | 0.379 | [-0.0034, +0.0013] |
| `log_days_since_upload` | -0.00362*** | 0.00104 | -3.47 | 0.001 | [-0.0057, -0.0016] |


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0775; median = 0.0767; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.323 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UCzTKskwIc_-a0cGvCXA848Q.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCucot-Zp428OwkyRm2I7v2Q.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UC4qk9TtGhBKCkoWz5qGJcGg.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCrfr4PnqvdJO4KrYWg10CJw` (0.915); least = `https://www.youtube.com/channel/UCwv-GM0CxoTghE8t0Bin9mg` (0.628).
