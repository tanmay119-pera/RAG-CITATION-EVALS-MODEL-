"""Query normalization and academic acronym expander."""
import re

_ACRONYMS = {
    "cgpa": "cumulative grade point average",
    "sgpa": "semester grade point average",
    "hod": "head of department",
    "ug": "undergraduate",
    "pg": "postgraduate",
}

class QueryRewriter:
    """Rewrites concise student queries for higher BM25 and dense recall."""

    @staticmethod
    def rewrite(query: str) -> str:
        tokens = re.sub(r"\s+", " ", query.strip()).split(" ")
        expanded = []
        for t in tokens:
            clean = re.sub(r"[^a-zA-Z0-9]", "", t).lower()
            expanded.append(t)
            if clean in _ACRONYMS:
                expanded.append(f"({_ACRONYMS[clean]})")
        return " ".join(expanded)
