# Leader Progress Report

## Files acquired

- `data/raw/spotify_tracks.csv` - original file, preserved unchanged.
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
- Six graph files are generated in `outputs/graphs/temporal/`. Year averages are descriptive and sample sizes are uneven.

## Recommendation evidence

- Energy/popularity correlation: r=0.147, a weak association that does not show causation.
- Korean-tagged mean popularity: 27.55, median 26.0, n=6,893.
- Recommendations focus on data validation, segment research, current audience signals, and controlled tests.

## Completed deliverables

- Beginner-friendly temporal notebook, executed and saved with cell outputs.
- Cleaned dataset copy, dataset profile, temporal report, recommendation report and evidence CSV.
- Code explanation with viva questions, reference audit, six temporal graphs, team tracker, handoff template, integration checklist, requirements, and editable 18-slide PPTX draft.

## Teammate tasks remaining

Member 1: complete cleaning and univariate analysis, then submit notebook, source, graph images, numerical findings, recommendations, and limitations.

Member 2: complete bivariate analysis with sample sizes and correlation caveats; submit the same handoff items.

Member 3: complete multivariate and outlier analysis, state the outlier rule, and distinguish errors from valid unusual tracks.

## Leader tasks remaining

1. Review Member 1: compare their cleaned row count, missing-value treatment, variable ranges, and distribution statistics with the raw CSV and data dictionary. Confirm every plot uses the same cleaned data.
2. Review Member 2: reproduce each reported correlation or group comparison; check axis scales, sample size, outliers, direction, and avoid causal wording.
3. Review Member 3: verify multivariate method and variable selection; check the outlier threshold and inspect examples before calling them errors.
4. Find incorrect interpretations by asking what rows, filters, formula, and comparison support each claim. Recalculate key values from the source.
5. Combine graphs only after confirming consistent columns, cleaning, labels, units, colors, and sample definitions. Keep separate plots if a combined scale would mislead.
6. Finalize recommendations by linking each action to a verified finding, a measurable success metric, a test plan, and a limitation.
7. Replace PPT placeholders, verify each number against the team's final notebooks, and keep the conclusion consistent with evidence.
8. Rehearse the 18-slide story, divide speaking roles, prepare short answers about methods and limitations, and keep a backup copy.

## Technical note

A project-local virtual environment was created and the packages in requirements.txt installed. All 17 notebook code cells were executed sequentially with Python; no cell errors occurred, and all six graph images were saved and embedded as notebook outputs. A full nbconvert run did not complete in this managed Windows session, so this report does not claim a successful Jupyter-kernel run. Open the notebook interactively with the setup commands in README.md and review the saved chart outputs.
