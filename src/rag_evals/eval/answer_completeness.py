"""Evaluate completeness of answers against required factual points."""
from typing import List

class CompletenessScorer:
    """Measures fraction of expected factual nuggets present in response."""

    @staticmethod
    def score(answer: str, required_facts: List[str]) -> float:
        if not required_facts:
            return 1.0
        low = answer.lower()
        covered = sum(1 for f in required_facts if f.lower() in low)
        return round(covered / len(required_facts), 4)
