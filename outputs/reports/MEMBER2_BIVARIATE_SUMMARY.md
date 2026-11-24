# Member 2 - Bivariate Analysis Summary

## 1. Scope and data

This report covers Member 2's **Bivariate Analysis**, implemented in the standalone notebook `person2_eda.ipynb`. The main `Spotify_EDA.ipynb` is left unchanged. Bivariate analysis studies the relationship between two variables.

- Input: `data/processed/cleaned_spotify_tracks.csv`, the existing cleaned dataset produced by Section 6 of the main notebook. The standalone notebook loads it as `df_clean`; it does not re-clean the raw file.
- Cleaning was **not** repeated. Exact duplicate rows were already removed, and invalid sentinel values were already marked as missing.
- Cleaned rows available: **62,239**.
- Most audio-feature pairs have **62,204** valid observations because 35 rows have missing feature values after sentinel cleaning.
- Duration/popularity has **62,239** valid observations because duration has no sentinel-missing values.
- Correlations use **pairwise valid observations**. The original `df_clean` is never modified.

All charts were saved at **180 DPI** in `outputs/graphs/bivariate/` using the shared Spotify dark chart theme.

## 2. Methods

- **Pearson correlation** measures the strength and direction of a straight-line association.
- **Spearman correlation** measures the strength and direction of a monotonic association.
- Scatter plots use a reproducible random sample of at most **5,000** points (`random_state=42`) for readability.
- Correlations are calculated from **all** pairwise valid rows, not from the 5,000-point sample.
- Duration is converted from milliseconds to minutes **in an analysis copy**; `df_clean` is unchanged.
- Key, mode, and time signature are treated as **categories**, not continuous measurements, and are excluded from the numerical heatmaps.
- Correlation describes association only. **Correlation does not prove causation.**

Strength labels used in this report:

| Absolute correlation | Description |
|---|---|
| below 0.10 | negligible / very weak |
| 0.10 to below 0.30 | weak |
| 0.30 to below 0.50 | moderate |
| 0.50 to below 0.70 | strong |
| 0.70 and above | very strong |

## 3. Numerical relationships with popularity

| Variable X | Variable Y | Pearson r | Spearman r | Valid n | Reading |
|---|---|---:|---:|---:|---|
| Energy | Popularity | 0.147 | 0.131 | 62,204 | weak positive |
| Danceability | Popularity | 0.042 | -0.015 | 62,204 | negligible, inconsistent sign |
| Valence | Popularity | 0.009 | -0.032 | 62,204 | negligible |
| Duration (minutes) | Popularity | -0.040 | -0.054 | 62,239 | negligible |
| Loudness | Popularity | 0.201 | 0.204 | 62,204 | weak positive |
| Acousticness | Popularity | -0.138 | -0.120 | 62,204 | weak negative |
| Instrumentalness | Popularity | -0.127 | -0.089 | 62,204 | weak negative |
| Liveness | Popularity | -0.012 | -0.019 | 62,204 | negligible |
| Tempo | Popularity | 0.028 | 0.019 | 62,204 | negligible |
| Energy | Danceability | 0.466 | 0.360 | 62,204 | moderate positive |

The full 55-pair table is saved in `outputs/tables/MEMBER2_CORRELATION_RESULTS.csv`.

### What the scatter plots show

- **Energy vs popularity:** a slight upward tendency, but a wide cloud of points. Energy explains only about 2% of popularity variation (r-squared about 0.022).
- **Danceability vs popularity:** essentially flat. Pearson is slightly positive and Spearman is slightly negative, so no consistent monotonic pattern exists.
- **Valence vs popularity:** no visible trend; the coefficient is effectively zero.
- **Duration vs popularity:** very weak negative association. The x-axis is limited to the 99th percentile (8.67 minutes) so the bulk of tracks is readable; longer tracks remain in the correlation.
- **Loudness vs popularity:** the strongest popularity relationship in the set, but still weak. Louder tracks tend slightly upward in popularity.
- **Acousticness vs popularity:** weak negative; more acoustic tracks are slightly less popular on average.
- **Instrumentalness vs popularity:** weak negative; highly instrumental tracks are slightly less popular on average.
- **Liveness vs popularity:** negligible.
- **Tempo vs popularity:** negligible.
- **Energy vs danceability:** moderate positive relationship; higher-energy tracks tend to be more danceable, with wide spread.

