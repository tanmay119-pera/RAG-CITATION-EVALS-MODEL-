"""Automated failure mode classification and diagnostics."""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional

@dataclass
class FailureRecord:
    case_id: str
    query: str
    failure_type: str
    details: str

class FailureClassifier:
    @staticmethod
    def classify(case: Dict[str, Any], retrieved_chunks: List[str], answer: str, is_refused: bool, is_valid_citation: bool) -> Optional[FailureRecord]:
        cid = case["case_id"]
        q = case["query"]
        expected_clause = case.get("expected_clause", "").lower()

        if not case.get("is_answerable", True):
            if not is_refused:
                return FailureRecord(cid, q, "MISSED_REFUSAL", "Answered unanswerable query.")
            return None

        if is_refused:
            return FailureRecord(cid, q, "FALSE_REFUSAL", "Refused an answerable question.")

        found = any(expected_clause in text.lower() for text in retrieved_chunks)
        if not found:
            return FailureRecord(cid, q, "RETRIEVAL_MISS", f"Expected clause '{expected_clause}' not in top chunks.")

        if not is_valid_citation:
            return FailureRecord(cid, q, "CITATION_ERROR", "Answer contains unverified citation IDs.")
        return None
