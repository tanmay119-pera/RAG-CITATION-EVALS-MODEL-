"""Deterministic hashing utilities for deduplication and cache keys."""
import hashlib

class TextHasher:
    """Computes stable SHA-256 fingerprints for documents and chunks."""

    @staticmethod
    def sha256_hex(text: str, length: int = 16) -> str:
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        return digest[:length] if length > 0 else digest

    @classmethod
    def make_chunk_id(cls, source: str, page: int, index: int, text: str) -> str:
        fp = cls.sha256_hex(text, 8)
        return f"{source}_p{page}_c{index}_{fp}"
