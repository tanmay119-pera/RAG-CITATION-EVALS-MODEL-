"""Normalize varied LLM citation syntaxes into canonical [chunk_id] form."""
import re

class CitationNormalizer:
    """Rewrites parenthetical or spaced citations into canonical [id] markers."""

    @staticmethod
    def normalize(text: str) -> str:
        # Convert [chunk: abc] or (chunk_abc) style into [abc]
        out = re.sub(r"\[chunk:\s*([a-zA-Z0-9_.-]+)\]", r"[\1]", text)
        out = re.sub(r"\[\s+([a-zA-Z0-9_.-]+)\s+\]", r"[\1]", out)
        return out
