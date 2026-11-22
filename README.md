# Spotify Tracks EDA Project

A four-member college project analyzing Spotify track metadata. The raw CSV is preserved in `data/raw/`; analysis output and source references are stored separately. The primary leader contribution is the beginner-friendly temporal notebook.

## Setup (Windows PowerShell)

```powershell
cd D:\MANHATTAN\Spotify_EDA_Project
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter notebook
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate the environment. In Google Colab, upload the project files or mount the project folder and adjust the notebook's relative paths.

## Main files

- `notebooks/05_Temporal_Analysis.ipynb`: leader's temporal analysis.
- `data/raw/spotify_tracks.csv`: unchanged original data.
- `data/processed/cleaned_spotify_tracks.csv`: exact repeats removed and confirmed missing sentinels marked as missing.
- `outputs/reports/`: dataset, temporal, recommendation, reference, and code explanation reports.
- `outputs/graphs/temporal/`: six temporal graph images.
- `team/`: assignment tracking, handoff, and final integration checklist.
- `presentation/Spotify_EDA_Draft.pptx`: editable 18-slide integration draft with placeholders for teammate results.

## Reproducibility

From `Spotify_EDA_Project`, run `python src\build_handoff.py` to rebuild the notebook outputs, cleaned copy, tables, reports, and presentation draft. It reads the raw CSV and does not edit it. The notebook itself uses beginner-level Pandas and Matplotlib operations.

## Source

Reference repository: https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks. See `outputs/reports/REFERENCE_AUDIT.md` for claim checks and caveats.
