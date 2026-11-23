"""Sentence-level contextual chunk compressor."""
import re
from typing import List, Dict

class ContextualSentenceCompressor:
    """Strips sentences from retrieved chunks that have zero keyword overlap with query."""
    def __init__(self, min_length: int = 15):
        self.min_length = min_length

    def compress_chunk(self, query: str, text: str) -> str:
        q_tokens = set(re.findall(r"\w+", query.lower()))
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
        relevant = []
        for s in sentences:
            s_tokens = set(re.findall(r"\w+", s.lower()))
            if q_tokens & s_tokens or len(s) < self.min_length:
                relevant.append(s)
        return " ".join(relevant) if relevant else text

    def compress(self, query: str, chunks: List[Dict]) -> List[Dict]:
        out = []
        for c in chunks:
            c_copy = dict(c)
            c_copy["text"] = self.compress_chunk(query, c.get("text", ""))
            out.append(c_copy)
        return out
