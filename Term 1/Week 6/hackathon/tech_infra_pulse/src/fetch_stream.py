import hashlib
import feedparser
import requests

from src.config import KEYWORDS, RSS_URL


def make_item_id(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def matches_topic(text: str) -> bool:
    text = text.lower()
    return any(keyword.lower() in text for keyword in KEYWORDS)


def get_new_items(existing_ids: set[str]) -> list[dict]:
    response = requests.get(
        RSS_URL,
        timeout=20,
        headers={"User-Agent": "TechInfrastructurePulse/1.0"},
    )
    response.raise_for_status()

    feed = feedparser.parse(response.content)
    items = []

    for entry in feed.entries:
        url = entry.get("link", "")
        title = entry.get("title", "").strip()

        if not url or not title:
            continue

        item_id = make_item_id(url)

        if item_id in existing_ids:
            continue

        if not matches_topic(title):
            continue

        items.append(
            {
                "item_id": item_id,
                "title": title,
                "url": url,
                "source": "Google News RSS",
                "topic": "technology_infrastructure",
                "published_at": entry.get("published", ""),
            }
        )

    return items