# Teacher Guide: Technology & Infrastructure Live Pulse

## 1. About our project
We built Technology & Infrastructure Live Pulse to monitor English news about technology and infrastructure. Our application collects news headlines, classifies their sentiment with ProsusAI/finbert, stores the results in SQLite and displays them in a Streamlit dashboard.

Our project relates to SDG 9: Industry, Innovation and Infrastructure. Our intended user is a municipal digital-infrastructure policy officer who wants to investigate news coverage about data centers, electricity infrastructure, cloud services and telecommunications.

This guide explains how to install our project, run the application, understand our code and reproduce our evaluation.

The dashboard supports human investigation. It does not prove public opinion, verify incidents or measure how severe an outage is. We analyse headlines, not complete articles.

## 2. Download our project
1. Open our GitHub repository.
2. Select Code and then Download ZIP.
3. Extract the downloaded ZIP.
4. Open the extracted project folder in VS Code or a terminal.
5. Check that requirements.txt, README.md, src, dashboard and tests are directly inside the folder.

Run all commands in this guide from the project root, which is the folder containing requirements.txt. Do not run them from inside src or dashboard.

## 3. Project structure
```text
tech_infra_pulse/
    README.md
    requirements.txt
    TEACHER_GUIDE.md
    dashboard/
        app.py
    src/
        analyze_sentiment.py
        config.py
        fetch_stream.py
        run_pipeline.py
        store_results.py
    data/
        pulse.db
    tests/
        calculate_accuracy.py
        manual_labels.csv
        model_comparison.md
```

If data/pulse.db is included and contains records, you can view existing results immediately. Otherwise, run our collector to create and populate it.

You do not need copied .venv or venv folders. Create a new environment on your own computer. Folders named __pycache__ and .ipynb_checkpoints are not needed to review the project. A Jupyter Notebook is optional and is not required for the application or accuracy test.

## 4. Requirements
You need:
- A compatible Python installation with pip and virtual-environment support.
- A terminal and web browser. VS Code is optional.
- Internet access for package installation, live news collection and the initial FinBERT download.
- Disk space for the Python environment and model files.

Python 3.11 is a suggested starting point, not a mandatory or verified original project version. Package compatibility also depends on the operating system. We do not specify a fixed hardware minimum in this guide.

Our requirements.txt lists:

| Package | Version | Purpose |
|---|---|---|
| streamlit | 1.49.1 | Dashboard interface |
| pandas | 2.3.3 | Data processing and evaluation |
| plotly | 6.3.1 | Interactive charts |
| requests | 2.32.5 | Downloading the RSS feed |
| feedparser | 6.0.12 | Reading RSS entries |
| transformers | 4.57.1 | Loading the sentiment pipeline |
| torch | 2.8.0 | Running the model |

We use Python's sqlite3 module, so a separate database server is not required. Our current code does not request API keys.

## 5. Install on Windows
Open PowerShell in the project root:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If your system uses python instead of py, use python for the first two commands.

We call the virtual environment's interpreter directly, so you do not need to activate the environment or change PowerShell's execution policy.

Check the installed packages:

```powershell
.\.venv\Scripts\python.exe -c "import streamlit, pandas, plotly, requests, feedparser, transformers, torch; print('Imports OK')"
```

## 6. Install on macOS or Linux
Open a terminal in the project root:

```bash
python3 --version
python3 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -c "import streamlit, pandas, plotly, requests, feedparser, transformers, torch; print('Imports OK')"
```

If venv is unavailable, install virtual-environment support according to your operating system's Python installation instructions.

## 7. View our dashboard
If a populated data/pulse.db is included, you can start the dashboard without running the collector.

Windows:

```powershell
.\.venv\Scripts\python.exe -m streamlit run dashboard/app.py
```

macOS or Linux:

```bash
./.venv/bin/python -m streamlit run dashboard/app.py
```

Open the Local URL displayed in the terminal. Keep the terminal open while reviewing the dashboard.

If the database is missing or empty, the dashboard displays a warning. Follow the next section to collect data. The dashboard reads the database, not the evaluation CSV.

## 8. Run live collection
Open two terminals in the project root.

### Terminal 1: news collector
Windows:

```powershell
.\.venv\Scripts\python.exe -m src.run_pipeline
```

macOS or Linux:

```bash
./.venv/bin/python -m src.run_pipeline
```

Use the module command above because our code imports modules through src.

