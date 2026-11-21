"""Manage context packing within LLM token constraints."""
from typing import List, Dict, Tuple

class ContextWindowManager:
    """Packs top retrieved chunks into prompt budget without overflowing context."""
    def __init__(self, max_tokens: int = 3000, reserved_tokens: int = 500):
        self.max_tokens = max_tokens
        self.reserved = reserved_tokens
        self.available = max_tokens - reserved_tokens

    def _estimate(self, text: str) -> int:
        return int(len(text.split()) * 1.3)

    def pack(self, chunks: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
        included, excluded = [], []
        used = 0
        for c in chunks:
            tok = self._estimate(c.get("text", ""))
            if used + tok <= self.available:
                included.append(c)
                used += tok
            else:
                excluded.append(c)
        return included, excluded

    def format_context(self, chunks: List[Dict]) -> str:
        return "\n\n".join([f"[{c.get('chunk_id', i)}] {c.get('text', '')}" for i, c in enumerate(chunks)])
