"""Audit golden evaluation datasets for integrity issues."""
from typing import List, Dict, Any

class GoldenSetAuditor:
    """Validates uniqueness, schema fields, and refusal representation in golden sets."""

    @staticmethod
    def audit(cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        seen_queries = set()
        duplicates = []
        missing_sources = []
        unanswerable_count = 0

        for idx, c in enumerate(cases):
            q = c.get("query", "").strip().lower()
            if q in seen_queries:
                duplicates.append(q)
            seen_queries.add(q)

            if c.get("is_unanswerable", False):
                unanswerable_count += 1
            elif not c.get("expected_chunk_ids") and not c.get("golden_chunk_ids"):
                missing_sources.append(c.get("id", f"row_{idx}"))

        return {
            "total": len(cases),
            "duplicates": duplicates,
            "missing_sources": missing_sources,
            "unanswerable_count": unanswerable_count,
            "healthy": len(duplicates) == 0 and len(missing_sources) == 0,
        }
