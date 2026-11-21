"""Collect and apply user relevance feedback."""
import time
from typing import List, Dict
from collections import defaultdict

class RelevanceFeedback:
    """Manages implicit and explicit relevance judgments to re-weight chunks."""
    def __init__(self):
        self.history: List[Dict] = []

    def record(self, query: str, chunk_id: str, is_relevant: bool):
        self.history.append({"query": query, "chunk_id": chunk_id, "relevant": is_relevant, "ts": time.time()})

    def get_boost_map(self) -> Dict[str, float]:
        boosts = defaultdict(float)
        for h in self.history:
            boosts[h["chunk_id"]] += 0.2 if h["relevant"] else -0.2
        return dict(boosts)

    def apply_boosts(self, results: List[Dict]) -> List[Dict]:
        boosts = self.get_boost_map()
        for r in results:
            cid = r.get("chunk_id", "")
            r["score"] = r.get("score", 0.0) + boosts.get(cid, 0.0)
        return sorted(results, key=lambda x: x.get("score", 0.0), reverse=True)
