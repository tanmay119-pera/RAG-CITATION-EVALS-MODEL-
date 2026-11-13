"""Lightweight tokenization and N-gram helpers."""
import re
from typing import List, Tuple

class SimpleTokenizer:
    """Stateless word, sentence, and N-gram tokenizer."""

    @staticmethod
    def tokenize_words(text: str) -> List[str]:
        return re.findall(r"\b[a-zA-Z0-9_-]+\b", text.lower())

    @staticmethod
    def split_sentences(text: str) -> List[str]:
        return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]

    @classmethod
    def word_ngrams(cls, text: str, n: int = 2) -> List[Tuple[str, ...]]:
        words = cls.tokenize_words(text)
        if n <= 0 or len(words) < n:
            return []
        return [tuple(words[idx:idx + n]) for idx in range(len(words) - n + 1)]
