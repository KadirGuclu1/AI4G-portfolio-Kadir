import os
import sqlite3
from datetime import datetime, timezone

from src.config import DATABASE_PATH


def get_connection():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS pulse_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id TEXT UNIQUE,
                title TEXT,
                url TEXT,
                source TEXT,
                topic TEXT,
                published_at TEXT,
                fetched_at TEXT,
                sentiment_label TEXT,
                sentiment_score REAL,
                second_model_label TEXT,
                second_model_score REAL
            )
            """
        )


def get_existing_ids() -> set[str]:
    create_database()

    with get_connection() as connection:
        rows = connection.execute("SELECT item_id FROM pulse_items").fetchall()

    return {row["item_id"] for row in rows}


def save_items(items: list[dict]):
    create_database()
    fetched_at = datetime.now(timezone.utc).isoformat()

    with get_connection() as connection:
        for item in items:
            connection.execute(
                """
                INSERT OR IGNORE INTO pulse_items (
                    item_id, title, url, source, topic,
                    published_at, fetched_at,
                    sentiment_label, sentiment_score,
                    second_model_label, second_model_score
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item["item_id"],
                    item["title"],
                    item["url"],
                    item["source"],
                    item["topic"],
                    item.get("published_at", ""),
                    fetched_at,
                    item.get("sentiment_label", ""),
                    item.get("sentiment_score"),
                    item.get("second_model_label", ""),
                    item.get("second_model_score"),
                ),
            )
