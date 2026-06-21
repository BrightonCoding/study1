# Model summaries — Study 1

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0275

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00157*** | 0.00054 | -2.92 | 0.003 | [-0.0026, -0.0005] |
| `log_days_since_upload` | -0.00221*** | 0.00040 | -5.52 | 0.000 | [-0.0030, -0.0014] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0224

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00116*** | 0.00039 | -2.93 | 0.003 | [-0.0019, -0.0004] |
| `log_days_since_upload` | -0.00215*** | 0.00039 | -5.51 | 0.000 | [-0.0029, -0.0014] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0289

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00167*** | 0.00050 | -3.35 | 0.001 | [-0.0026, -0.0007] |
| `log_days_since_upload` | -0.00219*** | 0.00040 | -5.53 | 0.000 | [-0.0030, -0.0014] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8324 videos/obs across 72 channels; within-R² = 0.0437

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | +0.04093 | 0.02704 | +1.51 | 0.130 | [-0.0121, +0.0939] |
| `log_days_since_upload` | +0.26911*** | 0.02758 | +9.76 | 0.000 | [+0.2151, +0.3232] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8324 videos/obs across 72 channels; within-R² = 0.0604

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.15495*** | 0.02199 | +7.05 | 0.000 | [+0.1118, +0.1981] |
| `log_days_since_upload` | +0.26529*** | 0.02700 | +9.83 | 0.000 | [+0.2124, +0.3182] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 8324 videos/obs across 72 channels; within-R² = 0.0539

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | +0.12368*** | 0.02470 | +5.01 | 0.000 | [+0.0753, +0.1721] |
| `log_days_since_upload` | +0.26908*** | 0.02753 | +9.77 | 0.000 | [+0.2151, +0.3231] |


## 6. Wear-out: cumulative formula EXPOSURE (redesign)

Outcome = engagement_rate. Predictor = accumulated exposure to the channel's formula BEFORE the video (recency-weighted dose / window-share / streak), z-scored within channel. Channel FE; clustered SE. Wear-out => NEGATIVE coefficient.

### 6.thumbnail.dose — engagement_rate ~ dose exposure (thumbnail)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0168

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00027 | 0.00022 | -1.24 | 0.216 | [-0.0007, +0.0002] |
| `log_days_since_upload` | -0.00216*** | 0.00040 | -5.46 | 0.000 | [-0.0029, -0.0014] |

### 6.thumbnail.winshare — engagement_rate ~ winshare exposure (thumbnail)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0167

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_thumbnail_z` | -0.00023 | 0.00022 | -1.01 | 0.311 | [-0.0007, +0.0002] |
| `log_days_since_upload` | -0.00217*** | 0.00040 | -5.46 | 0.000 | [-0.0029, -0.0014] |

### 6.thumbnail.streak — engagement_rate ~ streak exposure (thumbnail)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0165

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_thumbnail_z` | -0.00004 | 0.00018 | -0.20 | 0.841 | [-0.0004, +0.0003] |
| `log_days_since_upload` | -0.00217*** | 0.00040 | -5.49 | 0.000 | [-0.0029, -0.0014] |

### 6.thumbnail.nonlinear — engagement_rate ~ dose + dose^2 (thumbnail)
_quadratic in cumulative dose; channel FE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0169

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_thumbnail_z` | -0.00027 | 0.00023 | -1.15 | 0.248 | [-0.0007, +0.0002] |
| `dose_thumbnail_z_sq` | +0.00003 | 0.00009 | +0.37 | 0.714 | [-0.0001, +0.0002] |
| `log_days_since_upload` | -0.00217*** | 0.00040 | -5.46 | 0.000 | [-0.0029, -0.0014] |

### 6.thumbnail.rebound — engagement_rate ~ template_similarity (thumbnail)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8351 videos/obs across 72 channels; within-R² = 0.0284

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_thumbnail_z` | -0.00165*** | 0.00057 | -2.90 | 0.004 | [-0.0028, -0.0005] |
| `log_days_since_upload` | -0.00212*** | 0.00040 | -5.34 | 0.000 | [-0.0029, -0.0013] |

### 6.title.dose — engagement_rate ~ dose exposure (title)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0165

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | +0.00008 | 0.00022 | +0.36 | 0.720 | [-0.0004, +0.0005] |
| `log_days_since_upload` | -0.00218*** | 0.00040 | -5.39 | 0.000 | [-0.0030, -0.0014] |

### 6.title.winshare — engagement_rate ~ winshare exposure (title)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0166

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_title_z` | +0.00012 | 0.00022 | +0.57 | 0.571 | [-0.0003, +0.0006] |
| `log_days_since_upload` | -0.00218*** | 0.00040 | -5.41 | 0.000 | [-0.0030, -0.0014] |

### 6.title.streak — engagement_rate ~ streak exposure (title)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0167

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_title_z` | +0.00023 | 0.00016 | +1.43 | 0.152 | [-0.0001, +0.0006] |
| `log_days_since_upload` | -0.00218*** | 0.00040 | -5.51 | 0.000 | [-0.0030, -0.0014] |

