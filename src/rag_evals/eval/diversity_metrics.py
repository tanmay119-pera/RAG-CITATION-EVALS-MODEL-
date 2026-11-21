"""Measure retrieval diversity across sources and vocabulary."""
from typing import List, Dict

class DiversityScorer:
    """Calculates source diversity and vocabulary redundancy for retrieved chunks."""
    def source_diversity(self, chunks: List[Dict]) -> float:
        if not chunks:
            return 0.0
        sources = [c.get("source", "") for c in chunks]
        return len(set(sources)) / len(sources)

    def content_diversity(self, chunks: List[Dict]) -> float:
        words = []
        for c in chunks:
            words.extend(c.get("text", "").lower().split())
        if not words:
            return 0.0
        return len(set(words)) / len(words)

    def report(self, chunks: List[Dict]) -> Dict[str, float]:
        return {
            "source_diversity": round(self.source_diversity(chunks), 4),
            "content_diversity": round(self.content_diversity(chunks), 4),
        }
