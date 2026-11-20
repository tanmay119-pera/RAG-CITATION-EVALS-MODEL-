"""Compare two answers for A/B evaluation."""
from dataclasses import dataclass
from typing import List
from difflib import SequenceMatcher

@dataclass
class ComparisonResult:
    similarity: float
    shared_citations: List[str]
    only_a: List[str]
    only_b: List[str]
    verdict: str

class AnswerComparator:
    """Compare answers from two distinct RAG pipelines or prompt versions."""
    def __init__(self, similarity_threshold: float = 0.85):
        self.threshold = similarity_threshold

    def compare(self, answer_a: str, citations_a: List[str], answer_b: str, citations_b: List[str]) -> ComparisonResult:
        sim = SequenceMatcher(None, answer_a.lower(), answer_b.lower()).ratio()
        set_a, set_b = set(citations_a), set(citations_b)
        shared = sorted(set_a & set_b)
        only_a = sorted(set_a - set_b)
        only_b = sorted(set_b - set_a)

        if sim >= self.threshold:
            verdict = "equivalent"
        elif len(citations_a) > len(citations_b) and sim > 0.5:
            verdict = "a_better"
        elif len(citations_b) > len(citations_a) and sim > 0.5:
            verdict = "b_better"
        else:
            verdict = "different"

        return ComparisonResult(
            similarity=round(sim, 4),
            shared_citations=shared,
            only_a=only_a,
            only_b=only_b,
            verdict=verdict,
        )

    def batch_compare(self, pairs: list) -> List[ComparisonResult]:
        return [self.compare(p["a"], p["cit_a"], p["b"], p["cit_b"]) for p in pairs]
