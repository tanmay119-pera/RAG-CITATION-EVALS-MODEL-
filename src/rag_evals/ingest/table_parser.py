"""Preserves Markdown and tabular data structures during ingestion."""

import re
from typing import List, Tuple

class TableParser:
    """Detects tabular blocks and prevents them from being fragmented across chunk boundaries."""

    @staticmethod
    def extract_tables(markdown_text: str) -> List[str]:
        table_pattern = r"(?:^\|.*?\|$\n?)+"
        tables = re.findall(table_pattern, markdown_text, re.MULTILINE)
        return [t.strip() for t in tables if "|" in t]

    @staticmethod
    def is_table_row(line: str) -> bool:
        line = line.strip()
        return line.startswith("|") and line.endswith("|")
