# FINDINGS — Study 1: stylistic homogeneity → engagement wear-out

**Sample:** 238 channels, 26897 videos (personal-finance/investing niche; snapshot taken 2026-06-20).

## Headline (H1)
Within a channel, a +1 within-channel-SD increase in thumbnail formula-adherence is associated with **-0.00068** change in engagement_rate (SE 0.00036, p=0.056) — i.e. **LOWER** subsequent engagement, controlling for video age, subscribers, and upload frequency, with channel fixed effects. This is **not statistically significant (p≥0.05)**.

H1 predicts a NEGATIVE coefficient. **Not clearly supported** at conventional significance — reported honestly.

## All specifications (coefficient on the homogeneity regressor)

| model | outcome | coef | SE | p | N obs | N chan |
|---|---|---:|---:|---:|---:|---:|
| core_thumbnail | engagement_rate | -0.00068 | 0.00036 | 0.056 | 26149 | 238 |
| core_title | engagement_rate | -0.00064 | 0.00036 | 0.071 | 26150 | 238 |
| core_combined | engagement_rate | -0.00087 | 0.00035 | 0.012 | 26149 | 238 |
| core_thumbnail_logviews | log_views | -0.06812 | 0.01859 | 0.000 | 26658 | 238 |
| core_title_logviews | log_views | +0.06179 | 0.01589 | 0.000 | 26659 | 238 |
| core_combined_logviews | log_views | -0.00364 | 0.01757 | 0.836 | 26658 | 238 |
| week_thumbnail | engagement_rate | +0.00057 | 0.00031 | 0.066 | 11296 | 234 |
| week_title | engagement_rate | -0.00059 | 0.00049 | 0.225 | 11296 | 234 |
| week_combined | engagement_rate | -0.00021 | 0.00038 | 0.582 | 11296 | 234 |
| direction_thumbnail_forward | engagement | +0.02560 | 0.01123 | 0.023 | 11064 | 234 |
| direction_thumbnail_reverse | homogeneity | +0.02859 | 0.01150 | 0.013 | 11163 | 234 |
| direction_title_forward | engagement | +0.01316 | 0.01207 | 0.275 | 11064 | 234 |
| direction_title_reverse | homogeneity | +0.01343 | 0.01169 | 0.251 | 11163 | 234 |
| direction_combined_forward | engagement | +0.02344 | 0.01146 | 0.041 | 11064 | 234 |
| direction_combined_reverse | homogeneity | +0.02388 | 0.01185 | 0.044 | 11163 | 234 |
| robust_thumbnail | engagement_rate | -0.00009 | 0.00101 | 0.929 | 7639 | 71 |

## Direction probe (suggestive, not causal)
Forward (engagement_t ~ homogeneity_(t-1)): coef +0.0256 (p=0.023). Reverse (homogeneity_t ~ engagement_(t-1)): coef +0.0286 (p=0.013). Reverse is comparable/stronger — cannot rule out that declining engagement drives homogenization (the main reverse-causation threat).

## Robustness subsample (strong-start, then homogenized)
Coef -0.00009 (p=0.929, N=7639). H1 does not clearly survive here.

## Sanity checks

## 5. Manipulation / sanity checks

**5a. Within-channel SD of formula_adherence (thumbnail)** — the regressor must vary within channel or the test is dead.

- mean within-channel SD = 0.0874; median = 0.0855; share of channels with SD>0.02 = 100%


**5b. Thumbnail-sim vs title-sim correlation** (per channel, pairwise): mean = 0.221 (want positive but <1 — related, not redundant).


**5c. Thumbnail-tile panels** (eyeball the score): `sanity_thumbnail_Erika2.png`, `sanity_thumbnail_https:__www.youtube.com_channel_UC9vUu4vlIlMC0dHQCTvQPbg.png`, `sanity_thumbnail_GrahamStephan.png`


Homogeneity ranking (thumbnail): most-formulaic = `https://www.youtube.com/channel/UC9JYZbC-3QoAQVo6GHjKznw` (0.999); least = `https://www.youtube.com/channel/UCvJJ_dzjViJCoLf5uKUTwoA` (0.565).


## LIMITATIONS (read these)
- **Snapshot, not trajectory.** Engagement is accumulated stats at one scrape; we control for age and use the age-robust engagement_rate, but per-video time dynamics await the longitudinal rescrape dataset (M5).
- **Observational.** Channel FE removes fixed confounders but not time-varying ones (e.g. a channel simultaneously homogenizing AND declining for an external reason).
- **Reverse causation** is probed, not eliminated — see the direction section.
- **Single niche** (personal finance). External validity to other niches is untested.
- **Discovery noise.** Search-expanded channels may include some off-niche channels.
- **Membership-gated uploads** reduce yield on some channels (kept-if-public only).