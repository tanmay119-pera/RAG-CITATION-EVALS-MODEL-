"""Persistent SQLite embedding cache to prevent duplicate API calls."""

import sqlite3
import json
import hashlib
from pathlib import Path
from typing import Optional, List

class EmbeddingCache:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS embeddings (
                    hash_key TEXT PRIMARY KEY,
                    embedding_json TEXT
                )
            """)

    @staticmethod
    def _make_key(text: str, model_name: str) -> str:
        data = f"{model_name}:{text}".encode("utf-8")
        return hashlib.sha256(data).hexdigest()

    def get(self, text: str, model_name: str) -> Optional[List[float]]:
        key = self._make_key(text, model_name)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("SELECT embedding_json FROM embeddings WHERE hash_key = ?", (key,)).fetchone()
            if row:
                return json.loads(row[0])
        return None

    def put(self, text: str, model_name: str, embedding: List[float]):
        key = self._make_key(text, model_name)
        val = json.dumps(embedding)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT OR REPLACE INTO embeddings VALUES (?, ?)", (key, val))
