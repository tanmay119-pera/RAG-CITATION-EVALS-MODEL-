"""Positional context precision calculator over retrieved chunk lists."""
from typing import List, Set

class ContextPrecisionEvaluator:
    """Computes Average Precision emphasizing relevant chunks ranked near top."""

    @staticmethod
    def average_precision(retrieved_ids: List[str], relevant_ids: Set[str]) -> float:
        if not retrieved_ids or not relevant_ids:
            return 0.0
        hits = 0
        precision_sum = 0.0
        for rank, cid in enumerate(retrieved_ids, start=1):
            if cid in relevant_ids:
                hits += 1
                precision_sum += hits / rank
        return round(precision_sum / len(relevant_ids), 4)
