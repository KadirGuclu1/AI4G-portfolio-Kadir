from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert",
)


def analyze(text: str) -> dict:
    result = classifier(
        text,
        truncation=True,
        max_length=512,
    )[0]

    return {
        "sentiment_label": result["label"].lower(),
        "sentiment_score": round(float(result["score"]), 4),
    }