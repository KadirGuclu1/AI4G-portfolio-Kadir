# Ethical Reflection (SDG 9 Live Pulse)

## 1. Our User and Context
Our project is built for a Digital Infrastructure Policy Officer at a local municipality. The goal is to follow live news about data centers, the power grid, cloud outages and telecom networks under UN SDG 9 (Industry, Innovation and Infrastructure).

The policy officer uses our dashboard to see if media attention or public worry about energy use and digital infrastructure is rising. Because decisions made by a municipality affect real citizens, local businesses and power grids, we must be honest about what our AI model can and cannot do.

---

## 2. Who is Heard and Who is Missing?

### Media Focus vs. Real Citizens
Our data comes from Google News RSS. This gives us articles from newspapers, financial outlets and corporate press releases. This creates a clear bias in our data:
* **Companies and investors get a lot of attention:** Big investments, AI data center plans and new technology are reported quickly.
* **Normal citizens are underrepresented:** Local residents who deal with noise from data centers, power cuts or higher energy bills do not write news feeds. We only see their problems if a journalist decides to write an article about them.
* **Language barrier:** Our stream only collects English news. Local Dutch municipal debates, local petitions and neighborhood complaints are not in the dataset.

**Our takeaway:** The dashboard shows what journalists and financial media write. It does not measure direct public opinion or citizen satisfaction.

---

## 3. What Did We Learn from Our Model Test?

When we tested FinBERT on 50 real headlines from our live stream, we noticed an important bias:
* **Great at neutral news (96.0% accuracy):** When an article is purely factual (like a government bill or a technical report), FinBERT almost always labels it as neutral. It does not create false alarms on normal industry news.
* **Struggles with citizen costs (36.8% recall on negative news):** When headlines talk about higher electricity bills for households (for example: *"How much are AI data centers adding to your electricity bill? - NPR"*), FinBERT calls it neutral with high confidence (>90%).

### Why is this an ethical issue?
FinBERT was trained on financial market news. For a stock trader or company, rising energy costs are just normal market dynamics (neutral). But for a municipal policy officer and for local residents, a higher energy bill is clearly a negative problem.

If the policy officer only looks at the overall sentiment graph, they might think everything is calm and neutral, while residents are actually worried about their costs.

### How did we solve this in our dashboard?
1. We placed an alert banner on top of the dashboard reminding the officer that AI sentiment scores have blindspots.
2. We built an interactive search table with links. The officer can search for keywords like *"bills"* or *"rates"* and read the original articles themselves instead of trusting the AI blindly.

---

## 4. Privacy and Data Usage

* **No personal data:** We only store public news titles, website links, source names and timestamps in our SQLite database.
* **No tracking:** We do not track authors, social media profiles or individual people.
* **Clean data:** We hash URLs with SHA-256 so duplicate articles are not processed twice.

---

## 5. Human-in-the-Loop Rules

To use this tool responsibly, we set three clear rules:
1. **AI gives a signal, humans make the decision:** The dashboard is an investigation tool. A rise in negative news should never lead to policy decisions without human review.
2. **Always check the source:** The policy officer must click on the article link in the table to verify what is actually happening.
3. **Show uncertainty:** We display the confidence score of the model in the table so the user knows when the model is less certain about a headline.
