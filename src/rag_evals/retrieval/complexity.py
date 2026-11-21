"""Estimate query linguistic complexity to tune retrieval depth."""
import re
from typing import Dict, Any

class QueryComplexityEstimator:
    """Scores query complexity to select optimal top_k and reranking depth."""
    def estimate(self, query: str) -> Dict[str, Any]:
        words = query.strip().split()
        wc = len(words)
        has_compare = bool(re.search(r"\b(compare|vs|versus|difference)\b", query.lower()))
        score = 1
        if wc > 12: score += 1
        if wc > 25: score += 1
        if has_compare: score += 1
        return {
            "score": min(score, 5),
            "word_count": wc,
            "has_comparison": has_compare,
            "recommended_top_k": 4 + min(score, 5) * 2,
        }
