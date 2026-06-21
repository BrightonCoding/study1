# Data dictionary — Study 1

Two panels. **Snapshot caveat:** view/like/comment counts are accumulated values at `scrape_date`, not a time series — always control for `days_since_upload` and prefer `engagement_rate`. The longitudinal `rescrape` dataset (M5) carries true trajectories.

## 1. video-level panel (`video_panel.parquet`)
8445 rows × 77 cols.

| column | description |
|---|---|
| `video_id` | YouTube video id (primary key). |
| `channel_id` | YouTube channel id (UC...). |
| `channel_title` | Channel display name. |
| `title` | Video title (raw). |
| `description` | Video description (raw). |
| `upload_date` | Upload date (ISO YYYY-MM-DD). |
| `duration_seconds` | Video duration in seconds. |
| `view_count` | Accumulated views AT SCRAPE TIME (snapshot, age-dependent). |
| `like_count` | Accumulated likes at scrape time; null if disabled. |
| `comment_count` | Accumulated comments at scrape time; null if disabled. |
| `subscriber_count` | Channel subscriber count at scrape time. |
| `tags` | Video tags (list) if present. |
| `webpage_url` | (see code) |
| `availability` | yt-dlp availability field (public/unlisted/...). |
| `was_live` | Flag: video was a livestream. |
| `from_shorts_tab` | (see code) |
| `scrape_date` | UTC date the snapshot was taken. |
| `days_since_upload` | scrape_date - upload_date, in days (age control). |
| `is_short` | Flag: detected YouTube Short (duration<=short_max_seconds or shorts source). |
| `like_count_is_null` | Flag: likes were unavailable/disabled. |
| `comment_count_is_null` | Flag: comments were unavailable/disabled. |
| `channel_ref` | Seed reference used to fetch the channel (@handle or URL). |
| `thumbnail_url` | URL of the highest-res thumbnail fetched. |
| `thumbnail_path` | Local cached thumbnail path (null if none usable). |
| `engagement_rate` | (like_count + comment_count) / view_count. PRIMARY age-robust outcome. |
| `like_rate` | like_count / view_count. |
| `comment_rate` | comment_count / view_count. |
| `log_views` | log1p(view_count). Secondary outcome; REQUIRES age control. |
| `log_subscribers` | log1p(subscriber_count). |
| `log_days_since_upload` | log1p(days_since_upload). Age control regressor. |
| `iso_week` | ISO year-week 'YYYY-Www' of upload_date. |
| `upload_frequency` | Channel uploads per week over its observed window. |
| `title_char_len` | Title length in characters. |
| `title_word_count` | Title word count. |
| `title_allcaps_ratio` | Share of alphabetic chars that are uppercase. |
| `title_has_question` | Flag: '?' present. |
| `title_has_exclaim` | Flag: '!' present. |
| `title_has_number` | Flag: a digit present. |
| `title_n_emoji` | Count of emoji. |
| `title_has_emoji` | Flag: any emoji. |
| `title_has_bracket_or_pipe` | Flag: contains [], (), or |. |
| `formula_adherence_thumbnail` | (a) cosine of video thumbnail-embedding to mean of channel's previous 10 videos. Higher=more on-formula. PRIMARY H1 regressor. |
| `rolling_homogeneity_thumbnail` | (b) mean pairwise cosine over trailing 10 thumbnail-embeddings (incl. current). |
| `niche_adherence_thumbnail` | (c) cosine of video thumbnail-embedding to niche top-performer centroid. |
| `formula_adherence_thumbnail_z` | formula_adherence_thumbnail z-scored WITHIN channel. |
| `formula_adherence_title` | (a) cosine of video title-embedding to mean of channel's previous 10 videos. Higher=more on-formula. PRIMARY H1 regressor. |
| `rolling_homogeneity_title` | (b) mean pairwise cosine over trailing 10 title-embeddings (incl. current). |
| `niche_adherence_title` | (c) cosine of video title-embedding to niche top-performer centroid. |
| `formula_adherence_title_z` | formula_adherence_title z-scored WITHIN channel. |
| `formula_adherence_combined` | (a) cosine of video combined-embedding to mean of channel's previous 10 videos. Higher=more on-formula. PRIMARY H1 regressor. |
| `rolling_homogeneity_combined` | (b) mean pairwise cosine over trailing 10 combined-embeddings (incl. current). |
| `niche_adherence_combined` | (c) cosine of video combined-embedding to niche top-performer centroid. |
| `formula_adherence_combined_z` | formula_adherence_combined z-scored WITHIN channel. |
| `tmpl_sim_thumbnail` | Cosine of video thumbnail-embedding to the channel's overall template centroid (how on-formula this video is). |
| `dose_thumbnail` | Wear-out: recency-weighted mean of PAST videos' on-template-ness (thumbnail). Higher = audience recently saturated with the formula. |
| `winshare_thumbnail` | Wear-out: mean on-template-ness over the previous 10 videos (thumbnail). |
| `streak_thumbnail` | Wear-out: # consecutive prior videos above the channel's median template-similarity (thumbnail). |
| `tmpl_sim_thumbnail_z` | tmpl_sim_thumbnail z-scored within channel. |
| `dose_thumbnail_z` | dose_thumbnail z-scored within channel. |
| `winshare_thumbnail_z` | winshare_thumbnail z-scored within channel. |
| `streak_thumbnail_z` | streak_thumbnail z-scored within channel. |
| `tmpl_sim_title` | Cosine of video title-embedding to the channel's overall template centroid (how on-formula this video is). |
| `dose_title` | Wear-out: recency-weighted mean of PAST videos' on-template-ness (title). Higher = audience recently saturated with the formula. |
| `winshare_title` | Wear-out: mean on-template-ness over the previous 10 videos (title). |
| `streak_title` | Wear-out: # consecutive prior videos above the channel's median template-similarity (title). |
| `tmpl_sim_title_z` | tmpl_sim_title z-scored within channel. |
| `dose_title_z` | dose_title z-scored within channel. |
| `winshare_title_z` | winshare_title z-scored within channel. |
| `streak_title_z` | streak_title z-scored within channel. |
| `tmpl_sim_combined` | Cosine of video combined-embedding to the channel's overall template centroid (how on-formula this video is). |
| `dose_combined` | Wear-out: recency-weighted mean of PAST videos' on-template-ness (combined). Higher = audience recently saturated with the formula. |
| `winshare_combined` | Wear-out: mean on-template-ness over the previous 10 videos (combined). |
| `streak_combined` | Wear-out: # consecutive prior videos above the channel's median template-similarity (combined). |
| `tmpl_sim_combined_z` | tmpl_sim_combined z-scored within channel. |
| `dose_combined_z` | dose_combined z-scored within channel. |
| `winshare_combined_z` | winshare_combined z-scored within channel. |
| `streak_combined_z` | streak_combined z-scored within channel. |