The first startup may take longer while FinBERT downloads and loads. Each collection cycle then:
1. Reads the IDs of previously stored items.
2. Downloads our configured Google News RSS search feed.
3. Filters titles using our technology and infrastructure keywords.
4. Skips previously stored URLs.
5. Analyses the new titles with FinBERT.
6. Saves predictions in data/pulse.db.
7. Waits 600 seconds before the next cycle.

Processing time is additional to the 600-second wait. This is periodic polling, not a continuously pushed feed.

Expected terminal messages include:

```text
Found N new matching items.
Saved: <headline> -> <sentiment label>
```

Found 0 new matching items can be normal, especially when the feed entries have already been saved.

### Terminal 2: dashboard
Run the dashboard command from Section 7. Leave both terminals open for live collection and viewing.

Our dashboard caches database reads for 60 seconds. It does not automatically refresh on a schedule. After new items are saved, allow the cache to expire and reload or rerun the dashboard.

### Stop the application
Press Ctrl+C in both terminals. The database remains available for the next session.

### Optional: run one collection cycle
Instead of the continuous collector, use one of these commands:

Windows:

```powershell
.\.venv\Scripts\python.exe -c "from src.run_pipeline import run_once; run_once()"
```

macOS or Linux:

```bash
./.venv/bin/python -c "from src.run_pipeline import run_once; run_once()"
```

These commands load the model, process one batch and exit.

## 9. How to inspect the dashboard
1. Check the total number of monitored items and the positive, neutral and negative counts.
2. Switch between hourly, three-hour and daily aggregation.
3. Inspect the three charts.
4. Filter the article table by sentiment.
5. Search for a simple keyword such as outage, electricity or Texas.
6. Open an article through its Read News link and compare the headline with the prediction.

Our charts show article counts per predicted sentiment class. They do not show average confidence or incident severity. We group articles by collection time, fetched_at, rather than publication time. An initial collection batch can therefore create a spike even when the articles were published earlier.

The table filters do not change the cards or charts. The source column records Google News RSS rather than a verified original publisher identity.

Model Confidence is the model's output score, not a guarantee of correctness. The Operational Alert banner is static. Our current code does not automatically detect a spike or trigger the banner.

The search uses regular-expression matching. Simple search words are the easiest way to inspect titles.

## 10. What our code does

| File | Functions or settings | Role |
|---|---|---|
| src/config.py | KEYWORDS, RSS_URL, FETCH_INTERVAL_SECONDS, DATABASE_PATH | Defines topic keywords, the Google News feed, polling interval and database path. |
| src/fetch_stream.py | make_item_id(url) | Creates a SHA-256 identifier from a URL. |
| src/fetch_stream.py | matches_topic(text) | Checks whether a title contains a keyword, ignoring case. |
| src/fetch_stream.py | get_new_items(existing_ids) | Requests RSS with a 20-second timeout, parses entries, filters titles and returns new items. |
| src/analyze_sentiment.py | classifier and analyze(text) | Loads ProsusAI/finbert and returns a positive, neutral or negative label with a score rounded to four decimal places. |
| src/store_results.py | get_connection() | Creates the data directory if necessary and opens SQLite. |
| src/store_results.py | create_database() | Creates the pulse_items table if necessary. |
| src/store_results.py | get_existing_ids() | Reads stored item identifiers. |
| src/store_results.py | save_items(items) | Records UTC collection time and inserts new records using INSERT OR IGNORE. |
| src/run_pipeline.py | run_once() and main loop | Connects collection, sentiment analysis and storage, prints progress and repeats collection. |
| dashboard/app.py | load_data() | Reads SQLite records into pandas and prepares timestamps and display labels. |
| dashboard/app.py | make_area_series(subset, freq) | Counts articles in each selected time interval. |
| dashboard/app.py | Interface and filters | Displays cards, charts, the banner and an article table. |
| tests/calculate_accuracy.py | Label comparison | Calculates accuracy, per-class recall and a list of incorrect predictions. |
| tests/manual_labels.csv | Evaluation sample | Contains saved predictions and human labels. |
| tests/model_comparison.md | Evaluation report | Explains our results and discusses example errors. |

Additional implementation details:
- We analyse the first 512 characters of each title. This is character slicing, not token-based truncation.
- Deduplication works by URL. Different URLs covering the same story can still be stored.
- The database includes second_model_label and second_model_score fields, but our current pipeline only runs FinBERT.
- Collection-cycle exceptions are printed as Pipeline error messages. Model-loading errors can occur before that loop starts.

