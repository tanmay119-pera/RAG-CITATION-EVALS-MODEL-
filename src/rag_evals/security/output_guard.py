"""Sanitizes generated answer text to remove accidental prompt leakage."""

import re

class OutputGuard:
    @staticmethod
    def sanitize(answer: str) -> str:
        cleaned = re.sub(r"(?i)you are an academic assistant.*", "", answer)
        cleaned = re.sub(r"(?i)CRITICAL CITATION RULES:.*", "", cleaned)
        return cleaned.strip()
