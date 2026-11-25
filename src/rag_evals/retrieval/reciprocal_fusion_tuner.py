"""Reciprocal Rank Fusion (RRF) constant k tuner."""
from typing import List, Dict
from collections import defaultdict

class RRFTuner:
    """Fuses ranked ID lists with parameterized RRF constant k."""

    @staticmethod
    def fuse(ranked_lists: List[List[str]], k: int = 60) -> List[str]:
        scores: Dict[str, float] = defaultdict(float)
        for rlist in ranked_lists:
            for rank, doc_id in enumerate(rlist, start=1):
                scores[doc_id] += 1.0 / (k + rank)
        return [doc_id for doc_id, _ in sorted(scores.items(), key=lambda item: item[1], reverse=True)]
