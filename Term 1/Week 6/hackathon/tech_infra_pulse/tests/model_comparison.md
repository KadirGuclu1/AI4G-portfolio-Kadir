# Model Evaluation & Honest Test (SDG 9 Live Pulse)

## 1. Test Setup & Accuracy Benchmark

We evaluated **50 real headlines** collected by our live stream against human ground-truth labels using `tests/calculate_accuracy.py`.
=======================================================
MODEL ACCURACY REPORT: ProsusAI/finbert
=======================================================
Totaal geteste artikelen : 50
Correct voorspeld : 33
Foutief voorspeld : 17
Totale Accuratesse : 66.00%
=======================================================

--- PRESTATIES PER KLASSE (Ground Truth) ---
Positive : 2 / 6 correct (33.3%)
Neutral : 24 / 25 correct (96.0%)
Negative : 7 / 19 correct (36.8%)

---

## 2. Key Findings: Where the Model Succeeds and Fails

### Primary Strength: Near-Perfect Neutral Detection (96.0%)
FinBERT accurately identifies factual industry and governance reports without generating false alarms. Out of 25 neutral infrastructure headlines, 24 were correctly classified.

### Primary Weakness: Neutrality Bias on Household Utility Strain (36.8% on Negative)
Because FinBERT was pre-trained on corporate financial news (*Financial PhraseBank*), it interprets articles discussing rising electricity costs (*"How much are AI data centers adding to your electricity bill?"*) as routine macroeconomic questions rather than negative signals for citizens.

---

## 3. Detailed Analysis of Notable Failures

### Failure 1: Consumer Cost Strain Misclassified as Neutral (Item #2 & #15)
- **Headline:** *"How much are AI data centers adding to your electricity bill? - NPR"*
- **Ground Truth:** `negative`
- **FinBERT Prediction:** `neutral` (Confidence: 0.9240)
- **Explanation:** The headline discusses utility cost burdens on households. Because it is phrased as an analytical question without aggressive adjectives, FinBERT assigns it a high neutral probability.

### Failure 2: Infrastructure Moratorium & Grid Bottleneck (Item #18 & #27)
- **Headline:** *"Texas Pauses Data Center Construction - The Institute for Energy Research"*
- **Ground Truth:** `negative` (Project halt due to grid capacity constraints)
- **FinBERT Prediction:** `neutral` (Confidence: 0.9067)
- **Explanation:** Halting construction is an operational disruption, but FinBERT interprets the corporate announcement purely as a factual regulatory status.

### Failure 3: Technological Breakthrough Overlooked (Item #1)
- **Headline:** *"Data centers' 'flexible' power usage could save the grid billions. Can they scale? - Reuters"*
- **Ground Truth:** `positive` (Innovation mitigating grid strain and saving capital)
- **FinBERT Prediction:** `neutral` (Confidence: 0.8578)
- **Explanation:** The positive benefit (*"save the grid billions"*) is tempered by a cautious query (*"Can they scale?"*), leading the model to default to `neutral`.

---

## 4. Operational Recommendation for the Policy Officer

1. **Rely on the Red Monitor for Incident Surges:** When the red monitor spikes, the underlying events are genuinely severe outages or policy actions (e.g., Google Cloud outages, statewide moratoriums).
2. **Account for Under-Reported Public Resistance:** Because FinBERT misses ~63% of negative cost-related headlines by labeling them neutral, the policy officer must actively search keywords like *"bills"* or *"rates"* in the interactive table rather than trusting the automated summary line alone.