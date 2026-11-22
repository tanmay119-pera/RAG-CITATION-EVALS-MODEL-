"""Detect dominant script and language for incoming documents."""
import re
from typing import Dict, Any

_PATTERNS = {
    "latin": re.compile(r"[a-zA-Z]"),
    "devanagari": re.compile(r"[\u0900-\u097F]"),
    "digits": re.compile(r"[0-9]"),
}

class LanguageDetector:
    """Heuristic detector for document character scripts."""
    def detect(self, text: str) -> Dict[str, Any]:
        counts = {k: len(p.findall(text)) for k, p in _PATTERNS.items()}
        total = sum(counts.values())
        if total == 0:
            return {"script": "unknown", "language": "unknown", "confidence": 0.0}
        dominant = max(counts, key=counts.get)
        lang = "en" if dominant == "latin" else ("hi" if dominant == "devanagari" else "unknown")
        return {"script": dominant, "language": lang, "confidence": round(counts[dominant] / total, 2)}
