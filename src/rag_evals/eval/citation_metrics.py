"""Computes citation precision and citation recall against source chunks."""

from typing import List, Dict, Any

class CitationMetrics:
    @staticmethod
    def compute(answer: str, cited_ids: List[str], gold_clause: str, chunk_metadata: Dict[str, Dict[str, Any]]) -> Dict[str, float]:
        if not cited_ids:
            return {"citation_precision": 0.0, "citation_recall": 0.0}

        gold_lower = gold_clause.lower()
        supporting = 0
        for cid in cited_ids:
            meta = chunk_metadata.get(cid, {})
            text = meta.get("text", "").lower()
            sec = meta.get("section_title", "").lower()
            if gold_lower in text or gold_lower in sec:
                supporting += 1

        prec = supporting / len(cited_ids)
        rec = 1.0 if supporting > 0 else 0.0
        return {"citation_precision": prec, "citation_recall": rec}
