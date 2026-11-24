# Leader Progress Report

## Files acquired

- `spotify_tracks.csv` - problem-statement supplied raw file, copied unchanged to the project root.
- `spotify_data_description.csv` - problem-statement supplied data dictionary, copied unchanged to the project root.
- Root-level supplied CSV and the reference-repository CSV have identical parsed rows and values; their byte-level difference is line endings only.
- `data/metadata/spotify_data_description.csv` - data dictionary.
- `notebooks/reference_senior_eda.ipynb` - senior's 214-cell notebook.
- `presentation/reference_senior_presentation.pdf` - senior's 38-page PDF.
- `data/metadata/reference_README.md` - repository README copy.
- `team/Spotify_EDA_Team_Instructions_Grounded.html` - member guide updated with verified project facts as of 22 November 2026.
- Repository clone is in sibling folder `Spotify_EDA_Reference`.

## Dataset profile

Raw data has 62,317 rows and 22 columns, years 1971-2024. It has 78 exact repeated rows and 35 all-feature sentinel rows. Processed copy has 62,239 rows after exact duplicates are removed; sentinel measurements are marked missing without imputation.

## Temporal findings

- Highest year count: 2023 (6,427); lowest: 1976 (9).
- Mean popularity highest in 1976 (39.33; n=9), lowest in 1992 (7.90; n=405).
- The notebook now includes the original six actuals charts, eight additional temporal actuals analyses, and a separate year-over-year growth chart. Figures and result tables are embedded.
- Popular tracks use a fixed popularity >= cleaned-data Q3=26 cutoff; ties select 16,051 rows (25.8%). Popular-track duration medians by decade range from 4.85 minutes (1990s) to 3.47 minutes (2020s).
- Energy–danceability decade correlations range from +0.116 (1980s) to +0.552 (2000s). This is association, not causation. Popularity is the dataset snapshot score grouped by release year, not historical popularity at release.

## Recommendation evidence

- Energy/popularity correlation: r=0.147, a weak association that does not show causation.
- Korean-tagged mean popularity: 27.55, median 26.0, n=6,893.
- Recommendations focus on data validation, segment research, current audience signals, and controlled tests.

## Completed deliverables

- `Spotify_EDA.ipynb` - one consolidated, root-level integration notebook; data inspection, cleaning, correlation evidence, leader actuals, year-over-year growth, chart outputs, and explanations have been run. Member 1–3 analysis sections remain marked pending.
- Cleaned dataset copy, dataset profile, temporal report, recommendation report and evidence CSV.
- Root-level notebook and data files now follow the flat, notebook-centered layout of the supplied reference repository.
- Code explanation with viva questions, reference audit, six temporal graphs, team tracker, handoff template, integration checklist, requirements, and editable 18-slide PPTX draft.

## Final submission note

The problem statement requires one consolidated Jupyter notebook, one subjective-answer PDF, and a README. The PDF and teammate sections are still pending; the current root notebook is an integration draft, not a finished submission.

## Teammate tasks remaining

Member 1: complete cleaning review and univariate analysis, then submit code/Markdown, graph images, numerical findings, recommendations, and limitations for integration into the single root-level `Spotify_EDA.ipynb`.

Member 2: complete bivariate analysis with sample sizes and correlation caveats; submit code/Markdown, graphs, findings, and limitations for integration into the single root-level `Spotify_EDA.ipynb`.

Member 3: complete multivariate and outlier analysis, state the outlier rule, and distinguish errors from valid unusual tracks; submit all evidence for integration into the single root-level `Spotify_EDA.ipynb`.

## Leader tasks remaining

1. Learn and present your completed Data Description and temporal actuals/growth sections; review verified cutoffs, sample sizes, findings and limitations.
2. Review Member 1: compare their cleaned row count, missing-value treatment, variable ranges, and distribution statistics with the raw CSV and data dictionary. Confirm every plot uses the same cleaned data.
2. Review Member 2: reproduce each reported correlation or group comparison; check axis scales, sample size, outliers, direction, and avoid causal wording.
3. Review Member 3: verify multivariate method and variable selection; check the outlier threshold and inspect examples before calling them errors.
4. Find incorrect interpretations by asking what rows, filters, formula, and comparison support each claim. Recalculate key values from the source.
5. Combine graphs only after confirming consistent columns, cleaning, labels, units, colors, and sample definitions. Keep separate plots if a combined scale would mislead.
6. Finalize recommendations by linking each action to a verified finding, a measurable success metric, a test plan, and a limitation.
7. Replace PPT placeholders, verify each number against the team's final notebooks, and keep the conclusion consistent with evidence.
8. Rehearse the 18-slide story, divide speaking roles, prepare short answers about methods and limitations, and keep a backup copy.

## Technical note

A project-local virtual environment was created and the packages in requirements.txt installed. All 26 notebook code cells were executed sequentially with the project-local Python environment; no cell errors occurred, and all 15 graph images were saved and embedded as notebook outputs. A full nbconvert run was not performed for this update. Open the notebook interactively with the setup commands in README.md and review the saved chart outputs.
