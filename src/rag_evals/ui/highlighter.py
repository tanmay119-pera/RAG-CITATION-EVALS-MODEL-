"""Highlights search keywords and cited clauses in text snippets."""

import re
from typing import List

class TextHighlighter:
    """Applies ANSI terminal or Markdown highlight markup to query terms."""

    @staticmethod
    def highlight_markdown(text: str, keywords: List[str]) -> str:
        for kw in keywords:
            if len(kw.strip()) > 2:
                pattern = re.compile(rf"\b({re.escape(kw)})\b", re.IGNORECASE)
                text = pattern.sub(r"****", text)
        return text

    @staticmethod
    def highlight_ansi(text: str, keywords: List[str]) -> str:
        for kw in keywords:
            if len(kw.strip()) > 2:
                pattern = re.compile(rf"\b({re.escape(kw)})\b", re.IGNORECASE)
                text = pattern.sub(r"\033[1;33m\033[0m", text)
        return text