## 4. Correlation heatmaps

Two heatmaps were generated: Pearson and Spearman. A combined side-by-side image is also saved as `correlation_heatmap.png`.

### Important positive relationships between audio features

- Energy and loudness: Pearson **0.801**, Spearman **0.774** - very strong.
- Danceability and valence: Pearson **0.632**, Spearman **0.595** - strong.
- Energy and valence: Pearson **0.526**, Spearman **0.483** - strong.
- Energy and danceability: Pearson **0.466**, Spearman **0.360** - moderate.

### Important negative relationships between audio features

- Energy and acousticness: Pearson **-0.643**, Spearman **-0.612** - strong negative.
- Loudness and instrumentalness: Pearson **-0.555**, Spearman **-0.469** - strong negative.
- Loudness and acousticness: Pearson **-0.481**, Spearman **-0.483** - moderate/strong negative.
- Danceability and instrumentalness: Pearson **-0.430**, Spearman **-0.218** - moderate negative.
- Valence and instrumentalness: Pearson **-0.430**, Spearman **-0.294** - moderate negative.

### Relationships with popularity

The largest absolute popularity correlation is **loudness (Pearson 0.201, Spearman 0.204)**, followed by **energy (0.147 / 0.131)**, **acousticness (-0.138 / -0.120)**, and **instrumentalness (-0.127 / -0.089)**. All are weak. The remaining popularity correlations are negligible.

**Why Pearson and Spearman can differ:** popularity is heavily zero-inflated - **17,698 tracks (28.4% of cleaned rows) have popularity 0**. Pearson can be sensitive to that spike. When the two methods disagree in sign, as they mildly do for danceability and valence, the safer conclusion is that there is no consistent monotonic pattern.

**Limitation:** pairwise correlations do not control for language, release year, artist fame, playlist exposure, or platform access. They are descriptive, not causal.

## 5. Popularity by language

| Language | Track count | Mean popularity | Median popularity |
|---|---:|---:|---:|
| English | 23,389 | 14.76 | 5 |
| Hindi | 5,740 | 18.20 | 11 |
| Tamil | 12,609 | 11.91 | 3 |
| Korean | 6,893 | 27.55 | 26 |
| Telugu | 321 | 14.32 | 9 |
| Malayalam | 282 | 7.32 | 2 |
| Unknown | 13,005 | 12.26 | 4 |

**Reading:** Korean tracks have the highest centre (median 26, mean 27.55). Malayalam (median 2, mean 7.32) and Tamil (median 3, mean 11.91) have the lowest medians. The groups are very uneven in size, and they differ in catalogue composition, artists, years, and likely regional listener coverage. The pattern describes this dataset; it does not show that language causes popularity.

## 6. Popularity by musical categories

### Key

| Key | Track count | Mean popularity | Median popularity |
|---|---:|---:|---:|
| C | 8,101 | 15.55 | 7 |
| C#/Db | 5,744 | 16.01 | 7 |
| D | 6,832 | 14.92 | 7 |
| D#/Eb | 1,636 | 16.40 | 8 |
| E | 4,879 | 15.07 | 6 |
| F | 6,411 | 13.92 | 4 |
| F#/Gb | 3,655 | 15.85 | 6 |
| G | 6,956 | 15.10 | 7 |
| G#/Ab | 3,735 | 15.79 | 7 |
| A | 5,862 | 15.55 | 7 |
| A#/Bb | 3,920 | 15.74 | 8 |
| B | 4,473 | 15.96 | 7 |

