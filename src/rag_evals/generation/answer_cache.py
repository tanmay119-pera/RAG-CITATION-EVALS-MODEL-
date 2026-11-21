"""Persistent file-based cache for generated answers with citations."""
import hashlib, json, time
from pathlib import Path
from typing import Optional, Dict

class AnswerCache:
    """Local cache with TTL expiration for LLM-generated responses."""
    def __init__(self, cache_dir: str = "data/cache/answers", ttl_seconds: float = 86400):
        self.cache_dir = Path(cache_dir)
        self.ttl = ttl_seconds

    def _path(self, query: str) -> Path:
        h = hashlib.sha256(query.strip().lower().encode("utf-8")).hexdigest()[:20]
        return self.cache_dir / f"{h}.json"

    def get(self, query: str) -> Optional[Dict]:
        p = self._path(query)
        if not p.exists():
            return None
        data = json.loads(p.read_text())
        if time.time() - data.get("cached_at", 0) > self.ttl:
            p.unlink(missing_ok=True)
            return None
        return data

    def put(self, query: str, answer: str, citations: list):
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        p = self._path(query)
        data = {"query": query, "answer": answer, "citations": citations, "cached_at": time.time()}
        p.write_text(json.dumps(data, indent=2))
