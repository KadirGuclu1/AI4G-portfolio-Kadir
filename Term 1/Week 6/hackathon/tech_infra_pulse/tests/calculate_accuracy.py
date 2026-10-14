import pandas as pd

# 1. Laad het CSV bestand met de labels
df = pd.read_csv("tests/manual_labels.csv")

# Schoon kolomnamen en spaties op
df.columns = df.columns.str.strip()
df["finbert_label"] = df["finbert_label"].astype(str).str.strip().str.lower()
df["ground_truth"] = df["ground_truth"].astype(str).str.strip().str.lower()

# 2. Bereken de overeenkomsten
df["correct"] = df["finbert_label"] == df["ground_truth"]

total_items = len(df)
correct_items = df["correct"].sum()
accuracy = (correct_items / total_items) * 100

print("=" * 55)
print(f"       MODEL ACCURACY REPORT: ProsusAI/finbert")
print("=" * 55)
print(f"Totaal geteste artikelen : {total_items}")
print(f"Correct voorspeld        : {correct_items}")
print(f"Foutief voorspeld        : {total_items - correct_items}")
print(f"Totale Accuratesse       : {accuracy:.2f}%")
print("=" * 55)

# 3. Accuratesse per Ground Truth klasse
print("\n--- PRESTATIES PER KLASSE (Ground Truth) ---")
for sentiment in ["positive", "neutral", "negative"]:
    subset = df[df["ground_truth"] == sentiment]
    if len(subset) > 0:
        cat_correct = subset["correct"].sum()
        cat_acc = (cat_correct / len(subset)) * 100
        print(
            f"{sentiment.capitalize():<10} : {cat_correct}/{len(subset)} correct ({cat_acc:.1f}%)"
        )

# 4. Overzicht van alle foute voorspellingen
print("\n--- OVERZICHT VAN FOUTIEVE VOORSPELLINGEN ---")
fouten = df[~df["correct"]]
for idx, row in fouten.iterrows():
    print(f"ID #{row['id']}:")
    print(f"  Titel       : {row['title']}")
    print(
        f"  Verwacht    : {row['ground_truth']} | Voorspeld: {row['finbert_label']} (Score: {row['finbert_score']})"
    )
    print("-" * 55)