## 11. Data flow
```text
Google News RSS
    -> Keyword filtering and URL checks
    -> FinBERT headline classification
    -> SQLite database
    -> Streamlit dashboard
```

We store the title, URL, topic, source, timestamps, sentiment label and model score. The feed can provide Google News redirect links.

The collector updates the database. The dashboard reads it. Our evaluation CSV is separate and is not automatically updated by the collector.

Both config.py and app.py specify data/pulse.db. Update both if you change the database location.

## 12. Reproduce our evaluation
Run the accuracy script from the project root.

Windows:

```powershell
.\.venv\Scripts\python.exe tests/calculate_accuracy.py
```

macOS or Linux:

```bash
./.venv/bin/python tests/calculate_accuracy.py
```

The script uses saved predictions. It does not run FinBERT, fetch new articles or read the database.

Our CSV must contain id, title, finbert_label, finbert_score and ground_truth. The script recalculates agreement and does not use the agreement column.

Our fixed labeled sample produces:

| Measure | Result |
|---|---:|
| Evaluated headlines | 50 |
| Correct predictions | 33 |
| Incorrect predictions | 17 |
| Overall accuracy | 66.00% |
| Positive class recall | 2/6, 33.3% |
| Neutral class recall | 24/25, 96.0% |
| Negative class recall | 7/19, 36.8% |

Accuracy is the number of correct predictions divided by the number of evaluated headlines. The per-class percentages are recall, not precision: they measure how many human-labeled examples of each class were detected correctly.

For comparison, always predicting neutral would achieve 25/50, or 50.0%, on this sample. This reference is not the result of a second transformer model.

The script prints its output in Dutch. It does not export files or automatically update model_comparison.md. It assumes a nonempty CSV with complete and valid labels, so check the data before interpreting the results.

## 13. Limitations
Our sample contains only 50 headlines, including six positive examples. These results should not be treated as a guarantee of future performance.

Human labels depend on the interpretation and perspective used during labeling. A model error does not reveal the exact reason for the model's internal decision. Explanations in our error analysis should be understood as possible explanations.

Our results show many non-neutral headlines being classified as neutral. Strong neutral recall alone does not establish that negative alerts are reliable.

News coverage is not a representative survey of residents. Headlines may reflect company statements, journalistic framing or repeated coverage. Negative sentiment does not independently establish an outage or public resistance.

The negative-class miss rate applies to all 19 negative examples, not specifically to electricity-cost headlines. Our current dashboard does not implement a per-period low-count warning or automatic spike detection.

Collection targets such as 48 hours and 300 items should be assessed separately using database counts and collection timestamps. The 50-item evaluation is a different measurement.

## 14. Troubleshooting

| Problem | What to check |
|---|---|
| No module named src | Run from the project root and use the module command in Section 8. |
| Missing Python package | Install requirements.txt with the same environment interpreter used to run the app. |
| Python command is unavailable | Check the installed interpreter and whether your system uses py, python or python3. |
| Package version cannot be installed | Check the exact pip error, Python version and operating-system compatibility. Do not silently replace versions and assume identical results. |
| No data found yet | Run the collector and check data/pulse.db. There may be no new matching entries. |
| No such table: pulse_items | Run the collector to initialise the table. Back up existing data before making database changes. |
| Found 0 new matching items | Existing URLs are skipped, and keyword filtering can reject other entries. |
| RSS request fails | Check network access and RSS_URL in config.py. The continuous loop retries in a later cycle. |
| Model fails to load | Check package imports, Hugging Face access and the error message. Initial loading occurs before the collection loop. |
| New data is not visible | Check that both terminals use the same project root. Wait for cache expiry and reload or rerun the dashboard. |
| KeyError: ground_truth | Use the final human-labeled CSV rather than a prediction-only export. |
| Evaluation CSV is not found | Run from the project root and check tests/manual_labels.csv. |
| Search fails with punctuation | Try a simple word because the search interprets regular expressions. |
| A high-confidence prediction is wrong | Inspect the headline and human label. Confidence does not guarantee correctness. |

Our active feed is defined in src/config.py. If another document mentions Yahoo Finance, the current implementation uses Google News RSS. Use the collector command in this guide to match our imports.

## 15. Reproducibility
Our evaluation should produce the same results when the labeled CSV is unchanged. Live collection results can differ because the RSS feed changes over time.

The setup instructions do not guarantee identical operation on every computer. Use our pinned dependencies and check the troubleshooting section if installation or startup differs in your environment.
