"""Enriches chunks with hierarchical tags, keywords, and clause references."""

import re
from typing import Dict, Any, List

class MetadataEnricher:
    """Enriches chunk metadata with structural headers, clauses, and key academic concepts."""

    @staticmethod
    def enrich(chunk_text: str, existing_meta: Dict[str, Any]) -> Dict[str, Any]:
        meta = dict(existing_meta)

        # Detect clauses like Clause 3.2
        clauses = re.findall(r"Clause\s+(\d+\.\d+)", chunk_text)
        meta["detected_clauses"] = list(set(clauses))

        # Detect academic concepts
        keywords = []
        for kw in ["plagiarism", "withdrawal", "gpa", "attendance", "probation", "refund", "incomplete", "expulsion", "credits"]:
            if kw in chunk_text.lower():
                keywords.append(kw)
        meta["keywords"] = keywords

        return meta
