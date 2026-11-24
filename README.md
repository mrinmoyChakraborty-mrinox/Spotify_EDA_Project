# Spotify Tracks EDA Project

This is a four-member exploratory analysis of Spotify track data. The final analysis belongs in one consolidated, beginner-readable notebook at the project root: `Spotify_EDA.ipynb`.

## Submission layout

The flat root-level files follow the layout of the supplied reference repository:

- `Spotify_EDA.ipynb` — the single consolidated notebook for data inspection, cleaning, Univariate, Bivariate, Multivariate, Temporal analysis, findings, and recommendations.
- `spotify_tracks.csv` — copy of the dataset supplied with the problem statement; use as the raw input and do not overwrite it.
- `spotify_data_description.csv` — data dictionary supplied with the problem statement.
- `README.md` — project and run instructions.
- `Spotify_EDA_Subjective_Answers.pdf` — required final PDF answering the subjective questions; **not ready yet** because the teammate sections are still awaiting integration.

The final submission follows the reference repository's flat, root-level layout. Exactly one notebook remains in this project: `Spotify_EDA.ipynb`. The two older notebook drafts are preserved outside the repository in `D:\MANHATTAN\Spotify_EDA_Working_Archive\notebooks`. The nested `data/`, `outputs/`, `src/`, `team/`, and `presentation/` folders are supporting work materials; the required analyses and presentation narrative belong in the consolidated root notebook. Member work can be drafted elsewhere for review, but its final code and verified interpretation must be integrated into `Spotify_EDA.ipynb`.

## Run the notebook on Windows

From PowerShell:

```powershell
cd D:\MANHATTAN\Spotify_EDA_Project
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter notebook Spotify_EDA.ipynb
```

In Google Colab, upload `Spotify_EDA.ipynb`, `spotify_tracks.csv`, and `spotify_data_description.csv` together, or mount the folder containing them. The notebook expects the CSV beside the notebook.

## Current integration status

Dataset inspection, documented cleaning logic, leader temporal actuals, year-over-year growth, chart interpretations, and initial recommendation evidence are included. The leader's popular-track comparisons use a fixed global Q3 cutoff, with ties disclosed. Member 1's univariate section, Member 2's bivariate section, Member 3's multivariate/outlier section, final recommendation review, and the subjective-answer PDF still need reviewed results. The consolidated notebook labels teammate sections as pending; it remains an integration draft until they are complete.

## Verified source data

The root-level CSV and data dictionary are copies of the folder supplied with the problem statement. The supplied CSV and the previously cloned reference CSV have identical values and row order; their byte-level difference is line endings only. See `data/metadata/SOURCE_MANIFEST.md` and `outputs/reports/REFERENCE_AUDIT.md` for provenance and reference-claim checks.
