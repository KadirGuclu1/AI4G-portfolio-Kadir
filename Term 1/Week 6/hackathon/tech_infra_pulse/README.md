# Technology & Infrastructure Live Pulse

A continuous sentiment monitoring pipeline and interactive Streamlit dashboard that tracks news coverage regarding critical digital and energy infrastructure (SDG 9), analyzes headlines using a pre-trained financial transformer (`ProsusAI/finbert`), and visualizes trends over time.

For an in-depth technical walkthrough, evaluation instructions, and step-by-step setup commands for evaluators, refer to [TEACHER_GUIDE.md](TEACHER_GUIDE.md).

---

## 1. SDG Alignment & Problem Framing

This project supports **United Nations Sustainable Development Goal 9: Industry, Innovation and Infrastructure**.

Modern technological advancements such as artificial intelligence and cloud computing place unprecedented strain on energy grids, telecommunication networks, and regional utility infrastructure. This system provides automated continuous monitoring of public news streams to detect emerging risks, factual policy developments, and positive infrastructural milestones.

* **Target User:** Digital Infrastructure Policy Officer at a municipal or regional authority.
* **Decision Supported:** Monitoring whether public scrutiny, grid capacity constraints, or outage reports are escalating. A sudden surge in negative coverage prompts the officer to investigate source articles in the dashboard table, brief department leads, or coordinate utility communications before public escalations occur.

---

## 2. Live Data Stream

* **Source:** Continuous Google News RSS Search Feed (`https://news.google.com/rss/search`).
* **Search Query:** `(data center OR cloud OR 5G OR power outage OR electricity grid OR telecom) infrastructure`
* **Polling Interval:** Every 10 minutes (`600` seconds).
* **Filtering Logic:** Case-insensitive keyword matching against technical domain terms (`data center`, `electric grid`, `cloud outage`, `5G`, `broadband`, `power outage`, etc.).
* **Deduplication:** SHA-256 URL hashing ensures articles are processed and stored exactly once.

---

## 3. Machine Learning Model & Setup

* **Primary Model:** `ProsusAI/finbert` (Hugging Face Transformers)
* **Architecture:** BERT fine-tuned on financial and corporate news (*Financial PhraseBank*).
* **Classes:** `positive`, `neutral`, `negative`.
* **Selection Rationale:** Infrastructure planning and utility investments are reported through factual, industrial, and economic phrasing. FinBERT reliably identifies descriptive governance announcements as `neutral` without triggering false alarms.

---

## 4. System Architecture & Workflow

```text
[Google News RSS Stream]
         │
         ▼
[fetch_stream.py] ──> Keyword Filter & SHA-256 URL Deduplication
         │
         ▼
[analyze_sentiment.py] ──> ProsusAI/finbert Headline Classification
         │
         ▼
[store_results.py] ──> SQLite Database (`data/pulse.db`)
         │
         ▼
[dashboard/app.py] ──> Streamlit UI (Metrics, Area Charts, Search & Filter Table)
```

---

## 5. Quickstart & Installation

### Prerequisites
* Python 3.10+
* Virtual environment (`.venv`)

### Installation Commands

#### Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

#### macOS / Linux (Bash)
```bash
python3 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
```

---

## 6. Running the Application

### Option A: Launch Dashboard (Inspect Existing Data)
To inspect the historical dataset saved in `data/pulse.db`:

```powershell
# Windows
.\.venv\Scripts\python.exe -m streamlit run dashboard/app.py

# macOS / Linux
./.venv/bin/python -m streamlit run dashboard/app.py
```

### Option B: Run Continuous Pipeline (Collector + Dashboard)
Open two separate terminals from the project root:

* **Terminal 1 (Collector):**
  ```powershell
  python -m src.run_pipeline
  ```
* **Terminal 2 (Dashboard):**
  ```powershell
  python -m streamlit run dashboard/app.py
  ```

---

## 7. Model Evaluation & Honest Benchmark

We evaluated `ProsusAI/finbert` against 50 manually labeled headlines collected by our live stream (`tests/manual_labels.csv`).

To run the automated accuracy evaluation script:
```powershell
python tests/calculate_accuracy.py
```

### Evaluation Summary
* **Total Evaluated Items:** 50
* **Correct Predictions:** 33 / 50 (**66.00% Accuracy**)
* **Neutral Recall:** 24 / 25 (**96.0%**) -> Strong performance on factual infrastructure and policy reporting.
* **Negative Recall:** 7 / 19 (**36.8%**) -> Known neutrality bias on headlines regarding household utility bill burdens and ratepayer costs.
* **Positive Recall:** 2 / 6 (**33.3%**)

Detailed error analyses and operational safeguards are documented in [tests/model_comparison.md](tests/model_comparison.md).

---

## 8. Ethical Considerations & Limitations

1. **News Framing Bias:** RSS headlines predominantly reflect journalistic and corporate perspectives rather than direct citizen feedback or marginalized groups.
2. **Neutrality Bias on Consumer Costs:** FinBERT was pre-trained on corporate financial text, frequently classifying rising residential electricity rates as neutral macroeconomic questions rather than citizen burdens.
3. **Decision Support Only:** The dashboard is explicitly designed as an alert and exploration tool. Automated sentiment scores must never trigger municipal actions without manual verification of source articles.
4. **Data Privacy:** Only public article metadata (title, URL, source, timestamp) is stored. No personal user data or author tracking is performed.