# Reference Audit

## Resources inspected

Cloned `https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks` into the sibling folder `Spotify_EDA_Reference`. Inspected the README, CSV, data dictionary, 214-cell notebook, and 38-page PDF. The PDF is available locally at `presentation/reference_senior_presentation.pdf`.

## Claims checked against the supplied CSV

- README says 62,317 tracks: **verified** (62,317 rows).
- README says years 1971–2024: **verified**.
- English count of 23,392 / about 37.5%: **verified** (37.6%).
- Korean-tagged mean popularity of 27.55: **verified** (27.55; median 26.0; n=6,893). This alone does not establish success caused by language.
- Energy correlation with popularity of about 0.148: **verified** (Pearson r=0.147). It is weak and observational. Other feature correlations include danceability 0.042, valence 0.009, and acousticness -0.138.

## Claims not independently confirmed

The README's “2,888 outliers”, “5.0x more popular”, feature differences for a high-performance group, “+10 popularity points potential”, “623,170 popularity points impact”, and three emerging language opportunities have no sufficiently clear calculation or definition in the README. They are not repeated as established facts. The senior notebook contains extensive exploratory plots but does not provide a reproducible definition for every executive claim.

## Data-quality differences and caution

The source notebook labels missing values as absent at its initial inspection, but the CSV's invalid extraction values are encoded as -1 in 11 audio/code columns and -100,000 in loudness, so a null-only missing-value count misses 35 affected rows. The dictionary gives several ranges that include -1; the shared all-column sentinel pattern indicates missing extraction results in this file. Confirm that interpretation with the instructor if needed.

## Useful methods retained

Basic DataFrame inspection, group summaries, charts with explicit labels, and presentation flow from objective through recommendations were retained. This project's notebook independently computes its results from the copied CSV and shows sample sizes.

## PDF-specific claims checked

- Page 27 gives 1975 popularity as about 17.5; the supplied CSV gives **37.37** for 1975 (n=19). This is a material disagreement.
- Page 21 describes Korean popularity as narrow and low; the dataset's Korean-tagged tracks have the highest language mean (27.55; median 26.0; n=6,893).
- Page 7 reports “19 features,” while the CSV and data dictionary list 22 columns. The PDF does not explain a different counting convention.
- The PDF recommends increasing energy and copying a “Korean model.” This is not supported as a causal recommendation by the weak observed energy-popularity relationship (r=0.147). The outlier counts also lack enough detail to reproduce confidently.
