# Speaker Script — Spotify Tracks EDA

**Deck:** `Spotify_EDA_Presentation.pptx`  
**Length:** ~10–11 minutes at a measured pace  
**Audience:** classmates, instructor, and project reviewers  
**Core message:** Audio features describe sound, but they do not explain popularity strongly. Use the evidence to ask better questions and run better tests.

> If you have only five minutes: present slides 1, 2, 5, 7, 10, 14, 15, and 17.

## Slide 1 — Title (0:00–0:35)

Good morning. This is our exploratory analysis of 62,239 Spotify tracks. We asked a simple question: do audio features explain popularity? The short answer is that they do not explain it very well. But the data still tells a useful story about catalogue composition, feature overlap, language segments, and time.

## Slide 2 — The brief (0:35–1:10)

We focused on three questions. First, what is in the data? Second, which audio, duration, and language signals travel with popularity? Third, what should a creator or platform do differently? We treated the work as descriptive evidence. The deck deliberately separates what the data shows from what it cannot prove.

## Slide 3 — Dataset (1:10–1:50)

The raw file has 62,317 rows and 22 columns, spanning 1971 to 2024. After removing 78 exact duplicates, 62,239 records remain. There are 12 audio features, plus metadata, popularity, year, and URLs. Language is uneven: English is largest at 23,389, but Unknown is 13,005 and Tamil is 12,609. Korean is 6,893. Those denominators matter for every group comparison later.

## Slide 4 — Cleaning and method (1:50–2:30)

We did not overwrite the raw file. We removed exact duplicates, flagged 35 records with a shared −1 and −100,000 sentinel pattern, and set those 420 feature values to missing rather than imputing them. So the analysis copy is clean but honest: the metadata stays, and the invalid audio values are treated as unknown. We also treat correlations as associations, not causal effects.

## Slide 5 — Popularity distribution (2:30–3:10)

Popularity is not a bell curve. The median track is 7 out of 100. The mean is 15.4. And 28.4 percent of tracks are at zero. Only a handful reach the 80s and 90s. That long tail is the outcome we are trying to understand. Any model or recommendation has to respect the fact that most tracks are not hits.

## Slide 6 — Audio features (3:10–3:45)

The typical track is moderately energetic and danceable. Energy and danceability medians are about .64 and .63. Acousticness is .29, and instrumentalness is effectively zero for most tracks. These are catalogue averages. They describe the supplied sample, not the listening preferences of Spotify users.

## Slide 7 — Bivariate relationships (3:45–4:35)

Here are the four headline pairs. Loudness has the strongest relationship with popularity, but r is only .20. Energy is .15. Danceability is .04, and duration is −.04. Even the strongest scatter is a cloud, not a line. Energy explains roughly two percent of popularity variation. This is the core negative result of the project.

## Slide 8 — Correlation heatmap (4:35–5:20)

The stronger story is among the features themselves. Energy and loudness correlate at .80. Energy and acousticness at −.64. Danceability and valence at .63. Popularity is the pale row: every correlation is .20 or weaker. That means several audio features overlap, so treating one as an independent “hit lever” is misleading.

## Slide 9 — Multivariate view (5:20–6:00)

We also looked at features jointly. This bubble chart puts danceability on the x-axis, energy on the y-axis, colors by valence, and sizes by popularity. The top 10 tracks are ringed. They are more energetic and less acoustic on average, but they do not sit in one corner. Ten tracks cannot establish a rule; the visual is a caution against single-coordinate thinking.

## Slide 10 — Language (6:00–6:45)

Language labels show larger differences. Korean has a median popularity of 26 and a mean of 27.5 across 6,893 tracks. Tamil’s median is 3, and Malayalam’s is 2. That is a large gap in the file. But the groups differ in size, catalogue, era, artist mix, and audience coverage. This is a segmentation clue, not proof that language causes popularity.

## Slide 11 — Temporal coverage (6:45–7:25)

Time is uneven. 2023 contributes 6,427 tracks; 1976 contributes nine. The 1976 average popularity of 39.3 is based on nine tracks. The 1992 low of 7.9 is based on 405. Early-year comparisons are fragile. We show the full range, but we treat annual averages as descriptions of the sampled catalogue, not as a historical forecast.

## Slide 12 — Temporal features (7:25–8:05)

The sound does move. Danceability peaks around 1993, and valence is lower in recent years. Energy is high in the late 1970s and variable afterwards. But this is a cross-section of tracks, not a longitudinal study of the same artists. Use these patterns to generate hypotheses, not to prescribe a sound.

## Slide 13 — Extremes and top tracks (8:05–8:40)

Outliers here are mostly the commercial peaks. Under a 1.5-IQR rule, 1,115 tracks are high-popularity outliers, and 4,021 are loudness outliers. They are review flags, not errors. The top track is Big Dawgs at 93. The top 10 are all English in this file, which is a coverage fact, not a quality ranking.

## Slide 14 — Four findings (8:40–9:20)

Four findings survive scrutiny. One: audio features are weak mirrors of popularity. Two: features are strongly interrelated, so single-feature claims are unstable. Three: language segments differ, but are confounded. Four: the dataset itself has a shape — zero inflation and uneven years. The evidence supports hypotheses, not a formula.

## Slide 15 — Recommendations (9:20–10:05)

Three actions. First, test, don’t copy. Treat energy and loudness as hypotheses in controlled creative or release tests, with saves, completion, and repeat listens as outcomes. Second, segment before comparing: report medians and sample sizes by language, and control for artist, year, and promotion. Third, build a better dataset: timestamp popularity, capture playlist and region, and join artist-level metadata.

## Slide 16 — Limitations (10:05–10:40)

What we cannot claim: popularity is current, not lifetime; we lack promotion, playlist, artist fame, and region; language labels are incomplete; and this is observational. The next pass should add longitudinal popularity and a model with controls. That would turn a description into a stronger test.

## Slide 17 — Close (10:40–11:00)

The takeaway is simple: start with the signal, then test the rest. Audio features tell us what a track sounds like; they do not tell us why it becomes a hit. Thank you — we are happy to take questions.

## Q&A prep

**“So what actually drives popularity?”**  
In this dataset, unobserved factors dominate. Loudness is the strongest audio correlate at r = .20, but that is weak and likely entangled with genre, production era, artist, and audience. Promotion, playlist placement, artist fame, and region are not in the file.

**“Why not just make every track high-energy?”**  
Because energy explains about two percent of popularity variation, and the top tracks are not tightly clustered. A weak average relationship is not a production recipe. Test changes against real outcomes.

**“Isn’t Korean just more popular?”**  
Korean has the highest median in this file, but the group differs in size, catalogue, era, artists, and audience coverage. The comparison is descriptive. A controlled model or market-level test is the next step.

**“Why keep the 35 invalid rows?”**  
Their metadata is still usable, and dropping rows would silently change the sample. We mark only the invalid audio values as missing, and we report the missingness.

**“Is popularity a fair outcome measure?”**  
It is the outcome supplied in the data, but it is current and platform-defined. It is not lifetime streams, revenue, or artistic quality. That is a core limitation.
