"""Input query sanitization and prompt injection defense."""

import re
from dataclasses import dataclass
from typing import List

@dataclass
class GuardrailResult:
    is_safe: bool
    sanitized_query: str
    detected_patterns: List[str]

class SecurityGuardrail:
    """Detects and neutralizes prompt injections, system override attempts, and malicious directives."""

    INJECTION_PATTERNS = [
        r"(?i)ignore\s+all\s+(previous|above)\s+instructions",
        r"(?i)disregard\s+(all\s+)?guidelines",
        r"(?i)you\s+are\s+now\s+in\s+developer\s+mode",
        r"(?i)dan\s+mode",
        r"(?i)reveal\s+your\s+system\s+prompt",
        r"(?i)bypass\s+all\s+rules",
        r"(?i)do\s+not\s+cite",
        r"(?i)output\s+raw\s+passwords"
    ]

    @classmethod
    def inspect(cls, query: str) -> GuardrailResult:
        detected = []
        for pattern in cls.INJECTION_PATTERNS:
            if re.search(pattern, query):
                detected.append(pattern)

        # Sanitize HTML / control characters
        sanitized = re.sub(r"[<>]", "", query).strip()

        is_safe = len(detected) == 0
        return GuardrailResult(
            is_safe=is_safe,
            sanitized_query=sanitized,
            detected_patterns=detected
        )
