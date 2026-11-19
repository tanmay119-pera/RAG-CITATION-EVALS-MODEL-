"""Generates concise 1-sentence summaries for hierarchical indexing."""

import re

class ChunkSummarizer:
    """Produces extractive lead-sentence summaries for chunk metadata indexing."""

    @staticmethod
    def summarize(chunk_text: str) -> str:
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", chunk_text) if s.strip()]
        if not sentences:
            return ""
        # Find first sentence containing core policy definition
        for s in sentences:
            if any(term in s.lower() for term in ["defined as", "shall", "must", "policy", "penalty", "requirement"]):
                return s[:150]
        return sentences[0][:150]