Key means range only from **13.92** (F) to **16.40** (D#/Eb). The boxes overlap heavily, so key alone shows little separation.

### Mode

| Mode | Track count | Mean popularity | Median popularity |
|---|---:|---:|---:|
| Major | 36,511 | 15.14 | 6 |
| Minor | 25,693 | 15.68 | 7 |

Major and minor distributions are very similar. The minor group is marginally higher, but the difference is small and the boxes overlap.

### Time signature

| Time signature | Track count | Mean popularity | Median popularity |
|---|---:|---:|---:|
| 4/4 | 53,260 | 15.95 | 7 |
| 3/4 | 7,065 | 12.20 | 4 |
| 5/4 | 1,000 | 11.38 | 3 |
| 1/4 | 856 | 9.62 | 3 |
| 0/4 | 23 | 7.30 | 0 |

4/4 is both the most common signature and the highest-average category in this dataset. Rarer signatures have lower averages, but their groups are much smaller and may differ in catalogue composition. The 0/4 group has only 23 tracks, so its average is unstable.

## 7. Top 10 and bottom 10 tracks

**Reproducible tie-break rule:** sort by popularity, then release year (earlier first), then track name, artist name, and finally `track_id`. The selected rows are stored in `outputs/tables/MEMBER2_TOP_BOTTOM_TRACKS.csv`.

### Top 10

| Rank | Track | Artist | Year | Popularity |
|---:|---|---|---:|---:|
| 1 | Big Dawgs | Hanumankind, Kalmi | 2024 | 93 |
| 2 | Starboy | The Weeknd, Daft Punk | 2016 | 91 |
| 3 | Blinding Lights | The Weeknd | 2020 | 91 |
| 4 | Bye Bye Bye - From Deadpool and Wolverine Soundtrack | *NSYNC | 2000 | 90 |
| 5 | cardigan | Taylor Swift | 2020 | 89 |
| 6 | Anti-Hero | Taylor Swift | 2022 | 89 |
| 7 | Locked out of Heaven | Bruno Mars | 2012 | 88 |
| 8 | Counting Stars | OneRepublic | 2013 | 88 |
| 9 | Something Just Like This | The Chainsmokers, Coldplay | 2017 | 88 |
| 10 | august | Taylor Swift | 2020 | 88 |

### Bottom 10

**17,698 tracks share popularity 0**, so no unique "bottom 10" exists. The table below is a reproducible representative selection (earlier years first, then names).

| Rank | Track | Artist | Year | Popularity |
|---:|---|---|---:|---:|
| 1 | Intro to Travelin' Prayer - Live April 1972 At Sigma Sound Studios, WMMR Radio, Philadelphia, PA | Billy Joel | 1973 | 0 |
| 2 | Bhadrakali Theme - Instrumental | Ilaiyaraaja | 1976 | 0 |
| 3 | Chendoora Poove (From "Pathainaru Vayathinile") | S. Janaki, Ilaiyaraaja, Gangai Amaran | 1977 | 0 |
| 4 | Maanodum Paathayile | Ilaiyaraaja, P. Susheela | 1977 | 0 |
| 5 | Sugamo Aayiram (From "Thunaiyiruppal Meenakshi") | P. Susheela, Ilaiyaraaja | 1977 | 0 |
| 6 | Udhayam Varugindradhe | Ilaiyaraaja, S. Janaki, G. K. Venkatesh | 1977 | 0 |
| 7 | Adi Aatha | Ilaiyaraaja | 1978 | 0 |
| 8 | Siritthal Sirippaen (From "Mariyamman Thiruvizha") | T. M. Soundararajan, Ilaiyaraaja | 1978 | 0 |
| 9 | Veenai Meettum (From "Vazha Ninaithal Vazhalam") | S. Janaki, Ilaiyaraaja | 1978 | 0 |
| 10 | Enna Paattu Paada | Ilaiyaraaja | 1979 | 0 |

These lists describe the popularity column only. A high score does not prove that audio features caused success, and a zero score does not prove low quality. Popularity can reflect streaming activity, playlist exposure, region, artist fame, catalogue matching, and when the data was collected.

## 8. Key findings

1. **No audio feature is a strong stand-alone predictor of popularity.** The largest absolute popularity correlations are loudness (0.201 / 0.204), energy (0.147 / 0.131), acousticness (-0.138 / -0.120), and instrumentalness (-0.127 / -0.089). All are weak.
2. **Several features are effectively unrelated to popularity:** valence (0.009 / -0.032), liveness (-0.012 / -0.019), tempo (0.028 / 0.019), and duration (-0.040 / -0.054). Danceability is 0.042 with Pearson but -0.015 with Spearman, so its tiny association is inconsistent.
3. **Audio features are more strongly related to each other than to popularity.** Energy vs loudness is 0.801 (Spearman 0.774), energy vs acousticness -0.643 (-0.612), and danceability vs valence 0.632 (0.595). These overlaps matter when interpreting popularity correlations.
4. **Language groups differ descriptively.** Korean has the highest median popularity (26, n = 6,893); Malayalam (2, n = 282) and Tamil (3, n = 12,609) have lower medians. Group composition and size differ, so this is not evidence that language causes popularity.
5. **Key and mode show little separation.** Key means range from 13.92 to 16.40; major and minor medians are 6 and 7. 4/4 time is the most common signature and has the highest mean (15.95), but rare signatures have small groups.
6. **Top and bottom lists are descriptive, not causal.** The top score is 93; the bottom list is one reproducible selection from 17,698 tracks tied at 0.
7. **Overall:** bivariate analysis is useful for screening relationships, but it cannot isolate causes. Multivariable analysis and careful controls would be needed before making causal or prescriptive claims.

## 9. Files generated

### Notebook

- `person2_eda.ipynb` - standalone Member 2 bivariate notebook, executed with 0 errors.

### Graphs (`outputs/graphs/bivariate/`)

- `energy_vs_popularity.png`
- `danceability_vs_popularity.png`
- `valence_vs_popularity.png`
- `duration_vs_popularity.png`
- `loudness_vs_popularity.png`
- `acousticness_vs_popularity.png`
- `instrumentalness_vs_popularity.png`
- `liveness_vs_popularity.png`
- `tempo_vs_popularity.png`
- `energy_vs_danceability.png`
- `correlation_heatmap.png` (Pearson and Spearman side by side)
- `correlation_heatmap_pearson.png`
- `correlation_heatmap_spearman.png`
- `popularity_by_language.png`
- `popularity_by_key.png`
- `popularity_by_mode.png`
- `popularity_by_time_signature.png`
- `top_10_tracks_by_popularity.png`
- `bottom_10_tracks_by_popularity.png`

### Tables (`outputs/tables/`)

- `MEMBER2_CORRELATION_RESULTS.csv` - 55 unique pairs, with Pearson r, Spearman r, and valid n.
- `MEMBER2_GROUP_COMPARISON.csv` - language, key, mode, and time-signature summaries.
- `MEMBER2_TOP_BOTTOM_TRACKS.csv` - selected top 10 and bottom 10 rows with the tie-break rule.

## 10. Verification notes

- All bivariate code cells executed successfully in `person2_eda.ipynb` with **0 error outputs**.
- All required graphs were generated.
- Statistical values come from `df_clean`; the original DataFrame was not modified.
- Pairwise valid counts are 62,204 for audio-feature pairs and 62,239 for duration/popularity.
- The main `Spotify_EDA.ipynb` was restored to its previous state; the bivariate analysis lives in the separate `person2_eda.ipynb`.
- Correlation results are observational. They do not prove causation.
