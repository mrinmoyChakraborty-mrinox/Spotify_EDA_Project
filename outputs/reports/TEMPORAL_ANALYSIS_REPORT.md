# Temporal Analysis Report

## Scope

The analysis groups tracks by the `year` column and calculates yearly track count, mean and median popularity, and mean energy, danceability, and valence. Years with fewer than 30 rows remain in summary tables and the count graph, but are shown faintly and not connected in the feature trend lines. This threshold is a readability aid, not a claim of statistical significance.

## Main findings

- The dataset spans **1971–2024**.
- Track count is highest in **2023** (6,427) and lowest in **1976** (9).
- Years with fewer than 30 tracks: 1971, 1972, 1974, 1975, 1976, 1978, 1980. These annual averages are particularly sensitive to sample composition.
- Average popularity is highest in **1976** (39.33; n=9) and lowest in **1992** (7.90; n=405). Do not infer a historical cause: popularity scores, coverage, and cohort sizes differ.
- Energy, danceability, and valence trends are available in the annual summary CSV and charts. Read them alongside yearly track counts.

## Graph guide

Each graph's objective is to show change by release year. The line chart reports yearly averages; popularity also reports a yearly median and count in the table. Main insight: historical variation is descriptive and annual sample sizes are uneven. Recommendation: use these patterns to form a question for a current, controlled release-planning test. Limitation: this is a cross-sectional dataset with no control for artist, genre, promotion, track age, or collection process.

Files: `yearly_track_count.png`, `yearly_average_popularity.png`, `yearly_average_energy.png`, `yearly_average_danceability.png`, `yearly_average_valence.png`, and `combined_temporal_features.png`.

The combined chart min-max normalizes each feature separately across the included years. Its vertical values compare within-feature shapes only, not original values. Popularity is excluded because it uses a 0–100 scale.

## Graph-specific evidence and recommendations

- **Yearly track count:** 2023 is the maximum (6,427); 1976 is the minimum (9). The chart shows uneven dataset representation. Use year averages cautiously and plan with current audience signals.
- **Average popularity:** Across all years, 1976 is highest (39.33; n=9) and 1992 lowest (7.90; n=405). Among years with at least 30 tracks, 1977 is highest (34.46; n=39) and 1992 lowest (7.90; n=405). Treat this as historical context, not a release target.
- **Average energy:** Among years with at least 30 tracks, the range is 0.438 (1991) to 0.651 (1977). This describes the sampled tracks; it does not show that energy should be raised or lowered.
- **Average danceability:** The eligible-year range is 0.448 (1977) to 0.683 (1993). Compare with current audience tests before using it in production decisions.
- **Average valence:** The eligible-year range is 0.450 (2021) to 0.726 (1987). Valence is an audio estimate of positive musical character, not listener sentiment.
- **Combined normalized features:** The chart compares each eligible feature's relative position within its own observed range. Use it to compare broad shapes only; it contains no absolute feature score and suggests no causal mechanism.
