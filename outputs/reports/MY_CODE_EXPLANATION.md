# My Temporal Analysis Code: Beginner Guide

## What the notebook does

It reads the cleaned CSV, checks its basic structure, groups tracks by release year, calculates counts and yearly averages, saves six charts, and prints sample-size findings. It does not modify the raw data.

## Imports and loading

- `import pandas as pd` loads Pandas and gives it the short name `pd`. Pandas stores the CSV in a table called a DataFrame.
- `import matplotlib.pyplot as plt` loads the plotting functions with the short name `plt`.
- `pd.read_csv('../data/processed/cleaned_spotify_tracks.csv')` reads the original CSV. The `..` means “go up one folder” from `notebooks/`, then enter `data/processed/`.
- `df.head()` shows the first five rows. `df.shape` returns (row count, column count). `df.dtypes` lists each column's data type.

## Checking and preparing years

- `df.isna().sum().sum()` counts missing cells: the first `sum` counts within each column; the second adds those counts together.
- `df.duplicated().sum()` counts repeated full rows. `df['track_id'].duplicated().sum()` checks repeated IDs.
- `pd.to_numeric(..., errors='coerce')` converts the year to a number and would turn unparseable values into missing values. `dropna(subset=['year'])` removes only rows without a usable year. `astype(int)` makes the year a whole number.

## Grouping by year

- `df.groupby('year')` makes a group for each year.
- `['track_id'].count()` counts tracks in each year. `sort_index()` orders years from earliest to latest.
- `groupby(...).agg(...)` calculates several summaries together. `mean` is the arithmetic average; `median` is the middle value after sorting. `track_count` tells how many rows are behind each yearly result.
- `df.groupby('year')['energy'].mean()` calculates one average energy value for each year. The danceability and valence lines do the same for those columns.

## Making and saving graphs

- `plt.figure(figsize=(12, 5))` sets the graph's size. `plt.bar` makes the count bars. `plt.plot` makes lines; `marker='o'` adds a dot for each observed year.
- `plt.xlabel`, `plt.ylabel`, and `plt.title` label the axes and graph. `plt.grid` adds a light grid.
- `plt.savefig(..., dpi=150)` writes a clear PNG to the output folder. `plt.show(block=False)` displays it in Jupyter; `plt.close()` closes the current figure before the next one.
- `minimum_tracks = 30` sets a display threshold. `yearly_track_count >= minimum_tracks` identifies years meeting it. Years below 30 are still in the calculations, but the connected line focuses on years with more observations. If the threshold changes, the line and normalized comparison include a different set of years.

## Combined normalized graph

The three features are put in a small table, filtered to years meeting the sample threshold, then each feature is converted to a 0-to-1 range using `(value - minimum) / (maximum - minimum)`. This lets the reader compare the shapes of the lines. The result is not the original energy, danceability, or valence scale, so it cannot be read as a real feature score.

## Conclusions and limitations

A yearly average describes tracks in this file. It does not prove that release year caused the audio feature or popularity to change. Years have different track counts, and factors such as artist reach, promotion, genre, and the age of a track are not controlled.

## Viva questions and short answers

1. **What does `groupby` do?** It separates rows into groups that share a value, here the release year.
2. **Why show the median popularity too?** The median is less affected by a few very high values than the mean.
3. **Why include track count?** It shows how many rows support each yearly average.
4. **What does valence mean?** It is an audio-based estimate of how positive or happy the music sounds, not a direct measure of a listener's mood.
5. **Why sort the year index?** To display the results in chronological order.
6. **What does a line point represent?** The average for tracks in that release year.
7. **Why mark years with fewer than 30 tracks?** Their averages may be less stable, so the graph treats them cautiously.
8. **Does a positive correlation prove a feature causes popularity?** No. Correlation describes association and does not establish cause.
9. **What happens if `minimum_tracks` changes?** The set of highlighted years and the combined-chart year range changes.
10. **Why normalize the combined features?** It allows a shape comparison on one plot; it removes the original units and values.
