"""Maximal Marginal Relevance (MMR) reranker for candidate diversity."""

from typing import List
from rag_evals.retrieval.hybrid import RetrievedChunk

class MMRReranker:
    """Penalizes redundant near-duplicate chunks to maximize information diversity in top-K."""

    def __init__(self, lambda_mult: float = 0.7):
        self.lambda_mult = lambda_mult

    @staticmethod
    def _text_overlap(t1: str, t2: str) -> float:
        w1 = set(t1.lower().split())
        w2 = set(t2.lower().split())
        if not w1 or not w2:
            return 0.0
        return len(w1.intersection(w2)) / len(w1.union(w2))

    def rerank(self, chunks: List[RetrievedChunk], top_n: int = 5) -> List[RetrievedChunk]:
        if not chunks:
            return []

        selected = [chunks[0]]
        candidates = chunks[1:]

        while len(selected) < top_n and candidates:
            best_score = -float("inf")
            best_candidate = None

            for cand in candidates:
                relevance = cand.score
                max_redundancy = max(self._text_overlap(cand.text, sel.text) for sel in selected)
                mmr_score = self.lambda_mult * relevance - (1.0 - self.lambda_mult) * max_redundancy

                if mmr_score > best_score:
                    best_score = mmr_score
                    best_candidate = cand

            if best_candidate:
                selected.append(best_candidate)
                candidates.remove(best_candidate)
            else:
                break

        for rank, c in enumerate(selected, start=1):
            c.rank = rank

        return selected