### 6.title.nonlinear — engagement_rate ~ dose + dose^2 (title)
_quadratic in cumulative dose; channel FE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0169

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_title_z` | +0.00013 | 0.00022 | +0.60 | 0.549 | [-0.0003, +0.0006] |
| `dose_title_z_sq` | +0.00019* | 0.00011 | +1.73 | 0.083 | [-0.0000, +0.0004] |
| `log_days_since_upload` | -0.00221*** | 0.00040 | -5.48 | 0.000 | [-0.0030, -0.0014] |

### 6.title.rebound — engagement_rate ~ template_similarity (title)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8351 videos/obs across 72 channels; within-R² = 0.0252

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_title_z` | -0.00142*** | 0.00045 | -3.14 | 0.002 | [-0.0023, -0.0005] |
| `log_days_since_upload` | -0.00208*** | 0.00038 | -5.44 | 0.000 | [-0.0028, -0.0013] |

### 6.combined.dose — engagement_rate ~ dose exposure (combined)
_engagement_rate ~ dose_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0165

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00008 | 0.00020 | -0.40 | 0.687 | [-0.0005, +0.0003] |
| `log_days_since_upload` | -0.00216*** | 0.00040 | -5.40 | 0.000 | [-0.0029, -0.0014] |

### 6.combined.winshare — engagement_rate ~ winshare exposure (combined)
_engagement_rate ~ winshare_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0165

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `winshare_combined_z` | -0.00003 | 0.00018 | -0.14 | 0.890 | [-0.0004, +0.0003] |
| `log_days_since_upload` | -0.00217*** | 0.00040 | -5.41 | 0.000 | [-0.0030, -0.0014] |

### 6.combined.streak — engagement_rate ~ streak exposure (combined)
_engagement_rate ~ streak_z + controls + ChannelFE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0167

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `streak_combined_z` | +0.00019 | 0.00018 | +1.02 | 0.309 | [-0.0002, +0.0005] |
| `log_days_since_upload` | -0.00218*** | 0.00039 | -5.52 | 0.000 | [-0.0030, -0.0014] |

### 6.combined.nonlinear — engagement_rate ~ dose + dose^2 (combined)
_quadratic in cumulative dose; channel FE_

N = 8280 videos/obs across 72 channels; within-R² = 0.0169

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `dose_combined_z` | -0.00003 | 0.00019 | -0.16 | 0.877 | [-0.0004, +0.0003] |
| `dose_combined_z_sq` | +0.00018* | 0.00011 | +1.71 | 0.087 | [-0.0000, +0.0004] |
| `log_days_since_upload` | -0.00219*** | 0.00040 | -5.46 | 0.000 | [-0.0030, -0.0014] |

### 6.combined.rebound — engagement_rate ~ template_similarity (combined)
_NEGATIVE => on-formula videos underperform / breaking formula bumps engagement_

N = 8351 videos/obs across 72 channels; within-R² = 0.0329

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `tmpl_sim_combined_z` | -0.00194*** | 0.00056 | -3.49 | 0.000 | [-0.0030, -0.0008] |
| `log_days_since_upload` | -0.00206*** | 0.00039 | -5.34 | 0.000 | [-0.0028, -0.0013] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3098 videos/obs across 72 channels; within-R² = 0.0121

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | -0.00127*** | 0.00041 | -3.11 | 0.002 | [-0.0021, -0.0005] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3098 videos/obs across 72 channels; within-R² = 0.0069

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00096*** | 0.00032 | -2.98 | 0.003 | [-0.0016, -0.0003] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 3098 videos/obs across 72 channels; within-R² = 0.0106

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00119*** | 0.00038 | -3.15 | 0.002 | [-0.0019, -0.0004] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3025 videos/obs across 71 channels; within-R² = 0.0008

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.02866 | 0.01897 | -1.51 | 0.131 | [-0.0658, +0.0085] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3053 videos/obs across 72 channels; within-R² = 0.0004

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.02000 | 0.02189 | -0.91 | 0.361 | [-0.0629, +0.0229] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3025 videos/obs across 71 channels; within-R² = 0.0012

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03463* | 0.02047 | -1.69 | 0.091 | [-0.0748, +0.0055] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3053 videos/obs across 72 channels; within-R² = 0.0000

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.00035 | 0.02161 | +0.02 | 0.987 | [-0.0420, +0.0427] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 3025 videos/obs across 71 channels; within-R² = 0.0011

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03351* | 0.02023 | -1.66 | 0.098 | [-0.0732, +0.0062] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 3053 videos/obs across 72 channels; within-R² = 0.0000

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.00375 | 0.02305 | -0.16 | 0.871 | [-0.0489, +0.0414] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 21 channels meet 'strong start + later homogenized'.

### 4.thumbnail — engagement_rate ~ formula_adherence (subsample)
_same spec as Model 1, restricted sample_

N = 2405 videos/obs across 21 channels; within-R² = 0.0326

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00254* | 0.00140 | -1.81 | 0.070 | [-0.0053, +0.0002] |
| `log_days_since_upload` | -0.00236** | 0.00098 | -2.41 | 0.016 | [-0.0043, -0.0004] |


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0763; median = 0.0760; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.266 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_https:__www.youtube.com_channel_UCVYamHliCI9rw1tHR1xbkfw.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCXGgrKt94gR6lmN4aN3mYTg.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCBJycsmduvYEL83R_U4JriQ.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCWsEZ9v1KC8b5VYjYbEewJA` (0.875); least = `https://www.youtube.com/channel/UCymYq4Piq0BrhnM18aQzTlg` (0.603).
