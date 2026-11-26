"""Extract inline sentence claims paired with their bracketed citation IDs."""
import re
from typing import List, Dict

class CitationSpanExtractor:
    """Parses grounded answers into sentence + citation ID mappings."""

    @staticmethod
    def extract(answer: str) -> List[Dict]:
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", answer.strip()) if s.strip()]
        out: List[Dict] = []
        for s in sentences:
            cids = re.findall(r"\[([a-zA-Z0-9_.-]+)\]", s)
            out.append({"sentence": s, "citations": cids, "grounded": len(cids) > 0})
        return out
