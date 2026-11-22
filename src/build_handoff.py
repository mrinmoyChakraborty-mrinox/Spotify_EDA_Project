import os
import build_project_outputs as project
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

ROOT = project.ROOT

with open(os.path.join(ROOT, "data", "metadata", "SOURCE_MANIFEST.md"), "w", encoding="utf-8") as file:
    file.write("""# Source Manifest\n\nRepository: https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks\nClone URL: https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks.git\nFiles were cloned from the repository's `main` branch at commit `7867c8b74a49df9fd2df56440b7fa372a989bb10` and copied into the project without changing the raw CSV. The separate working clone is `D:\\MANHATTAN\\Spotify_EDA_Reference`.\n\n| Resource | Repository file | Direct URL | Local project copy |\n|---|---|---|---|\n| Dataset | `spotify_tracks.csv` | https://raw.githubusercontent.com/Adrija-verse/EDA_Project1_SpotifyTracks/main/spotify_tracks.csv | `data/raw/spotify_tracks.csv` |\n| Data dictionary | `spotify_data_description.csv` | https://raw.githubusercontent.com/Adrija-verse/EDA_Project1_SpotifyTracks/main/spotify_data_description.csv | `data/metadata/spotify_data_description.csv` |\n| Senior notebook | `EDA_PROJECT_ADRIJA_SIL (1).ipynb` | https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks/blob/main/EDA_PROJECT_ADRIJA_SIL%20(1).ipynb | `notebooks/reference_senior_eda.ipynb` |\n| Senior presentation | `Exploratory Data Analysis of Spotify Tracks_Adrija Sil.pdf` | https://github.com/Adrija-verse/EDA_Project1_SpotifyTracks/blob/main/Exploratory%20Data%20Analysis%20of%20Spotify%20Tracks_Adrija%20Sil.pdf | `presentation/reference_senior_presentation.pdf` |\n| README | `README.md` | https://raw.githubusercontent.com/Adrija-verse/EDA_Project1_SpotifyTracks/main/README.md | `data/metadata/reference_README.md` |\n\nAll five expected resources are present locally and readable. Repository source metadata is stored in the sibling clone. No Spotify API or scraping was used.\n""")

with open(os.path.join(ROOT, "outputs", "reports", "REFERENCE_AUDIT.md"), "a", encoding="utf-8") as file:
    file.write(f"""\n## PDF-specific claims checked\n\n- Page 27 gives 1975 popularity as about 17.5; the supplied CSV gives **{project.yearly.loc[1975,'average_popularity']:.2f}** for 1975 (n={int(project.yearly.loc[1975,'track_count'])}). This is a material disagreement.\n- Page 21 describes Korean popularity as narrow and low; the dataset's Korean-tagged tracks have the highest language mean ({project.language_summary.loc['Korean','average_popularity']:.2f}; median {project.language_summary.loc['Korean','median_popularity']:.1f}; n={int(project.language_summary.loc['Korean','track_count']):,}).\n- Page 7 reports “19 features,” while the CSV and data dictionary list 22 columns. The PDF does not explain a different counting convention.\n- The PDF recommends increasing energy and copying a “Korean model.” This is not supported as a causal recommendation by the weak observed energy-popularity relationship (r={project.correlations['energy']:.3f}). The outlier counts also lack enough detail to reproduce confidently.\n""")

with open(os.path.join(ROOT, "team", "TEAM_TRACKER.md"), "w", encoding="utf-8") as file:
    file.write("""# Team Tracker\n\n| Member | Assignment | Status | Deliverables | Deadline | Review Status |\n|---|---|---|---|---|---|\n| Leader | Temporal analysis, recommendations, integration | In progress | Temporal notebook and reports prepared; integration pending | 25 Nov 2026 | Temporal outputs checked; final review pending |\n| Member 1 | Data cleaning and univariate analysis | Awaiting teammate update | Notebook, source code, graphs, findings | 25 Nov 2026 | Pending evidence |\n| Member 2 | Bivariate analysis | Awaiting teammate update | Notebook, source code, graphs, findings | 25 Nov 2026 | Pending evidence |\n| Member 3 | Multivariate and outlier analysis | Awaiting teammate update | Notebook, source code, graphs, findings | 25 Nov 2026 | Pending evidence |\n\nUpdate statuses only after receiving and checking deliverables.\n""")

