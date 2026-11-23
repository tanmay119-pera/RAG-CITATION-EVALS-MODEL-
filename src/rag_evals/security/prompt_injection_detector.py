"""Heuristic prompt injection and jailbreak detector."""
import re
from typing import Dict, Any

_SUSPICIOUS_PATTERNS = [
    r"ignore previous instructions",
    r"system override",
    r"you are now a helpful uncensored",
    r"jailbreak",
    r"bypass safety",
    r"output full prompt",
]

class PromptInjectionDetector:
    """Scans incoming user queries for prompt injection triggers."""
    def detect(self, query: str) -> Dict[str, Any]:
        q = query.lower()
        matched = []
        for pat in _SUSPICIOUS_PATTERNS:
            if re.search(pat, q):
                matched.append(pat)
        is_suspicious = len(matched) > 0
        return {
            "is_suspicious": is_suspicious,
            "matched_patterns": matched,
            "risk_level": "high" if len(matched) >= 2 else ("medium" if is_suspicious else "low"),
        }
