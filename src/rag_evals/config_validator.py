"""Validate RAG execution configurations prior to execution."""
from typing import Dict, List

class ConfigValidator:
    """Checks validity and safety of parameters for chunking and retrieval."""
    def validate(self, cfg: Dict) -> List[str]:
        errors = []
        if cfg.get("chunk_size", 400) <= 20:
            errors.append("chunk_size must be greater than 20 tokens.")
        if cfg.get("overlap", 50) >= cfg.get("chunk_size", 400):
            errors.append("overlap must be strictly less than chunk_size.")
        if cfg.get("top_k", 5) <= 0:
            errors.append("top_k must be at least 1.")
        return errors