with open(os.path.join(ROOT, "team", "TEAM_HANDOFF_TEMPLATE.md"), "w", encoding="utf-8") as file:
    file.write("""# Team Member Handoff Template\n\n**Member:**\n\n**Analysis section:**\n\n**Dataset file and cleaning steps used:**\n\n## Deliverables\n\n- [ ] Notebook (`.ipynb`)\n- [ ] Python source code (`.py`, if used)\n- [ ] Graph images\n- [ ] Graph interpretation for each graph\n- [ ] Numerical evidence and sample sizes\n- [ ] Main insights\n- [ ] Recommendations linked to evidence\n- [ ] Limitations and assumptions\n\n## Review notes\n\n**Columns and filters used:**\n\n**Results independently checked:**\n\n**Questions or unresolved issues:**\n""")

with open(os.path.join(ROOT, "team", "FINAL_INTEGRATION_CHECKLIST.md"), "w", encoding="utf-8") as file:
    file.write("""# Final Integration Checklist\n\n- [ ] Same raw dataset used or differences documented.\n- [ ] Cleaning steps are reproducible; raw data remains unchanged.\n- [ ] Every notebook runs from top to bottom.\n- [ ] Graph titles, axes, units, legends, and sample sizes are clear.\n- [ ] Numerical claims match notebook or CSV output.\n- [ ] Interpretations do not claim causation from correlation.\n- [ ] Recommendations link a finding to an action and measurable outcome.\n- [ ] Teammate results replace PPT placeholders.\n- [ ] PPT numbers and graphs match the reports.\n- [ ] Presenters know their sections and handoffs.\n- [ ] Full presentation is rehearsed and timed.\n- [ ] Final files are backed up in two locations.\n""")

raw = project.raw_df
yearly = project.yearly
year_counts = project.year_counts
language_summary = project.language_summary
correlations = project.correlations
duplicate_rows = project.duplicate_rows
sentinel_rows = project.sentinel_rows
peak_year = project.peak_year
low_year = project.low_year
peak_pop_year = project.peak_pop_year
low_pop_year = project.low_pop_year
TEMPORAL_DIR = project.TEMPORAL_DIR

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
navy = RGBColor(22, 43, 70)
green = RGBColor(30, 140, 112)
white = RGBColor(255, 255, 255)
dark = RGBColor(40, 48, 58)
slides = [
    ("Exploratory Data Analysis of Spotify Tracks", ["Team project | Data, audio features, and release-year patterns", "Team members: [Add four names]", "Submission: 25 November 2026"], None),
    ("Project Objective", ["Describe track and audio-feature patterns in the supplied dataset.", "Explore relationships and release-year differences.", "Develop evidence-based recommendations with clear limitations."], None),
    ("Problem Statement", ["What patterns are visible in the tracks represented in this dataset?", "Which comparisons are useful for artists, producers, marketers, or platforms?", "How can we avoid treating an association as a guarantee of success?"], None),
    ("Dataset Overview", [f"{raw.shape[0]:,} rows and {raw.shape[1]} columns in the raw file", f"Release years: {int(raw.year.min())} to {int(raw.year.max())}", "Seven language labels, including Unknown", "Source: reference repository listed in project README"], None),
    ("Variables", ["Track metadata: title, artist, album, ID, language, year", "Popularity: numeric score from 0 to 100", "Audio features: energy, danceability, valence, acousticness, and others", "Variable definitions are in the supplied data dictionary"], None),
    ("Methodology", ["Inspect data types, missing values, duplicates, and unusual values.", "Use descriptive statistics and visual comparisons.", "Keep original data unchanged and document cleaning.", "Treat results as descriptive evidence, not causal proof."], None),
    ("Data Cleaning", [f"Found {duplicate_rows} exact repeated rows and {sentinel_rows} records with a shared missing-feature sentinel pattern.", "Removed exact repeated rows in the processed copy.", "Marked sentinel measurements missing; did not impute or discard the records.", "Raw CSV remains unchanged."], None),
    ("Univariate Analysis", ["[Member 1: add distributions, summary statistics, and interpretations]", "[Add evidence and sample size for each main conclusion]"], None),
    ("Bivariate Analysis", ["[Member 2: add selected variable relationships and graphs]", "[State direction and strength; correlation does not establish causation]"], None),
    ("Multivariate Analysis", ["[Member 3: add combined-feature analysis and method]", "[Explain why the selected variables and comparisons are useful]"], None),
    ("Temporal Analysis: Track Counts", [f"The cleaned dataset includes {int(year_counts.sum()):,} non-duplicate records.", f"Most represented year: {peak_year} ({int(year_counts.max()):,} tracks). Least represented: {low_year} ({int(year_counts.min())} tracks).", "Early-year averages have small samples; the chart labels the full observed range."], "yearly_track_count.png"),
    ("Temporal Analysis: Popularity", [f"Yearly mean is highest in {peak_pop_year} ({yearly.loc[peak_pop_year,'average_popularity']:.2f}; n={int(yearly.loc[peak_pop_year,'track_count'])}).", f"It is lowest in {low_pop_year} ({yearly.loc[low_pop_year,'average_popularity']:.2f}; n={int(yearly.loc[low_pop_year,'track_count'])}).", "Annual values describe the collected tracks and are not a forecast."], "yearly_average_popularity.png"),
    ("Temporal Analysis: Audio Features", ["Yearly energy, danceability, and valence averages are shown in the project graphs.", "The combined graph min-max normalizes each feature across eligible years.", "Its scale compares within-feature shapes; it is not an original feature score."], "combined_temporal_features.png"),
    ("Outlier Analysis", ["[Member 3: add the team's chosen outlier rule and findings]", "[Report the number of flagged records and whether they are errors or plausible unusual tracks]"], None),
    ("Overall Findings", [f"Energy and popularity have a weak positive Pearson correlation in this dataset (r={correlations['energy']:.3f}).", f"Korean-tagged tracks average {language_summary.loc['Korean','average_popularity']:.2f} popularity (median {language_summary.loc['Korean','median_popularity']:.1f}; n={int(language_summary.loc['Korean','track_count']):,}).", "Language and audio-feature averages do not isolate the cause of popularity."], None),
    ("Recommendations", ["Validate duplicate and missing-feature patterns before analysis.", "Compare language segments with sample sizes, median scores, and audience research.", "Run controlled creative or marketing tests; measure saves, completion, and conversion.", "Use historical patterns as context and current audience data for release planning."], None),
    ("Limitations", ["The dataset's collection and coverage process is not documented here.", "Track counts vary across years and language labels.", "Popularity may reflect track age, artist reach, promotion, and platform factors.", "Observational relationships do not establish cause or predict future results."], None),
    ("Conclusion and Questions", ["[Add a one-sentence conclusion after teammate results are integrated]", "Thank you", "Questions?"], None),
]

