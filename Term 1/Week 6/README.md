# Term 1 - Week 6: Language Models

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?**

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ ] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:** Technology & Infrastructure Live Pulse (SDG 9)

**My pair partner:** Joe Navarro Munté

**Tool we had to use:** Python, Streamlit, Hugging Face Transformers (`ProsusAI/finbert`), SQLite, Google News RSS

**SDG we had to address:** SDG 9: Industry, Innovation and Infrastructure

**What problem does it solve, and for whom?**
It helps a Digital Infrastructure Policy Officer at a local municipality monitor continuous media signals and public attention around data centers, power grids, cloud outages and telecom networks. Instead of reading hundreds of articles manually, the officer gets a real-time overview of infrastructure news trends.

**What did you build?**
We built an automated data stream that fetches live infrastructure news every 10 minutes via RSS, filters them with technical keywords, and scores headline sentiment using FinBERT. We built an interactive dark-themed Streamlit dashboard with time-series charts, metric cards, and a searchable table where the policy officer can click directly to the original news articles.

**Link to the live thing (if any):**
Local live demo running via Streamlit (`http://localhost:8501`), with source code and evaluation files in our GitHub repository.

**How do I run it?**
1. Install requirements: `pip install -r requirements.txt`
2. Start the continuous collector in Terminal 1: `python -m src.run_pipeline`
3. Launch the dashboard in Terminal 2: `python -m streamlit run dashboard/app.py`
4. Run the accuracy benchmark: `python tests/calculate_accuracy.py`

**Who did what?**
* **Partner:** Built the RSS feed collector (`fetch_stream.py`), SQLite database storage (`store_results.py`), and the continuous background loop.
* **Me:** Implemented the FinBERT sentiment analysis pipeline (`analyze_sentiment.py`), designed the Streamlit dashboard with custom CSS (`app.py`), and conducted the 50-item manual evaluation benchmark (`tests/calculate_accuracy.py` and `tests/model_comparison.md`).

**Ethical reflection - what are the risks of your tool? Who could it harm?**
Our RSS stream mostly captures journalists and corporate press releases, not ordinary citizens. In our honest benchmark of 50 headlines, FinBERT showed a neutrality bias: it scored 96% on neutral factual news, but missed 63% of negative headlines concerning household electricity bills because it was trained on corporate financial news. If a policy officer relies only on the sentiment graph, they could miss rising citizen frustration about energy costs. That is why our dashboard includes an alert banner and forces the user to verify original articles in the interactive table before making policy decisions.

### Checklist
- [x] Prototype code (or export / workflow file) is in `hackathon/`
- [x] This week's slides are in `hackathon/`
- [x] The prototype actually runs, and I wrote down how to run it
- [x] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [ ] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?**

---

## 4. Reflection

**What is the most important thing I learned this week?**

**Where does this connect to "AI for Good"?**
_One concrete link to ethics, sustainability or social impact._
