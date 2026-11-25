"""Scan raw corpus passages for embedded PII or markup scripts prior to indexing."""
import re
from typing import Dict, Any

class CorpusSafetyScanner:
    """Identifies potentially unsafe patterns or sensitive PII inside corpus chunks."""

    @staticmethod
    def scan(text: str) -> Dict[str, Any]:
        has_script = bool(re.search(r"<script\b", text, re.I))
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
        return {
            "clean": (not has_script) and len(emails) == 0,
            "has_script_tag": has_script,
            "email_count": len(emails),
        }