## 2. channel-week panel (`channel_week_panel.parquet`)
3777 rows × 24 cols. Aggregated to (channel_ref, iso_week).

| column | description |
|---|---|
| `channel_ref` | Seed reference used to fetch the channel (@handle or URL). |
| `iso_week` | ISO year-week 'YYYY-Www' of upload_date. |
| `engagement_rate` | (like_count + comment_count) / view_count. PRIMARY age-robust outcome. |
| `like_rate` | like_count / view_count. |
| `comment_rate` | comment_count / view_count. |
| `log_views` | log1p(view_count). Secondary outcome; REQUIRES age control. |
| `view_count` | Accumulated views AT SCRAPE TIME (snapshot, age-dependent). |
| `days_since_upload` | scrape_date - upload_date, in days (age control). |
| `subscriber_count` | Channel subscriber count at scrape time. |
| `upload_frequency` | Channel uploads per week over its observed window. |
| `n_uploads` | (channel-week) number of uploads that week. |
| `formula_adherence_thumbnail` | (a) cosine of video thumbnail-embedding to mean of channel's previous 10 videos. Higher=more on-formula. PRIMARY H1 regressor. |
| `rolling_homogeneity_thumbnail` | (b) mean pairwise cosine over trailing 10 thumbnail-embeddings (incl. current). |
| `niche_adherence_thumbnail` | (c) cosine of video thumbnail-embedding to niche top-performer centroid. |
| `formula_adherence_title` | (a) cosine of video title-embedding to mean of channel's previous 10 videos. Higher=more on-formula. PRIMARY H1 regressor. |
| `rolling_homogeneity_title` | (b) mean pairwise cosine over trailing 10 title-embeddings (incl. current). |
| `niche_adherence_title` | (c) cosine of video title-embedding to niche top-performer centroid. |
| `formula_adherence_combined` | (a) cosine of video combined-embedding to mean of channel's previous 10 videos. Higher=more on-formula. PRIMARY H1 regressor. |
| `rolling_homogeneity_combined` | (b) mean pairwise cosine over trailing 10 combined-embeddings (incl. current). |
| `niche_adherence_combined` | (c) cosine of video combined-embedding to niche top-performer centroid. |
| `week_pairwise_homogeneity_thumbnail` | (channel-week) mean pairwise cosine among that week's thumbnail-embeddings. |
| `week_pairwise_homogeneity_title` | (channel-week) mean pairwise cosine among that week's title-embeddings. |
| `week_pairwise_homogeneity_combined` | (channel-week) mean pairwise cosine among that week's combined-embeddings. |
| `channel_id` | YouTube channel id (UC...). |