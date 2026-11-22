"""Evaluate intrinsic quality of ingested chunks."""
from typing import Dict, Any

class ChunkQualityScorer:
    """Evaluates length balance, vocabulary richness, and metadata completeness."""
    def score(self, chunk: Dict) -> Dict[str, float]:
        text = chunk.get("text", "")
        words = text.split()
        wc = len(words)
        len_score = 1.0 if 30 <= wc <= 500 else max(0.2, min(wc / 30.0, 500.0 / max(wc, 1)))
        uniq = len(set(w.lower() for w in words))
        vocab_score = uniq / max(wc, 1)
        has_src = 1.0 if chunk.get("source") else 0.0
        overall = len_score * 0.4 + vocab_score * 0.4 + has_src * 0.2
        return {
            "overall": round(overall, 4),
            "length_score": round(len_score, 4),
            "vocab_score": round(vocab_score, 4),
            "has_source": has_src,
        }

    def batch_score(self, chunks: list) -> list:
        return [{"chunk_id": c.get("chunk_id", f"c{i}"), **self.score(c)} for i, c in enumerate(chunks)]
