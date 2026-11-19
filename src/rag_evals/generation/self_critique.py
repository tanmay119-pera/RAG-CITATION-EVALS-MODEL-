"""Self-critique and verification loop for generated citations."""

from typing import List, Tuple
from rag_evals.generation.verifier import CitationVerifier
from rag_evals.retrieval.hybrid import RetrievedChunk

class SelfCritiqueAgent:
    """Critiques answer candidates, flags hallucinated IDs, and strips ungrounded claims."""

    @staticmethod
    def critique_and_repair(answer: str, retrieved_chunks: List[RetrievedChunk]) -> Tuple[str, bool]:
        valid_ids = {c.chunk_id for c in retrieved_chunks}
        v_res = CitationVerifier.verify(answer, valid_ids)

        if not v_res.is_valid and v_res.invalid_ids:
            repaired = answer
            for bad_id in v_res.invalid_ids:
                repaired = repaired.replace(f"[{bad_id}]", "")
            return repaired.strip(), False

        return answer, True
