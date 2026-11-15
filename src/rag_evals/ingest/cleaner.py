"""Text cleaning, whitespace normalization, and section header extraction."""

import re
from typing import Tuple, List

class TextCleaner:
    @staticmethod
    def clean(text: str) -> str:
        # Strip trailing/leading space, unify line breaks
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        # Replace multiple spaces with single space
        text = re.sub(r"[ \t]+", " ", text)
        # Collapse 3+ newlines to 2 newlines
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    @staticmethod
    def extract_section_title(text: str) -> str:
        """Extract the most prominent section header from passage text."""
        # Check for SECTION X: TITLE
        match = re.search(r"SECTION \d+:[^\n]+", text)
        if match:
            return match.group(0).strip(" =#")
        # Check for Clause X.Y - TITLE
        match_clause = re.search(r"Clause \d+\.\d+ - [^:\n]+", text)
        if match_clause:
            return match_clause.group(0).strip(" =#")
        # Fallback to markdown header
        match_md = re.search(r"^#{1,3}\s+([^\n]+)", text, re.MULTILINE)
        if match_md:
            return match_md.group(1).strip()
        return "General Regulations"
