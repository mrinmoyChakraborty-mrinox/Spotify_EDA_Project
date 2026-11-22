# Dataset Profile

## Source

The raw CSV and data dictionary were cloned from [Adrija-verse/EDA_Project1_SpotifyTracks](https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks), then copied unchanged into `data/raw/` and `data/metadata/`. The source CSV is preserved.

## Shape and quality

- Rows and columns: **62,317 x 22**.
- Missing cells in the original: **0**.
- Exact duplicate rows: **78**.
- Duplicate track IDs: **78**. These duplicate rows are exact repeats.
- Year range: **1971 to 2024**.
- Languages: **7** categories, including `Unknown`.
- 35 rows contain -1 in every audio feature and categorical audio code listed in the dictionary; the same rows use loudness -100,000 dB (35 rows). Treat these values as missing extraction results.
- There are **30** tracks longer than 30 minutes. These are flagged for review, not removed, because duration alone does not prove an error.

## Numeric summary

                    count        mean         50%       min          max
year              62317.0    2014.426    2017.000    1971.0     2024.000
popularity        62317.0      15.358       7.000       0.0       93.000
acousticness      62317.0       0.362       0.286      -1.0        0.996
danceability      62317.0       0.597       0.631      -1.0        0.986
duration_ms       62317.0  242527.040  236267.000    5000.0  4581483.000
energy            62317.0       0.602       0.639      -1.0        1.000
instrumentalness  62317.0       0.146       0.000      -1.0        0.999
key               62317.0       5.102       5.000      -1.0       11.000
liveness          62317.0       0.194       0.125      -1.0        0.998
loudness          62317.0     -65.103      -7.506 -100000.0        1.233
mode              62317.0       0.586       1.000      -1.0        1.000
speechiness       62317.0       0.088       0.049      -1.0        0.959
tempo             62317.0     117.931     117.991      -1.0      239.970
time_signature    62317.0       3.857       4.000      -1.0        5.000
valence           62317.0       0.495       0.507      -1.0        0.995

## Year and language coverage

The most represented year is **2023** (6,427 tracks); the least represented year is **1976** (9 tracks). English has 23,389 tracks (37.6% of rows); `Unknown` has 13,005.

## Cleaning decisions

`cleaned_spotify_tracks.csv` removes exact duplicate rows and replaces only the confirmed invalid sentinel measurements with missing values. It does not fill missing values, trim durations, remove statistical outliers, or change the raw file. This keeps questionable observations available for review while preventing impossible sentinel values from distorting feature summaries.

The supplied dictionary describes several Spotify audio-feature fields as spanning -1 to 1. In this file, -1 appears simultaneously across all measured audio features, key, mode, time signature, and loudness for the same records. That shared pattern is evidence of a missing-data sentinel. Recheck this assumption with the instructor or dataset owner if a different meaning is intended.
