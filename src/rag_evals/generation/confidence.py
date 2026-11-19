"""Calculates grounded confidence scores based on retrieval affinity and citation validity."""

from typing import List
from rag_evals.retrieval.hybrid import RetrievedChunk
from rag_evals.generation.verifier import VerificationResult

class ConfidenceScorer:
    """Computes a calibrated 0.0-1.0 confidence score for generated RAG answers."""

    @staticmethod
    def calculate(
        retrieved_chunks: List[RetrievedChunk],
        verification_result: VerificationResult,
        is_refusal: bool
    ) -> float:
        if is_refusal:
            return 1.0  # High confidence refusal

        if not verification_result.is_valid:
            return 0.2

        if not retrieved_chunks:
            return 0.0

        top_score = max(c.score for c in retrieved_chunks)
        citation_factor = min(1.0, len(verification_result.valid_ids) * 0.5)

        confidence = (top_score * 0.6) + (citation_factor * 0.4)
        return round(min(1.0, max(0.0, confidence)), 3)
