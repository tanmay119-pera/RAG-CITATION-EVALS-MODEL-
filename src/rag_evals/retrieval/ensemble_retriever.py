"""Weighted ensemble retriever across multiple search backends."""
from typing import List, Dict, Callable
from collections import defaultdict

class EnsembleRetriever:
    """Fuses results from multiple retrievers using weighted linear combination."""
    def __init__(self, retrievers: List[tuple]): # list of (retriever_fn, weight)
        self.retrievers = retrievers

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        combined_scores = defaultdict(float)
        meta_lookup = {}
        for fn, weight in self.retrievers:
            results = fn(query, top_k * 2)
            for r in results:
                cid = r.get("chunk_id", "")
                combined_scores[cid] += r.get("score", 1.0) * weight
                if cid not in meta_lookup:
                    meta_lookup[cid] = r

        fused = []
        for cid, score in sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]:
            item = dict(meta_lookup[cid])
            item["score"] = round(score, 4)
            fused.append(item)
        return fused
