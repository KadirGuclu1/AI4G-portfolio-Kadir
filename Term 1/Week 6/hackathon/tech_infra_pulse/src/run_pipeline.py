import time

from src.config import FETCH_INTERVAL_SECONDS
from src.analyze_sentiment import analyze
from src.fetch_stream import get_new_items
from src.store_results import get_existing_ids, save_items


def run_once():
    existing_ids = get_existing_ids()
    items = get_new_items(existing_ids)

    print(f"Found {len(items)} new matching items.")

    for item in items:
        sentiment = analyze(item["title"])
        item.update(sentiment)
        save_items([item])
        print(f"Saved: {item['title']} -> {item['sentiment_label']}")


if __name__ == "__main__":
    while True:
        try:
            run_once()
        except Exception as error:
            print(f"Pipeline error: {error}")

        time.sleep(FETCH_INTERVAL_SECONDS)
