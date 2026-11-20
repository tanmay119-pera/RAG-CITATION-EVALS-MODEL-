"""Classify query intent to dynamically guide retrieval."""
import re
from enum import Enum

class QueryIntent(Enum):
    FACTUAL = "factual"
    COMPARISON = "comparison"
    PROCEDURAL = "procedural"
    DEFINITION = "definition"
    UNANSWERABLE = "unanswerable"

_COMPARISON_PATTERNS = [r"\bcompare\b", r"\bdifference\b", r"\bvs\.?\b", r"\bversus\b"]
_PROCEDURAL_PATTERNS = [r"\bhow to\b", r"\bsteps?\b", r"\bprocess\b", r"\bprocedure\b"]
_DEFINITION_PATTERNS = [r"\bwhat is\b", r"\bdefine\b", r"\bdefinition\b", r"\bmeans?\b"]

class IntentClassifier:
    """Rule-based query intent classifier."""
    def classify(self, query: str) -> QueryIntent:
        q = query.lower().strip()
        if not q:
            return QueryIntent.UNANSWERABLE
        for pat in _COMPARISON_PATTERNS:
            if re.search(pat, q):
                return QueryIntent.COMPARISON
        for pat in _PROCEDURAL_PATTERNS:
            if re.search(pat, q):
                return QueryIntent.PROCEDURAL
        for pat in _DEFINITION_PATTERNS:
            if re.search(pat, q):
                return QueryIntent.DEFINITION
        return QueryIntent.FACTUAL

    def route_top_k(self, intent: QueryIntent) -> int:
        mapping = {
            QueryIntent.FACTUAL: 5,
            QueryIntent.COMPARISON: 10,
            QueryIntent.PROCEDURAL: 7,
            QueryIntent.DEFINITION: 3,
            QueryIntent.UNANSWERABLE: 0,
        }
        return mapping.get(intent, 5)
