# Model summaries — Study 1

## 1. Core within-channel association (video-level)

Outcome = engagement_rate. Regressor of interest = formula_adherence (z-scored within channel → coef is per +1 within-channel SD of 'on-formula-ness'). Channel FE; SE clustered by channel.

### 1.thumbnail — engagement_rate ~ formula_adherence (thumbnail)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 26149 videos/obs across 238 channels; within-R² = 0.0027

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00068* | 0.00036 | -1.92 | 0.056 | [-0.0014, +0.0000] |
| `log_days_since_upload` | -0.00165*** | 0.00058 | -2.85 | 0.004 | [-0.0028, -0.0005] |

### 1.title — engagement_rate ~ formula_adherence (title)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 26150 videos/obs across 238 channels; within-R² = 0.0027

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | -0.00064* | 0.00036 | -1.80 | 0.071 | [-0.0013, +0.0001] |
| `log_days_since_upload` | -0.00163*** | 0.00057 | -2.86 | 0.004 | [-0.0027, -0.0005] |

### 1.combined — engagement_rate ~ formula_adherence (combined)
_engagement_rate ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 26149 videos/obs across 238 channels; within-R² = 0.0030

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00087** | 0.00035 | -2.50 | 0.012 | [-0.0015, -0.0002] |
| `log_days_since_upload` | -0.00166*** | 0.00057 | -2.90 | 0.004 | [-0.0028, -0.0005] |

### 1.thumbnail.logviews — log_views ~ formula_adherence (thumbnail) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 26658 videos/obs across 238 channels; within-R² = 0.0317

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.06812*** | 0.01859 | -3.66 | 0.000 | [-0.1046, -0.0317] |
| `log_days_since_upload` | +0.22277*** | 0.02416 | +9.22 | 0.000 | [+0.1754, +0.2701] |

### 1.title.logviews — log_views ~ formula_adherence (title) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 26659 videos/obs across 238 channels; within-R² = 0.0311

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_title_z` | +0.06179*** | 0.01589 | +3.89 | 0.000 | [+0.0306, +0.0929] |
| `log_days_since_upload` | +0.22823*** | 0.02404 | +9.50 | 0.000 | [+0.1811, +0.2753] |

### 1.combined.logviews — log_views ~ formula_adherence (combined) [age-controlled]
_log_views ~ formula_adherence_z + log_days_since_upload + log_subscribers + upload_frequency + ChannelFE_

N = 26658 videos/obs across 238 channels; within-R² = 0.0285

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_combined_z` | -0.00364 | 0.01757 | -0.21 | 0.836 | [-0.0381, +0.0308] |
| `log_days_since_upload` | +0.22632*** | 0.02416 | +9.37 | 0.000 | [+0.1790, +0.2737] |


## 2. Channel-week association

Outcome = mean engagement_rate per (channel, week). Homogeneity = week pairwise homogeneity (falls back to mean formula_adherence where pairwise is sparse). Channel FE; SE clustered by channel.

### 2.thumbnail — mean engagement_rate ~ homogeneity (thumbnail)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 11296 videos/obs across 234 channels; within-R² = 0.0005

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_thumbnail_z` | +0.00057* | 0.00031 | +1.84 | 0.066 | [-0.0000, +0.0012] |

### 2.title — mean engagement_rate ~ homogeneity (title)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 11296 videos/obs across 234 channels; within-R² = 0.0005

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_title_z` | -0.00059 | 0.00049 | -1.21 | 0.225 | [-0.0015, +0.0004] |

### 2.combined — mean engagement_rate ~ homogeneity (combined)
_engagement_rate ~ homogeneity_z + log_subscribers + upload_frequency + ChannelFE_

N = 11296 videos/obs across 234 channels; within-R² = 0.0001

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_combined_z` | -0.00021 | 0.00038 | -0.55 | 0.582 | [-0.0009, +0.0005] |


## 3. Direction / reverse-causation probe (poor-man's Granger)

Forward: engagement_t ~ homogeneity_{t-1}. Reverse: homogeneity_t ~ engagement_{t-1}. Both with channel FE + clustered SE. Stronger forward than reverse is *suggestive* (NOT proof) that the arrow runs homogeneity→engagement.

### 3.thumbnail.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 11064 videos/obs across 234 channels; within-R² = 0.0007

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | +0.02560** | 0.01123 | +2.28 | 0.023 | [+0.0036, +0.0476] |

### 3.thumbnail.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 11163 videos/obs across 234 channels; within-R² = 0.0008

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.02859** | 0.01150 | +2.49 | 0.013 | [+0.0060, +0.0511] |

### 3.title.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 11064 videos/obs across 234 channels; within-R² = 0.0002

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | +0.01316 | 0.01207 | +1.09 | 0.275 | [-0.0105, +0.0368] |

### 3.title.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 11163 videos/obs across 234 channels; within-R² = 0.0002

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.01343 | 0.01169 | +1.15 | 0.251 | [-0.0095, +0.0363] |

### 3.combined.forward — engagement_t ~ homogeneity_(t-1)
_ChannelFE; standardized_

N = 11064 videos/obs across 234 channels; within-R² = 0.0006

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_hom_lag_z` | +0.02344** | 0.01146 | +2.05 | 0.041 | [+0.0010, +0.0459] |

### 3.combined.reverse — homogeneity_t ~ engagement_(t-1)
_ChannelFE; standardized_

N = 11163 videos/obs across 234 channels; within-R² = 0.0006

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `_eng_lag_z` | +0.02388** | 0.01185 | +2.01 | 0.044 | [+0.0006, +0.0471] |


## 4. Robustness subsample (strong-start, then homogenized)

Restrict to channels whose EARLY-window engagement was above the niche median AND whose LATE-window formula_adherence rose vs early. If H1 survives here, the effect is not just 'always-struggling channels chasing a formula'.

Subsample: 71 channels meet 'strong start + later homogenized'.

### 4.thumbnail — engagement_rate ~ formula_adherence (subsample)
_same spec as Model 1, restricted sample_

N = 7639 videos/obs across 71 channels; within-R² = 0.0003

| term | coef | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---|
| `formula_adherence_thumbnail_z` | -0.00009 | 0.00101 | -0.09 | 0.929 | [-0.0021, +0.0019] |
| `log_days_since_upload` | -0.00091 | 0.00179 | -0.51 | 0.611 | [-0.0044, +0.0026] |


## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0874; median = 0.0855; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.221 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_Erika2.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UC9vUu4vlIlMC0dHQCTvQPbg.png`, `sanity_thumbnail_GrahamStephan.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UC9JYZbC-3QoAQVo6GHjKznw` (0.999); least = `https://www.youtube.com/channel/UCvJJ_dzjViJCoLf5uKUTwoA` (0.565).
