"""Pure-Python numerical helpers for similarity and IR metrics."""
import math
from typing import Sequence

def dot_product(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))

def l2_norm(vec: Sequence[float]) -> float:
    return math.sqrt(sum(x * x for x in vec))

def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    denom = l2_norm(a) * l2_norm(b)
    return dot_product(a, b) / denom if denom > 0 else 0.0

def reciprocal_rank(ranked_ids: Sequence[str], relevant_ids: set) -> float:
    for idx, item in enumerate(ranked_ids, start=1):
        if item in relevant_ids:
            return 1.0 / idx
    return 0.0
