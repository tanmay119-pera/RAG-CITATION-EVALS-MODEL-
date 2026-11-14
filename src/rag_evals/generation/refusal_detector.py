"""Detect whether a model answer explicitly refuses unanswerable queries."""
import re

_REFUSAL_CUES = [
    r"i don't know",
    r"not enough information",
    r"cannot determine from the provided",
    r"no information in the retrieved",
    r"unable to find an answer",
]

class RefusalDetector:
    """Identifies grounded abstentions cleanly."""

    @staticmethod
    def is_refusal(answer: str) -> bool:
        low = answer.lower()
        return any(re.search(pat, low) for pat in _REFUSAL_CUES)
