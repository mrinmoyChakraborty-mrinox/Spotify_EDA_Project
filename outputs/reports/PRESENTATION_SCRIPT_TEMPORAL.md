# Presenter Script — Temporal Analysis (6 charts)

Purpose: spoken script for the six charts that carry the temporal story.
Target: ~8 minutes (opening 20 s + 6 × ~70 s + closing 30 s).
Every number below was recomputed from `data/processed/cleaned_spotify_tracks.csv`
(62,239 rows, 1971–2024). Nothing here is new analysis — it is the same data the
charts show.

Charts covered:

1. `yearly_track_count.png` — coverage by year
2. `yearly_average_popularity.png` — average popularity + sample-size warning
3. `yearly_average_valence.png` — mood trend
4. `popular_duration_by_decade.png` — hit length
5. `popular_acousticness_instrumentalness_by_year.png` — acoustic collapse
6. `energy_danceability_correlation_by_decade.png` — features became coupled

To swap a chart, keep the block structure: **point → number → meaning → caveat**.

---

## Opening (20 seconds, before the first chart)

> "This section is about time. We have 62,239 tracks released between 1971 and
> 2024 — 54 years. The question is simple: as the years pass, do the songs
> change? I'll show six charts. For each one I'll give you the number, what it
> means in plain language, and the one caveat that keeps us honest."

---

## 1. Track counts by release year — `yearly_track_count.png` (~60 s)

**Point at:** the two ends of the x-axis — 1976 and 2023.

**Say:**

> "Start with how much data sits behind each year, because that shapes
> everything after it.
>
> In 1976 the dataset has **9 tracks**. In 2023 it has **6,427**. Seven years in
> the 1970s and 1980s have fewer than 30 tracks — so thin that a single song can
> move the year's average.
>
> This is not a chart about music. It's a chart about coverage. Whenever a later
> slide says 'average for 1975', remember it's an average of a handful of songs,
> not of the year's real output."

**Numbers:** 62,239 rows; 1971–2024; max 2023 = 6,427; min 1976 = 9; 2022 =
5,181; 2024 = 5,471; years under 30 tracks: 1971, 1972, 1974, 1975, 1976, 1978,
1980.

**If asked "why so few old tracks?"** → the collection is a sample, not a
complete archive; the dataset does not document how tracks were selected.

**If asked about 2024** → treat the last bar as incomplete; 5,471 is below 2023,
which is a coverage effect, not a drop in releases.

**Transition:** "So if we average popularity by year, we have to read it
carefully."

---

## 2. Average popularity by release year — `yearly_average_popularity.png` (~75 s)

**Point at:** the faded grey points on the left, then the solid green line from
1977 onward.

**Say:**

> "Popularity is Spotify's 0–100 score, captured when the data was scraped —
> it is not a chart position or sales number.
>
> The grey dots are years with fewer than 30 tracks. The highest dot looks
> dramatic — **39.3 in 1976** — but that year has **nine songs**. Among years we
> can actually trust, the peak is **34.5 in 1977**, on 39 tracks.
>
> The lowest year is **7.9 in 1992**, on 405 tracks. Since then it sits roughly
> between 10 and 20.
>
> The honest reading: older tracks score higher in this file. But popularity is
> partly a function of age and how long a track has had to accumulate plays — so
> this is a description of the dataset, not evidence that music got worse."

**Numbers:** max all years 39.33 (1976, n=9); reliable max 34.46 (1977, n=39);
min 7.90 (1992, n=405).

**If asked "is the decline real?"** → "Partly an age/catalogue effect we cannot
separate with this data. We report the pattern, we don't claim the cause."

**Transition:** "Popularity is one number. Let's look at what the audio itself
says — starting with mood."

---

## 3. Average valence by release year — `yearly_average_valence.png` (~70 s)

**Point at:** the high plateau 1982–1987, then trace the line down to 2021.

**Say:**

> "Valence is Spotify's estimate of how positive a track sounds — brighter,
> happier, more upbeat. It's an audio estimate, not a listener survey.
>
> The mid-1980s are the brightest stretch: **0.726 in 1987**. After 1988 the
> line steps down, and by **2021 it's 0.450** — the lowest reliable value in the
> file. The drop is not one bad year; it's a steady decline with short rebounds.
>
> Two caveats. The low point at the far left is a year with almost no data, so
> it's faded out. And the mix of languages and genres changes over time, so part
> of this could be a change in what got included, not a change in music."

**Numbers:** 0.726 (1987) → 0.450 (2021); reliable years only; 1971's 0.397 is
n<30 and faded.

**If asked "does that mean music is sadder?"** → "The scores say the tracks
sound less positive. Why is outside this dataset."

**Transition:** "Mood is abstract. Let's use something everyone can feel —
length."

---

## 4. Popular-track duration by decade — `popular_duration_by_decade.png` (~65 s)

**Point at:** the green median dots, then the 1990s bar, then the 2020s bar.

**Say:**

> "This chart only uses popular tracks — popularity 26 or higher, which is
> **16,051 tracks**, about a quarter of the data.
>
> The dot is the median; the bar is the middle half, from the 25th to the 75th
> percentile. The median runs **4.08, 4.51, 4.85, 4.44, 3.90, 3.47** minutes
> from the 1970s to the 2020s. The 1990s are the longest; the 2020s are the
> shortest — about **1.4 minutes shorter** than the peak.
>
> That is a real, visible shift, but the chart doesn't tell us why. Streaming,
> playlist formats, and how hits are written all changed at the same time. We
> describe the pattern; we don't claim one cause."

**Numbers:** medians 4.08 / 4.51 / 4.85 / 4.44 / 3.90 / 3.47; popular n=16,051
(25.8%); threshold 26.0.