for index, item in enumerate(slides):
    title, bullets, graph_file = item
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = white
    if index == 0:
        band = slide.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(7.5))
        band.fill.solid()
        band.fill.fore_color.rgb = navy
        band.line.fill.background()
        title_box = slide.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(1.6))
        title_box.text_frame.text = title
        for paragraph in title_box.text_frame.paragraphs:
            paragraph.font.name = "Aptos Display"
            paragraph.font.size = Pt(34)
            paragraph.font.bold = True
            paragraph.font.color.rgb = white
        y = 3.6
        for bullet in bullets:
            box = slide.shapes.add_textbox(Inches(1.0), Inches(y), Inches(11), Inches(0.45))
            box.text_frame.text = bullet
            box.text_frame.paragraphs[0].font.size = Pt(18)
            box.text_frame.paragraphs[0].font.color.rgb = white
            y += 0.65
        continue
    accent = slide.shapes.add_shape(1, 0, 0, Inches(0.18), prs.slide_height)
    accent.fill.solid()
    accent.fill.fore_color.rgb = green
    accent.line.fill.background()
    title_box = slide.shapes.add_textbox(Inches(0.65), Inches(0.42), Inches(12), Inches(0.65))
    title_box.text_frame.text = title
    title_paragraph = title_box.text_frame.paragraphs[0]
    title_paragraph.font.name = "Aptos Display"
    title_paragraph.font.size = Pt(27)
    title_paragraph.font.bold = True
    title_paragraph.font.color.rgb = navy
    text_width = Inches(6.0 if graph_file else 12.0)
    body = slide.shapes.add_textbox(Inches(0.85), Inches(1.5), text_width, Inches(5.2))
    body.text_frame.word_wrap = True
    for bullet in bullets:
        paragraph = body.text_frame.add_paragraph()
        paragraph.text = bullet
        paragraph.level = 0
        paragraph.font.name = "Aptos"
        paragraph.font.size = Pt(18)
        paragraph.font.color.rgb = dark
        paragraph.space_after = Pt(14)
    if graph_file:
        image_path = os.path.join(TEMPORAL_DIR, graph_file)
        if os.path.exists(image_path):
            slide.shapes.add_picture(image_path, Inches(6.7), Inches(1.65), width=Inches(5.9))
    footer = slide.shapes.add_textbox(Inches(0.7), Inches(7.05), Inches(12), Inches(0.2))
    footer.text_frame.text = "Spotify Tracks EDA | Draft - replace bracketed sections after team review"
    footer.text_frame.paragraphs[0].font.size = Pt(9)
    footer.text_frame.paragraphs[0].font.color.rgb = RGBColor(110, 120, 130)

