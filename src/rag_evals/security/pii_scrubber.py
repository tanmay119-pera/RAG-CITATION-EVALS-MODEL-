"""Detects and masks Personally Identifiable Information (PII) before ingestion or logging."""

import re

class PIIScrubber:
    """Masks emails, phone numbers, SSNs, and student ID numbers."""

    EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    PHONE_PATTERN = r"\b(?:\+?1[-. ]?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})\b"
    SSN_PATTERN = r"\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b"
    STUDENT_ID_PATTERN = r"\b(?:STU|ID)-[0-9]{6,8}\b"

    @classmethod
    def scrub(cls, text: str) -> str:
        text = re.sub(cls.EMAIL_PATTERN, "[REDACTED_EMAIL]", text)
        text = re.sub(cls.PHONE_PATTERN, "[REDACTED_PHONE]", text)
        text = re.sub(cls.SSN_PATTERN, "[REDACTED_SSN]", text)
        text = re.sub(cls.STUDENT_ID_PATTERN, "[REDACTED_STUDENT_ID]", text)
        return text