**If asked "why 26?"** → "It's the popularity cut-off we used to define the
popular subset; it's a choice, not a natural boundary, and it's stated on the
slide."

**Transition:** "Shorter — and less acoustic."

---

## 5. Acousticness and instrumentalness — `popular_acousticness_instrumentalness_by_year.png` (~75 s)

**Point at:** the left panel first (acousticness), then the right panel
(instrumentalness spikes).

**Say:**

> "Same popular subset, two panels.
>
> Acousticness estimates how much a track sounds unplugged. In **1971 it's
> 0.83**, it dips to **0.135 in 1975**, climbs back to **0.830 by 1988**, and
> then falls away — after 2000 it settles around **0.28**. The 1980s are the
> last time popular tracks were genuinely acoustic-heavy.
>
> Instrumentalness is the chance a track has no vocals. On this chart it's
> near zero almost everywhere — popular tracks are sung. There are isolated
> spikes, the largest **0.272 in 1991**, but they don't form a trend.
>
> Faint dots mark years with fewer than 10 valid tracks, so the early swings are
> built on thin data."

**Numbers:** acousticness 0.826 (1971), 0.830 (1988), 0.135 (1975), ≈0.28 after
2000; instrumentalness max 0.272 (1991).

**If asked "why the 1991 spike?"** → "A small set of instrumental tracks in one
year; one year is not a trend and the slide says so."

**Transition:** "So the sound changed. Do the features still relate to each
other the same way?"

---

## 6. Energy–danceability correlation by decade — `energy_danceability_correlation_by_decade.png` (~85 s)

**Point at:** the dip in the 1980s, the steep climb through the 1990s, the peak
in the 2000s, then the gentle decline.

**Say:**

> "This is the most interesting result in the section. Pearson r measures how
> tightly two features move together across tracks in a decade — plus one means
> they rise and fall together, zero means no linear relationship. It is not a
> causal statement.
>
> In the 1970s r is **0.199**, in the 1980s it's **0.116** — essentially
> unrelated. Then it jumps: **0.474 in the 1990s**, peaks at **0.552 in the
> 2000s**, and eases to **0.497** in the 2010s and **0.449** in the 2020s.
>
> Plain language: in older recordings a song could be energetic without being
> danceable — think guitar rock. From the 1990s on, production made 'energetic'
> and 'danceable' describe more of the same tracks — beat-driven pop and
> electronic music.
>
> The sample is also much larger after 2000 — 7,000 to 25,000 tracks per decade
> versus 232 in the 1970s — so the modern values are the most stable."

**Numbers:** 0.199 (1970s, n=232), 0.116 (1980s, n=1,863), 0.474 (1990s,
n=3,738), 0.552 (2000s, n=7,144), 0.497 (2010s, n=25,442), 0.449 (2020s,
n=23,785).

**If asked "does that mean modern music is all the same?"** → "No. It means the
two features co-move more. Similarity in two dimensions is not sameness overall."

**Transition:** "Six charts, one story: the dataset's coverage is uneven, the
sound shifted — less acoustic, shorter hits, less positive — and the audio
features became more tightly linked. All descriptive. Next, [teammate section]."

---

## Closing (30 seconds)

> "Two things to take away. First, coverage drives what we can see: 9 tracks in
> 1976 versus 6,427 in 2023, and that shapes every average. Second, the trends
> are consistent — less acoustic, shorter popular tracks, lower valence, and a
> much stronger energy–danceability link from the 1990s on.
>
> These are patterns in an observational sample. They are useful for asking
> better questions, not for claiming that a feature causes a hit."

---

## Defence sheet — exact values if challenged

| Claim | Value | Basis |
|---|---|---|
| Rows / years | 62,239 / 1971–2024 | cleaned CSV |
| Busiest / emptiest year | 6,427 (2023) / 9 (1976) | counts |
| Years under 30 tracks | 1971, 1972, 1974, 1975, 1976, 1978, 1980 | counts |
| Popularity max (raw) | 39.33 (1976, n=9) | mean, all years |
| Popularity max (reliable) | 34.46 (1977, n=39) | mean, n ≥ 30 |
| Popularity min | 7.90 (1992, n=405) | mean |
| Valence | 0.726 (1987) → 0.450 (2021) | mean, n ≥ 30 |
| Popular-track duration medians | 4.08 / 4.51 / 4.85 / 4.44 / 3.90 / 3.47 min | median, popularity ≥ 26 |
| Popular subset size | 16,051 (25.8%) | threshold 26.0 |
| Acousticness (popular) | 0.826 (1971), 0.830 (1988), 0.135 (1975), ≈0.28 post-2000 | mean |
| Instrumentalness (popular) | max 0.272 (1991) | mean |
| Energy–danceability r | 0.199 / 0.116 / 0.474 / 0.552 / 0.497 / 0.449 | Pearson, complete pairs |

---

## If you only have 3 minutes

Say slides **1 → 4 → 6** (coverage → shorter hits → features coupled), 45 seconds
each, then the closing. Those three carry the most information per minute.

## If you want two more slides later

- **Energy & Danceability (popular subset)** — `popular_energy_danceability_by_year.png`:
  "For hits, median energy runs about 0.30 in 1971 up to 0.71 recently; median
  danceability about 0.45 in 1975 up to 0.75 in 1979, then a slow drift." Use it
  to answer "does this hold for popular tracks too?"
- **Language composition** — `language_share_by_year.png`: "English is 100% of
  labelled tracks in 1971 and 61.5% by 2024; Korean appears after 2011; the
  Unknown band grows because many Indian film tracks were never language-tagged
  upstream." Only add if the audience asks about catalogue mix.
