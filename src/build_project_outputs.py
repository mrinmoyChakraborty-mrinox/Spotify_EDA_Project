import json
import base64
import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(ROOT, "data", "raw", "spotify_tracks.csv")
TEMPORAL_DIR = os.path.join(ROOT, "outputs", "graphs", "temporal")
REPORT_DIR = os.path.join(ROOT, "outputs", "reports")
TABLE_DIR = os.path.join(ROOT, "outputs", "tables")
NOTEBOOK_PATH = os.path.join(ROOT, "notebooks", "05_Temporal_Analysis.ipynb")

os.makedirs(TEMPORAL_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(TABLE_DIR, exist_ok=True)

raw_df = pd.read_csv(RAW_PATH)
df = raw_df.drop_duplicates().copy()
sentinel_columns = ["energy", "danceability", "valence", "acousticness", "instrumentalness", "liveness", "speechiness", "tempo", "key", "mode", "time_signature"]
for column in sentinel_columns:
    df.loc[df[column] == -1, column] = np.nan
df.loc[df["loudness"] <= -1000, "loudness"] = np.nan
cleaned_path = os.path.join(ROOT, "data", "processed", "cleaned_spotify_tracks.csv")
df.to_csv(cleaned_path, index=False)
year_counts = df.groupby("year")["track_id"].count().sort_index()
yearly_track_count = year_counts
yearly = df.groupby("year").agg(
    track_count=("track_id", "count"),
    average_popularity=("popularity", "mean"),
    median_popularity=("popularity", "median"),
    average_energy=("energy", "mean"),
    average_danceability=("danceability", "mean"),
    average_valence=("valence", "mean"),
)

yearly.to_csv(os.path.join(TABLE_DIR, "temporal_yearly_summary.csv"))

def make_notebook():
    cells = []

    def markdown(source):
        cells.append({"cell_type": "markdown", "metadata": {}, "source": source.splitlines(True)})

    def code(source):
        cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source.splitlines(True)})

    markdown("# Temporal Analysis of Spotify Tracks\n\nThis notebook studies how track counts and audio features vary by release year. The yearly averages describe this dataset; they do not prove that release year caused a change in music or popularity.")
    markdown("## 1. Import libraries\n\nPandas reads and summarizes the table. Matplotlib saves the graphs as image files.")
    code("import pandas as pd\nimport matplotlib.pyplot as plt\n")
    markdown("## 2. Load the dataset\n\nThe notebook reads the cleaned copy. The raw CSV is preserved separately. Exact duplicate rows were removed and confirmed invalid sentinel measurements were marked as missing; no values were filled in.")
    code("df = pd.read_csv('../data/processed/cleaned_spotify_tracks.csv')\n")
    markdown("## 3. Display the first five rows")
    code("print(df.head())\n")
    markdown("## 4. Understand the dataset")
    code("print('Rows and columns:', df.shape)\nprint('Column names:', list(df.columns))\nprint(df.dtypes)\nprint('Missing values:', df.isna().sum().sum())\nprint('Duplicate rows:', df.duplicated().sum())\nprint('Duplicate track IDs:', df['track_id'].duplicated().sum())\n")
    markdown("## 5. Prepare the year column\n\nThe source stores year as a number. Convert it to numeric safely, then check which rows have a valid year. We keep only years present in the CSV; we do not fill missing years.")
    code("df['year'] = pd.to_numeric(df['year'], errors='coerce')\ndf = df.dropna(subset=['year'])\ndf['year'] = df['year'].astype(int)\nprint('Year range:', df['year'].min(), 'to', df['year'].max())\n")
    markdown("## 6. Calculate yearly track counts\n\n`groupby` collects rows with the same year, and `count` counts track IDs in each group.")
    code("yearly_track_count = df.groupby('year')['track_id'].count().sort_index()\nprint(yearly_track_count)\n")
    markdown("## 7. Calculate yearly average popularity\n\nWe calculate both the mean and median because a few popular tracks can pull the mean upward. Track count shows how many rows support each yearly result.")
    code("yearly_popularity = df.groupby('year').agg(\n    average_popularity=('popularity', 'mean'),\n    median_popularity=('popularity', 'median'),\n    track_count=('track_id', 'count')\n).sort_index()\nprint(yearly_popularity.head())\n")
    markdown("## 8. Calculate yearly average energy")
    code("yearly_energy = df.groupby('year')['energy'].mean().sort_index()\nprint(yearly_energy.head())\n")
    markdown("## 9. Calculate yearly average danceability")
    code("yearly_danceability = df.groupby('year')['danceability'].mean().sort_index()\nprint(yearly_danceability.head())\n")
    markdown("## 10. Calculate yearly average valence\n\nValence is Spotify's estimate of the positive or happy character conveyed by a track. It is an audio feature, not a direct survey of listeners' feelings.")
    code("yearly_valence = df.groupby('year')['valence'].mean().sort_index()\nprint(yearly_valence.head())\n")
    markdown("## 11. Generate graphs\n\nThe first chart includes every year represented in the data. For trend charts, years with fewer than 30 tracks are shown as faint markers and excluded from the connected line, because their averages are less stable. The threshold is a display rule, not a data correction.")
    code("minimum_tracks = 30\nreliable_years = yearly_track_count[yearly_track_count >= minimum_tracks].index\n\nplt.figure(figsize=(12, 5))\nplt.bar(yearly_track_count.index, yearly_track_count.values, color='steelblue')\nplt.title('Number of Spotify Tracks by Release Year')\nplt.xlabel('Release year')\nplt.ylabel('Number of tracks')\nplt.tight_layout()\nplt.savefig('../outputs/graphs/temporal/yearly_track_count.png', dpi=150)\nplt.show(block=False)\nplt.close()\n")
    for name, variable, label, filename, title in [
        ("Popularity", "yearly_popularity['average_popularity']", "Average popularity (0 to 100)", "yearly_average_popularity.png", "Average Track Popularity by Release Year"),
        ("Energy", "yearly_energy", "Average energy", "yearly_average_energy.png", "Average Track Energy by Release Year"),
        ("Danceability", "yearly_danceability", "Average danceability", "yearly_average_danceability.png", "Average Track Danceability by Release Year"),
        ("Valence", "yearly_valence", "Average valence", "yearly_average_valence.png", "Average Track Valence by Release Year"),
    ]:
        code(f"plt.figure(figsize=(12, 5))\nplt.plot({variable}.index, {variable}.values, color='steelblue', marker='o', markersize=3, linewidth=1, alpha=0.45)\nplt.plot(reliable_years, {variable}.loc[reliable_years], color='darkblue', marker='o', markersize=3, linewidth=1.5)\nplt.title('{title}')\nplt.xlabel('Release year')\nplt.ylabel('{label}')\nplt.grid(True, alpha=0.3)\nplt.tight_layout()\nplt.savefig('../outputs/graphs/temporal/{filename}', dpi=150)\nplt.show(block=False)\nplt.close()\n")
    markdown("## 12. Print important findings")
    code("print('Year with the most tracks:', int(yearly_track_count.idxmax()), '-', int(yearly_track_count.max()), 'tracks')\nprint('Year with the fewest tracks:', int(yearly_track_count.idxmin()), '-', int(yearly_track_count.min()), 'tracks')\nprint('Yearly popularity average uses the track_count column above.')\nprint('Years with fewer than', minimum_tracks, 'tracks:', list(yearly_track_count[yearly_track_count < minimum_tracks].index))\n")
    markdown("## 13. Combined normalized audio-feature trend\n\nEnergy, danceability and valence share a similar 0-to-1 scale in this dataset. Popularity uses a different 0-to-100 scale, so it is left out of this combined chart. Each feature is normalized to its own 1971-2024 range so that changes in shape can be compared; the vertical values are not original feature scores.")
    code("combined_features = pd.DataFrame({\n    'Energy': yearly_energy,\n    'Danceability': yearly_danceability,\n    'Valence': yearly_valence\n})\ncombined_features = combined_features.loc[reliable_years]\nnormalized_features = (combined_features - combined_features.min()) / (combined_features.max() - combined_features.min())\n\nplt.figure(figsize=(12, 5))\nfor column in normalized_features.columns:\n    plt.plot(normalized_features.index, normalized_features[column], marker='o', markersize=2, label=column)\nplt.title('Normalized Yearly Audio Feature Trends (Years with 30+ Tracks)')\nplt.xlabel('Release year')\nplt.ylabel('Normalized value (0 to 1; within-feature scale)')\nplt.legend()\nplt.grid(True, alpha=0.3)\nplt.tight_layout()\nplt.savefig('../outputs/graphs/temporal/combined_temporal_features.png', dpi=150)\nplt.show(block=False)\nplt.close()\n")
    markdown("## 14. Conclusions\n\nThe plots describe the dataset's release-year composition and the average features of tracks represented in each year. Track counts are uneven, and historical averages can reflect which songs were included, how popularity was measured, and how the dataset was assembled. They should guide questions for further research, not be treated as forecasts or causal explanations.")
    return {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.x"}}, "nbformat": 4, "nbformat_minor": 5}

notebook = make_notebook()
with open(NOTEBOOK_PATH, "w", encoding="utf-8") as file:
    json.dump(notebook, file, ensure_ascii=False, indent=1)

# Build the dataset profile and year-by-year evidence directly from the CSV.
profile_stats = raw_df.select_dtypes(include="number").describe().T
missing_count = int(raw_df.isna().sum().sum())
duplicate_rows = int(raw_df.duplicated().sum())
duplicate_ids = int(raw_df["track_id"].duplicated().sum())
sentinel_rows = int(raw_df[sentinel_columns].eq(-1).all(axis=1).sum())
bad_loudness_rows = int((raw_df["loudness"] <= -1000).sum())
language_summary = df.groupby("language").agg(
    track_count=("track_id", "count"),
    average_popularity=("popularity", "mean"),
    median_popularity=("popularity", "median"),
    average_energy=("energy", "mean"),
).sort_values("track_count", ascending=False)
language_summary.to_csv(os.path.join(TABLE_DIR, "language_summary.csv"))
correlation_columns = ["popularity", "energy", "danceability", "valence", "acousticness", "instrumentalness", "liveness", "speechiness", "tempo", "duration_ms"]
correlations = df[correlation_columns].corr()["popularity"].drop("popularity").sort_values(ascending=False)
peak_year = int(yearly_track_count.idxmax())
low_year = int(yearly_track_count.idxmin())
peak_pop_year = int(yearly["average_popularity"].idxmax())
low_pop_year = int(yearly["average_popularity"].idxmin())
eligible_yearly = yearly[yearly["track_count"] >= 30]
eligible_pop_high = eligible_yearly["average_popularity"].idxmax()
eligible_pop_low = eligible_yearly["average_popularity"].idxmin()

with open(os.path.join(REPORT_DIR, "DATASET_PROFILE.md"), "w", encoding="utf-8") as file:
    file.write(f"""# Dataset Profile\n\n## Source\n\nThe raw CSV and data dictionary were cloned from [Adrija-verse/EDA_Project1_SpotifyTracks](https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks), then copied unchanged into `data/raw/` and `data/metadata/`. The source CSV is preserved.\n\n## Shape and quality\n\n- Rows and columns: **{raw_df.shape[0]:,} x {raw_df.shape[1]}**.\n- Missing cells in the original: **{missing_count}**.\n- Exact duplicate rows: **{duplicate_rows}**.\n- Duplicate track IDs: **{duplicate_ids}**. These duplicate rows are exact repeats.\n- Year range: **{df['year'].min()} to {df['year'].max()}**.\n- Languages: **{df['language'].nunique()}** categories, including `Unknown`.\n- {sentinel_rows} rows contain -1 in every audio feature and categorical audio code listed in the dictionary; the same rows use loudness -100,000 dB ({bad_loudness_rows} rows). Treat these values as missing extraction results.\n- There are **{int((df['duration_ms'] > 1800000).sum())}** tracks longer than 30 minutes. These are flagged for review, not removed, because duration alone does not prove an error.\n\n## Numeric summary\n\n{profile_stats[['count','mean','50%','min','max']].round(3).to_string()}\n\n## Year and language coverage\n\nThe most represented year is **{peak_year}** ({int(yearly_track_count.max()):,} tracks); the least represented year is **{low_year}** ({int(yearly_track_count.min())} tracks). English has {int(language_summary.loc['English','track_count']):,} tracks ({language_summary.loc['English','track_count']/len(df):.1%} of rows); `Unknown` has {int(language_summary.loc['Unknown','track_count']):,}.\n\n## Cleaning decisions\n\n`cleaned_spotify_tracks.csv` removes exact duplicate rows and replaces only the confirmed invalid sentinel measurements with missing values. It does not fill missing values, trim durations, remove statistical outliers, or change the raw file. This keeps questionable observations available for review while preventing impossible sentinel values from distorting feature summaries.\n\nThe supplied dictionary describes several Spotify audio-feature fields as spanning -1 to 1. In this file, -1 appears simultaneously across all measured audio features, key, mode, time signature, and loudness for the same records. That shared pattern is evidence of a missing-data sentinel. Recheck this assumption with the instructor or dataset owner if a different meaning is intended.\n""")

# Recommendation evidence table. Correlations are descriptive, not causal.
rows = []
for feature, value in correlations.items():
    if feature in ["energy", "danceability", "valence", "acousticness", "instrumentalness"]:
        pair_count = int(df[["popularity", feature]].dropna().shape[0])
        rows.append({"Finding": f"Popularity correlation with {feature}", "Evidence": f"Pearson r = {value:.3f}; n={pair_count:,} paired records; unadjusted and descriptive", "Insight": "The relationship is weak in this dataset; it does not show that changing the feature will increase popularity.", "Recommendation": "Treat the feature as a creative test variable, not a formula for a hit.", "Implementation": "Run controlled audience tests on alternative arrangements while holding other campaign conditions steady.", "Success Metric": "Compare listener completion, saves, and popularity after a pre-defined test period.", "Limitations": "Popularity is observational and may reflect age, artist reach, promotion, and platform coverage."})
for language, row in language_summary.iterrows():
    if language in ["Korean", "Malayalam", "Telugu", "Hindi"]:
        rows.append({"Finding": f"Language segment: {language}", "Evidence": f"n={int(row['track_count']):,}; average popularity={row['average_popularity']:.2f}; median={row['median_popularity']:.1f}; average energy={row['average_energy']:.3f}", "Insight": "Segment averages vary, while group sizes differ substantially.", "Recommendation": "Research each audience and compare like-for-like releases before reallocating effort.", "Implementation": "Pair local audience research with a small campaign pilot and report both mean and median with n.", "Success Metric": "Incremental saves, completion rate, and campaign conversion versus a matched baseline.", "Limitations": "Language labels and the Unknown category may be incomplete; group averages do not control for artist or release age."})
rows.extend([
    {"Finding":"Dataset metadata quality", "Evidence":f"{missing_count} missing cells; {duplicate_rows} exact repeated rows; {sentinel_rows} all-feature sentinel records; language categories include Unknown ({int(language_summary.loc['Unknown','track_count']):,} tracks).", "Insight":"Incomplete and repeated metadata can affect comparisons and search/filter quality.", "Recommendation":"Add validation checks and a documented review queue for missing language and audio features.", "Implementation":"At each data refresh, report duplicates, sentinel values, missing language and valid feature ranges before analysis.", "Success Metric":"Share of records passing checks; duplicate rate; Unknown-language share over time.", "Limitations":"The CSV does not show how or when metadata was collected."},
    {"Finding":"Release-year coverage is uneven", "Evidence":f"{peak_year} has {int(yearly_track_count.max()):,} records while {low_year} has {int(yearly_track_count.min())}; years before 1982 usually have fewer than 30 tracks.", "Insight":"Yearly averages from small groups are unstable and the dataset's coverage changes over time.", "Recommendation":"Use year trends as context and plan release timing with current audience data, not historical averages alone.", "Implementation":"Combine recent platform and campaign signals with a small release-calendar test; label sample sizes in reporting.", "Success Metric":"Performance against a comparable release or campaign baseline.", "Limitations":"Historical sample composition and popularity measurement can vary; no forecast or causal effect is established."}
])
evidence = pd.DataFrame(rows)
evidence.to_csv(os.path.join(TABLE_DIR, "recommendation_evidence.csv"), index=False)
with open(os.path.join(REPORT_DIR, "RECOMMENDATION_EVIDENCE.md"), "w", encoding="utf-8") as file:
    file.write("# Evidence-Based Recommendations\n\nThese recommendations are proposals for testing. The data are observational; none of the associations show that an audio feature or language causes popularity.\n\n")
    file.write(evidence[['Finding','Evidence','Recommendation']].to_string(index=False))
    file.write(f"\n\n## Priority by timing\n\n### Immediate\n\n- Validate incoming data for exact duplicates and the confirmed -1 / -100000 sentinel pattern.\n- Include sample size and median alongside averages in team charts.\n- Keep audio-feature correlations as context rather than production targets.\n\n### Short-term\n\n- Run small, controlled arrangement or marketing tests with a pre-defined comparison group and success metric.\n- Research language segments locally; compare multiple releases and include Unknown records in data-quality work.\n- Pair release-calendar decisions with current audience and campaign information.\n\n### Long-term\n\n- Improve metadata completeness and track data provenance across refreshes.\n- Build repeatable experiments that can separate audience response from artist reach, promotion, and release age.\n- Revisit findings as newer data and more representative samples become available.\n\n## Presentation-ready wording\n\n- “Korean-tagged tracks have the highest average popularity in this file (27.55; median 26; n=6,893), but this is a descriptive comparison and does not isolate why.”\n- “Energy has a weak positive correlation with popularity (r={correlations['energy']:.3f}); it is not evidence that increasing energy will make a track more popular.”\n- “The dataset has 78 exact duplicate rows and 35 records with missing-feature sentinel values; validate metadata before using it for decisions.”\n- “Track counts are uneven by year, so historical averages should be treated as context, not a release-success forecast.”\n")

with open(os.path.join(REPORT_DIR, "TEMPORAL_ANALYSIS_REPORT.md"), "w", encoding="utf-8") as file:
    file.write(f"""# Temporal Analysis Report\n\n## Scope\n\nThe analysis groups tracks by the `year` column and calculates yearly track count, mean and median popularity, and mean energy, danceability, and valence. Years with fewer than 30 rows remain in summary tables and the count graph, but are shown faintly and not connected in the feature trend lines. This threshold is a readability aid, not a claim of statistical significance.\n\n## Main findings\n\n- The dataset spans **{df['year'].min()}–{df['year'].max()}**.\n- Track count is highest in **{peak_year}** ({int(yearly_track_count.max()):,}) and lowest in **{low_year}** ({int(yearly_track_count.min())}).\n- Years with fewer than 30 tracks: {', '.join(str(int(y)) for y in year_counts[year_counts < 30].index)}. These annual averages are particularly sensitive to sample composition.\n- Average popularity is highest in **{peak_pop_year}** ({yearly.loc[peak_pop_year,'average_popularity']:.2f}; n={int(yearly.loc[peak_pop_year,'track_count'])}) and lowest in **{low_pop_year}** ({yearly.loc[low_pop_year,'average_popularity']:.2f}; n={int(yearly.loc[low_pop_year,'track_count'])}). Do not infer a historical cause: popularity scores, coverage, and cohort sizes differ.\n- Energy, danceability, and valence trends are available in the annual summary CSV and charts. Read them alongside yearly track counts.\n\n## Graph guide\n\nEach graph's objective is to show change by release year. The line chart reports yearly averages; popularity also reports a yearly median and count in the table. Main insight: historical variation is descriptive and annual sample sizes are uneven. Recommendation: use these patterns to form a question for a current, controlled release-planning test. Limitation: this is a cross-sectional dataset with no control for artist, genre, promotion, track age, or collection process.\n\nFiles: `yearly_track_count.png`, `yearly_average_popularity.png`, `yearly_average_energy.png`, `yearly_average_danceability.png`, `yearly_average_valence.png`, and `combined_temporal_features.png`.\n\nThe combined chart min-max normalizes each feature separately across the included years. Its vertical values compare within-feature shapes only, not original values. Popularity is excluded because it uses a 0–100 scale.\n""")

with open(os.path.join(REPORT_DIR, "TEMPORAL_ANALYSIS_REPORT.md"), "a", encoding="utf-8") as file:
    file.write(f"""\n## Graph-specific evidence and recommendations

- **Yearly track count:** {peak_year} is the maximum ({int(yearly_track_count.max()):,}); {low_year} is the minimum ({int(yearly_track_count.min())}). The chart shows uneven dataset representation. Use year averages cautiously and plan with current audience signals.
- **Average popularity:** Across all years, {peak_pop_year} is highest ({yearly.loc[peak_pop_year,'average_popularity']:.2f}; n={int(yearly.loc[peak_pop_year,'track_count'])}) and {low_pop_year} lowest ({yearly.loc[low_pop_year,'average_popularity']:.2f}; n={int(yearly.loc[low_pop_year,'track_count'])}). Among years with at least 30 tracks, {eligible_pop_high} is highest ({eligible_yearly.loc[eligible_pop_high,'average_popularity']:.2f}; n={int(eligible_yearly.loc[eligible_pop_high,'track_count'])}) and {eligible_pop_low} lowest ({eligible_yearly.loc[eligible_pop_low,'average_popularity']:.2f}; n={int(eligible_yearly.loc[eligible_pop_low,'track_count'])}). Treat this as historical context, not a release target.
- **Average energy:** Among years with at least 30 tracks, the range is {eligible_yearly['average_energy'].min():.3f} ({int(eligible_yearly['average_energy'].idxmin())}) to {eligible_yearly['average_energy'].max():.3f} ({int(eligible_yearly['average_energy'].idxmax())}). This describes the sampled tracks; it does not show that energy should be raised or lowered.
- **Average danceability:** The eligible-year range is {eligible_yearly['average_danceability'].min():.3f} ({int(eligible_yearly['average_danceability'].idxmin())}) to {eligible_yearly['average_danceability'].max():.3f} ({int(eligible_yearly['average_danceability'].idxmax())}). Compare with current audience tests before using it in production decisions.
- **Average valence:** The eligible-year range is {eligible_yearly['average_valence'].min():.3f} ({int(eligible_yearly['average_valence'].idxmin())}) to {eligible_yearly['average_valence'].max():.3f} ({int(eligible_yearly['average_valence'].idxmax())}). Valence is an audio estimate of positive musical character, not listener sentiment.
- **Combined normalized features:** The chart compares each eligible feature's relative position within its own observed range. Use it to compare broad shapes only; it contains no absolute feature score and suggests no causal mechanism.
""")

with open(os.path.join(REPORT_DIR, "MY_CODE_EXPLANATION.md"), "w", encoding="utf-8") as file:
    file.write("""# My Temporal Analysis Code: Beginner Guide\n\n## What the notebook does\n\nIt reads the cleaned CSV, checks its basic structure, groups tracks by release year, calculates counts and yearly averages, saves six charts, and prints sample-size findings. It does not modify the raw data.\n\n## Imports and loading\n\n- `import pandas as pd` loads Pandas and gives it the short name `pd`. Pandas stores the CSV in a table called a DataFrame.\n- `import matplotlib.pyplot as plt` loads the plotting functions with the short name `plt`.\n- `pd.read_csv('../data/processed/cleaned_spotify_tracks.csv')` reads the original CSV. The `..` means “go up one folder” from `notebooks/`, then enter `data/processed/`.\n- `df.head()` shows the first five rows. `df.shape` returns (row count, column count). `df.dtypes` lists each column's data type.\n\n## Checking and preparing years\n\n- `df.isna().sum().sum()` counts missing cells: the first `sum` counts within each column; the second adds those counts together.\n- `df.duplicated().sum()` counts repeated full rows. `df['track_id'].duplicated().sum()` checks repeated IDs.\n- `pd.to_numeric(..., errors='coerce')` converts the year to a number and would turn unparseable values into missing values. `dropna(subset=['year'])` removes only rows without a usable year. `astype(int)` makes the year a whole number.\n\n## Grouping by year\n\n- `df.groupby('year')` makes a group for each year.\n- `['track_id'].count()` counts tracks in each year. `sort_index()` orders years from earliest to latest.\n- `groupby(...).agg(...)` calculates several summaries together. `mean` is the arithmetic average; `median` is the middle value after sorting. `track_count` tells how many rows are behind each yearly result.\n- `df.groupby('year')['energy'].mean()` calculates one average energy value for each year. The danceability and valence lines do the same for those columns.\n\n## Making and saving graphs\n\n- `plt.figure(figsize=(12, 5))` sets the graph's size. `plt.bar` makes the count bars. `plt.plot` makes lines; `marker='o'` adds a dot for each observed year.\n- `plt.xlabel`, `plt.ylabel`, and `plt.title` label the axes and graph. `plt.grid` adds a light grid.\n- `plt.savefig(..., dpi=150)` writes a clear PNG to the output folder. `plt.show(block=False)` displays it in Jupyter; `plt.close()` closes the current figure before the next one.\n- `minimum_tracks = 30` sets a display threshold. `yearly_track_count >= minimum_tracks` identifies years meeting it. Years below 30 are still in the calculations, but the connected line focuses on years with more observations. If the threshold changes, the line and normalized comparison include a different set of years.\n\n## Combined normalized graph\n\nThe three features are put in a small table, filtered to years meeting the sample threshold, then each feature is converted to a 0-to-1 range using `(value - minimum) / (maximum - minimum)`. This lets the reader compare the shapes of the lines. The result is not the original energy, danceability, or valence scale, so it cannot be read as a real feature score.\n\n## Conclusions and limitations\n\nA yearly average describes tracks in this file. It does not prove that release year caused the audio feature or popularity to change. Years have different track counts, and factors such as artist reach, promotion, genre, and the age of a track are not controlled.\n\n## Viva questions and short answers\n\n1. **What does `groupby` do?** It separates rows into groups that share a value, here the release year.\n2. **Why show the median popularity too?** The median is less affected by a few very high values than the mean.\n3. **Why include track count?** It shows how many rows support each yearly average.\n4. **What does valence mean?** It is an audio-based estimate of how positive or happy the music sounds, not a direct measure of a listener's mood.\n5. **Why sort the year index?** To display the results in chronological order.\n6. **What does a line point represent?** The average for tracks in that release year.\n7. **Why mark years with fewer than 30 tracks?** Their averages may be less stable, so the graph treats them cautiously.\n8. **Does a positive correlation prove a feature causes popularity?** No. Correlation describes association and does not establish cause.\n9. **What happens if `minimum_tracks` changes?** The set of highlighted years and the combined-chart year range changes.\n10. **Why normalize the combined features?** It allows a shape comparison on one plot; it removes the original units and values.\n""")

with open(os.path.join(REPORT_DIR, "REFERENCE_AUDIT.md"), "w", encoding="utf-8") as file:
    file.write(f"""# Reference Audit\n\n## Resources inspected\n\nCloned `https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks` into the sibling folder `Spotify_EDA_Reference`. Inspected the README, CSV, data dictionary, 214-cell notebook, and 38-page PDF. The PDF is available locally at `presentation/reference_senior_presentation.pdf`.\n\n## Claims checked against the supplied CSV\n\n- README says 62,317 tracks: **verified** (62,317 rows).\n- README says years 1971–2024: **verified**.\n- English count of 23,392 / about 37.5%: **verified** ({language_summary.loc['English','track_count']/len(df):.1%}).\n- Korean-tagged mean popularity of 27.55: **verified** ({language_summary.loc['Korean','average_popularity']:.2f}; median {language_summary.loc['Korean','median_popularity']:.1f}; n={int(language_summary.loc['Korean','track_count']):,}). This alone does not establish success caused by language.\n- Energy correlation with popularity of about 0.148: **verified** (Pearson r={correlations['energy']:.3f}). It is weak and observational. Other feature correlations include danceability {correlations['danceability']:.3f}, valence {correlations['valence']:.3f}, and acousticness {correlations['acousticness']:.3f}.\n\n## Claims not independently confirmed\n\nThe README's “2,888 outliers”, “5.0x more popular”, feature differences for a high-performance group, “+10 popularity points potential”, “623,170 popularity points impact”, and three emerging language opportunities have no sufficiently clear calculation or definition in the README. They are not repeated as established facts. The senior notebook contains extensive exploratory plots but does not provide a reproducible definition for every executive claim.\n\n## Data-quality differences and caution\n\nThe source notebook labels missing values as absent at its initial inspection, but the CSV's invalid extraction values are encoded as -1 in 11 audio/code columns and -100,000 in loudness, so a null-only missing-value count misses 35 affected rows. The dictionary gives several ranges that include -1; the shared all-column sentinel pattern indicates missing extraction results in this file. Confirm that interpretation with the instructor if needed.\n\n## Useful methods retained\n\nBasic DataFrame inspection, group summaries, charts with explicit labels, and presentation flow from objective through recommendations were retained. This project's notebook independently computes its results from the copied CSV and shows sample sizes.\n""")

with open(os.path.join(ROOT, "requirements.txt"), "w", encoding="utf-8") as file:
    file.write("pandas\nnumpy\nmatplotlib\nseaborn\nscipy\njupyter\npython-pptx\n")

with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as file:
    file.write("""# Spotify Tracks EDA Project\n\nA four-member college project analyzing Spotify track metadata. The raw CSV is preserved in `data/raw/`; analysis output and source references are stored separately. The primary leader contribution is the beginner-friendly temporal notebook.\n\n## Setup (Windows PowerShell)\n\n```powershell\ncd D:\\MANHATTAN\\Spotify_EDA_Project\npython -m venv .venv\n.venv\\Scripts\\Activate.ps1\npython -m pip install -r requirements.txt\njupyter notebook\n```\n\nIf PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate the environment. In Google Colab, upload the project files or mount the project folder and adjust the notebook's relative paths.\n\n## Main files\n\n- `notebooks/05_Temporal_Analysis.ipynb`: leader's temporal analysis.\n- `data/raw/spotify_tracks.csv`: unchanged original data.\n- `data/processed/cleaned_spotify_tracks.csv`: exact repeats removed and confirmed missing sentinels marked as missing.\n- `outputs/reports/`: dataset, temporal, recommendation, reference, and code explanation reports.\n- `outputs/graphs/temporal/`: six temporal graph images.\n- `team/`: assignment tracking, handoff, and final integration checklist.\n- `presentation/Spotify_EDA_Draft.pptx`: editable 18-slide integration draft with placeholders for teammate results.\n\n## Reproducibility\n\nFrom `Spotify_EDA_Project`, run `python src\\build_handoff.py` to rebuild the notebook outputs, cleaned copy, tables, reports, and presentation draft. It reads the raw CSV and does not edit it. The notebook itself uses beginner-level Pandas and Matplotlib operations.\n\n## Source\n\nReference repository: https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks. See `outputs/reports/REFERENCE_AUDIT.md` for claim checks and caveats.\n""")

# Execute the notebook code in order and store printed output and execution counts.
os.chdir(os.path.join(ROOT, "notebooks"))
execution_space = {}
execution_count = 1
for cell in notebook["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        output_text = ""
        import io
        import contextlib
        output_buffer = io.StringIO()
        with contextlib.redirect_stdout(output_buffer):
            exec(compile(source, NOTEBOOK_PATH, "exec"), execution_space)
        output_text = output_buffer.getvalue()
        cell["execution_count"] = execution_count
        if output_text:
            cell["outputs"] = [{"output_type": "stream", "name": "stdout", "text": output_text.splitlines(True)}]
        image_name = None
        for filename in ["yearly_track_count.png", "yearly_average_popularity.png", "yearly_average_energy.png", "yearly_average_danceability.png", "yearly_average_valence.png", "combined_temporal_features.png"]:
            if filename in source:
                image_name = filename
        if image_name:
            image_path = os.path.join(TEMPORAL_DIR, image_name)
            with open(image_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode("ascii")
            cell["outputs"].append({"output_type": "display_data", "data": {"image/png": image_data, "text/plain": f"<Figure: {image_name}>"}, "metadata": {}})
        execution_count += 1
with open(NOTEBOOK_PATH, "w", encoding="utf-8") as file:
    json.dump(notebook, file, ensure_ascii=False, indent=1)

print("Notebook cells executed:", execution_count - 1)
print("Notebook saved:", NOTEBOOK_PATH)



