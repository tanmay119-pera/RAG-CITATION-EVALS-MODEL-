"""Calculate descriptive statistics for indexed corpora."""
import math
from typing import List, Dict, Any

class IndexStatistics:
    """Gathers length, vocabulary, and distribution metrics for document chunks."""
    def chunk_stats(self, chunks: List[Dict]) -> Dict[str, Any]:
        if not chunks:
            return {"count": 0, "avg_words": 0.0}
        lens = [len(c.get("text", "").split()) for c in chunks]
        avg = sum(lens) / len(lens)
        var = sum((x - avg)**2 for x in lens) / max(len(lens) - 1, 1)
        return {
            "count": len(chunks),
            "avg_words": round(avg, 2),
            "min_words": min(lens),
            "max_words": max(lens),
            "std_words": round(math.sqrt(var), 2),
        }

    def source_distribution(self, chunks: List[Dict]) -> Dict[str, int]:
        dist = {}
        for c in chunks:
            src = c.get("source", "unknown")
            dist[src] = dist.get(src, 0) + 1
        return dict(sorted(dist.items(), key=lambda x: x[1], reverse=True))

    def report(self, chunks: List[Dict]) -> Dict[str, Any]:
        return {
            "chunk_statistics": self.chunk_stats(chunks),
            "source_distribution": self.source_distribution(chunks),
        }
