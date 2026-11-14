"""Heuristic PDF layout feature detector."""
import re

class LayoutHintExtractor:
    """Identifies headings, numbered rules, and table lines during extraction."""

    @staticmethod
    def is_heading(line: str) -> bool:
        s = line.strip()
        if not s or len(s) > 90:
            return False
        return bool(re.match(r"^(?:Section|Chapter|Rule|Article|\d+\.\d*)\b", s, re.I) or s.isupper())

    @staticmethod
    def is_bullet(line: str) -> bool:
        return bool(re.match(r"^\s*(?:[-*•]|\(?\d+\)|[a-z]\))\s+", line))