presentation_path = os.path.join(ROOT, "presentation", "Spotify_EDA_Draft.pptx")
prs.save(presentation_path)

with open(os.path.join(ROOT, "LEADER_PROGRESS_REPORT.md"), "w", encoding="utf-8") as file:
    file.write(f"""# Leader Progress Report\n\n## Files acquired\n\n- `data/raw/spotify_tracks.csv` - original file, preserved unchanged.\n- `data/metadata/spotify_data_description.csv` - data dictionary.\n- `notebooks/reference_senior_eda.ipynb` - senior's 214-cell notebook.\n- `presentation/reference_senior_presentation.pdf` - senior's 38-page PDF.\n- `data/metadata/reference_README.md` - repository README copy.\n- Repository clone is in sibling folder `Spotify_EDA_Reference`.\n\n## Dataset profile\n\nRaw data has {raw.shape[0]:,} rows and {raw.shape[1]} columns, years {int(raw.year.min())}-{int(raw.year.max())}. It has {duplicate_rows} exact repeated rows and {project.sentinel_rows} all-feature sentinel rows. Processed copy has {project.df.shape[0]:,} rows after exact duplicates are removed; sentinel measurements are marked missing without imputation.\n\n## Temporal findings\n\n- Highest year count: {peak_year} ({int(year_counts.max()):,}); lowest: {low_year} ({int(year_counts.min())}).\n- Mean popularity highest in {peak_pop_year} ({yearly.loc[peak_pop_year,'average_popularity']:.2f}; n={int(yearly.loc[peak_pop_year,'track_count'])}), lowest in {low_pop_year} ({yearly.loc[low_pop_year,'average_popularity']:.2f}; n={int(yearly.loc[low_pop_year,'track_count'])}).\n- Six graph files are generated in `outputs/graphs/temporal/`. Year averages are descriptive and sample sizes are uneven.\n\n## Recommendation evidence\n\n- Energy/popularity correlation: r={correlations['energy']:.3f}, a weak association that does not show causation.\n- Korean-tagged mean popularity: {language_summary.loc['Korean','average_popularity']:.2f}, median {language_summary.loc['Korean','median_popularity']:.1f}, n={int(language_summary.loc['Korean','track_count']):,}.\n- Recommendations focus on data validation, segment research, current audience signals, and controlled tests.\n\n## Completed deliverables\n\n- Beginner-friendly temporal notebook, executed and saved with cell outputs.\n- Cleaned dataset copy, dataset profile, temporal report, recommendation report and evidence CSV.\n- Code explanation with viva questions, reference audit, six temporal graphs, team tracker, handoff template, integration checklist, requirements, and editable 18-slide PPTX draft.\n\n## Teammate tasks remaining\n\nMember 1: complete cleaning and univariate analysis, then submit notebook, source, graph images, numerical findings, recommendations, and limitations.\n\nMember 2: complete bivariate analysis with sample sizes and correlation caveats; submit the same handoff items.\n\nMember 3: complete multivariate and outlier analysis, state the outlier rule, and distinguish errors from valid unusual tracks.\n\n## Leader tasks remaining\n\n1. Review Member 1: compare their cleaned row count, missing-value treatment, variable ranges, and distribution statistics with the raw CSV and data dictionary. Confirm every plot uses the same cleaned data.\n2. Review Member 2: reproduce each reported correlation or group comparison; check axis scales, sample size, outliers, direction, and avoid causal wording.\n3. Review Member 3: verify multivariate method and variable selection; check the outlier threshold and inspect examples before calling them errors.\n4. Find incorrect interpretations by asking what rows, filters, formula, and comparison support each claim. Recalculate key values from the source.\n5. Combine graphs only after confirming consistent columns, cleaning, labels, units, colors, and sample definitions. Keep separate plots if a combined scale would mislead.\n6. Finalize recommendations by linking each action to a verified finding, a measurable success metric, a test plan, and a limitation.\n7. Replace PPT placeholders, verify each number against the team's final notebooks, and keep the conclusion consistent with evidence.\n8. Rehearse the 18-slide story, divide speaking roles, prepare short answers about methods and limitations, and keep a backup copy.\n\n## Technical note\n\nA project-local virtual environment was created and the packages in requirements.txt installed. All 17 notebook code cells were executed sequentially with Python; no cell errors occurred, and all six graph images were saved and embedded as notebook outputs. A full nbconvert run did not complete in this managed Windows session, so this report does not claim a successful Jupyter-kernel run. Open the notebook interactively with the setup commands in README.md and review the saved chart outputs.\n""")

print("Team documents and presentation saved.")


