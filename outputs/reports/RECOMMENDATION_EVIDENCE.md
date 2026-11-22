# Evidence-Based Recommendations

These recommendations are proposals for testing. The data are observational; none of the associations show that an audio feature or language causes popularity.

                                     Finding                                                                                                                       Evidence                                                                                                Recommendation
          Popularity correlation with energy                                                         Pearson r = 0.147; n=62,204 paired records; unadjusted and descriptive                                       Treat the feature as a creative test variable, not a formula for a hit.
    Popularity correlation with danceability                                                         Pearson r = 0.042; n=62,204 paired records; unadjusted and descriptive                                       Treat the feature as a creative test variable, not a formula for a hit.
         Popularity correlation with valence                                                         Pearson r = 0.009; n=62,204 paired records; unadjusted and descriptive                                       Treat the feature as a creative test variable, not a formula for a hit.
Popularity correlation with instrumentalness                                                        Pearson r = -0.127; n=62,204 paired records; unadjusted and descriptive                                       Treat the feature as a creative test variable, not a formula for a hit.
    Popularity correlation with acousticness                                                        Pearson r = -0.138; n=62,204 paired records; unadjusted and descriptive                                       Treat the feature as a creative test variable, not a formula for a hit.
                    Language segment: Korean                                                           n=6,893; average popularity=27.55; median=26.0; average energy=0.759                         Research each audience and compare like-for-like releases before reallocating effort.
                     Language segment: Hindi                                                           n=5,740; average popularity=18.20; median=11.0; average energy=0.654                         Research each audience and compare like-for-like releases before reallocating effort.
                    Language segment: Telugu                                                              n=321; average popularity=14.32; median=9.0; average energy=0.670                         Research each audience and compare like-for-like releases before reallocating effort.
                 Language segment: Malayalam                                                               n=282; average popularity=7.32; median=2.0; average energy=0.675                         Research each audience and compare like-for-like releases before reallocating effort.
                    Dataset metadata quality 0 missing cells; 78 exact repeated rows; 35 all-feature sentinel records; language categories include Unknown (13,005 tracks).                  Add validation checks and a documented review queue for missing language and audio features.
             Release-year coverage is uneven                                  2023 has 6,427 records while 1976 has 9; years before 1982 usually have fewer than 30 tracks. Use year trends as context and plan release timing with current audience data, not historical averages alone.

## Priority by timing

### Immediate

- Validate incoming data for exact duplicates and the confirmed -1 / -100000 sentinel pattern.
- Include sample size and median alongside averages in team charts.
- Keep audio-feature correlations as context rather than production targets.

### Short-term

- Run small, controlled arrangement or marketing tests with a pre-defined comparison group and success metric.
- Research language segments locally; compare multiple releases and include Unknown records in data-quality work.
- Pair release-calendar decisions with current audience and campaign information.

### Long-term

- Improve metadata completeness and track data provenance across refreshes.
- Build repeatable experiments that can separate audience response from artist reach, promotion, and release age.
- Revisit findings as newer data and more representative samples become available.

## Presentation-ready wording

- “Korean-tagged tracks have the highest average popularity in this file (27.55; median 26; n=6,893), but this is a descriptive comparison and does not isolate why.”
- “Energy has a weak positive correlation with popularity (r=0.147); it is not evidence that increasing energy will make a track more popular.”
- “The dataset has 78 exact duplicate rows and 35 records with missing-feature sentinel values; validate metadata before using it for decisions.”
- “Track counts are uneven by year, so historical averages should be treated as context, not a release-success forecast.”
