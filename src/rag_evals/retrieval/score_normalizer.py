"""Normalize heterogeneous BM25 and dense cosine similarity scores."""
import math
from typing import List

class ScoreNormalizer:
    """Scales retrieval scores prior to weighted fusion."""

    @staticmethod
    def min_max(scores: List[float]) -> List[float]:
        if not scores:
            return []
        lo, hi = min(scores), max(scores)
        if hi == lo:
            return [1.0 for _ in scores]
        return [round((s - lo) / (hi - lo), 4) for s in scores]

    @staticmethod
    def z_score(scores: List[float]) -> List[float]:
        if not scores:
            return []
        mean = sum(scores) / len(scores)
        var = sum((s - mean) ** 2 for s in scores) / len(scores)
        std = math.sqrt(var)
        return [0.0 for _ in scores] if std == 0 else [round((s - mean) / std, 4) for s in scores]
