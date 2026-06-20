# Model summaries — Study 1

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 1009 videos/obs across 14 channels; within-R² = 0.0037

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00020 | 0.00021 | -0.95 | 0.341 | [-0.0006, +0.0002] |
| `log_days_since_upload` | +0.00059 | 0.00044 | +1.34 | 0.181 | [-0.0003, +0.0015] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 1009 videos/obs across 14 channels; within-R² = 0.0157

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00116** | 0.00052 | -2.20 | 0.028 | [-0.0022, -0.0001] |
| `log_days_since_upload` | +0.00049 | 0.00047 | +1.04 | 0.299 | [-0.0004, +0.0014] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 1009 videos/obs across 14 channels; within-R² = 0.0103

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00088* | 0.00046 | -1.91 | 0.057 | [-0.0018, +0.0000] |
| `log_days_since_upload` | +0.00047 | 0.00048 | +0.97 | 0.330 | [-0.0005, +0.0014] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 1009 videos/obs across 14 channels; within-R² = 0.0030

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00743 | 0.05031 | -0.15 | 0.883 | [-0.1062, +0.0913] |
| `log_days_since_upload` | +0.05172 | 0.07403 | +0.70 | 0.485 | [-0.0936, +0.1970] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 1009 videos/obs across 14 channels; within-R² = 0.0079

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.06570 | 0.05395 | +1.22 | 0.224 | [-0.0402, +0.1716] |
| `log_days_since_upload` | +0.06023 | 0.07677 | +0.78 | 0.433 | [-0.0904, +0.2109] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 1009 videos/obs across 14 channels; within-R² = 0.0051

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | +0.04292 | 0.04565 | +0.94 | 0.347 | [-0.0467, +0.1325] |
| `log_days_since_upload` | +0.06007 | 0.07615 | +0.79 | 0.430 | [-0.0894, +0.2095] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 792 videos/obs across 14 channels; within-R² = 0.0021

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | -0.00048** | 0.00020 | -2.35 | 0.019 | [-0.0009, -0.0001] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 792 videos/obs across 14 channels; within-R² = 0.0120

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00114** | 0.00054 | -2.10 | 0.036 | [-0.0022, -0.0001] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 792 videos/obs across 14 channels; within-R² = 0.0083

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00095** | 0.00043 | -2.19 | 0.029 | [-0.0018, -0.0001] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 778 videos/obs across 14 channels; within-R² = 0.0015

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03817 | 0.04449 | -0.86 | 0.391 | [-0.1255, +0.0492] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 790 videos/obs across 14 channels; within-R² = 0.0000

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | -0.00200 | 0.02717 | -0.07 | 0.941 | [-0.0553, +0.0513] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 778 videos/obs across 14 channels; within-R² = 0.0012

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.03386 | 0.04621 | -0.73 | 0.464 | [-0.1246, +0.0569] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 790 videos/obs across 14 channels; within-R² = 0.0004

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.01972 | 0.03935 | +0.50 | 0.616 | [-0.0575, +0.0970] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 778 videos/obs across 14 channels; within-R² = 0.0017

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | -0.04033 | 0.05328 | -0.76 | 0.449 | [-0.1449, +0.0643] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 790 videos/obs across 14 channels; within-R² = 0.0001

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.01185 | 0.03771 | +0.31 | 0.753 | [-0.0622, +0.0859] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 4 channels meet 'strong start + later homogenized'.

_Too few channels for a stable estimate._


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0755; median = 0.0758; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.229 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_ThePlainBagel.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UCIbslwukNCyVp-XMz_2-gmw.png`, `sanity_thumbnail_BenFelixCSI.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UCGy7SkBjcIAgTiwkXEtPnYg` (0.777); least = `https://www.youtube.com/channel/UCFBpVaKCC0ajGps1vf0AgBg` (0.622).
