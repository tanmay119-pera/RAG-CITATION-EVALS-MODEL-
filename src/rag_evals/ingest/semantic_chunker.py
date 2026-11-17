"""Semantic sentence boundary splitter for high-coherence chunking."""

import re
from typing import List

class SemanticSplitter:
    """Splits raw text along natural clause and sentence boundaries rather than hard character cuts."""

    SENTENCE_REGEX = r"(?<=[.!?])\s+(?=[A-Z0-9])"

    @classmethod
    def split_sentences(cls, text: str) -> List[str]:
        sentences = [s.strip() for s in re.split(cls.SENTENCE_REGEX, text) if s.strip()]
        return sentences

    @classmethod
    def group_sentences(cls, sentences: List[str], max_words: int = 150) -> List[str]:
        groups = []
        current_group = []
        current_count = 0

        for s in sentences:
            w_count = len(s.split())
            if current_count + w_count > max_words and current_group:
                groups.append(" ".join(current_group))
                current_group = [s]
                current_count = w_count
            else:
                current_group.append(s)
                current_count += w_count

        if current_group:
            groups.append(" ".join(current_group))
        return groups
