"""Detect and eliminate near-duplicate chunks."""
import hashlib
from typing import List, Dict, Tuple
from difflib import SequenceMatcher

class ChunkDeduplicator:
    """Exact and fuzzy deduplication for ingested text chunks."""
    def __init__(self, similarity_threshold: float = 0.90):
        self.threshold = similarity_threshold

    def _hash(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def exact_dedup(self, chunks: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
        seen = {}
        unique, dupes = [], []
        for c in chunks:
            h = self._hash(c.get("text", ""))
            if h in seen:
                dupes.append(c)
            else:
                seen[h] = True
                unique.append(c)
        return unique, dupes

    def fuzzy_dedup(self, chunks: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
        unique, dupes = [], []
        for c in chunks:
            is_dup = False
            for u in unique:
                sim = SequenceMatcher(None, c.get("text", ""), u.get("text", "")).ratio()
                if sim >= self.threshold:
                    is_dup = True
                    break
            if is_dup:
                dupes.append(c)
            else:
                unique.append(c)
        return unique, dupes

    def dedup(self, chunks: List[Dict], fuzzy: bool = False) -> Tuple[List[Dict], List[Dict]]:
        return self.fuzzy_dedup(chunks) if fuzzy else self.exact_dedup(chunks)
