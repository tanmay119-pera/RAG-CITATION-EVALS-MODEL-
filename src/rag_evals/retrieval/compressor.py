"""Context compressor that extracts key sentences from retrieved chunks."""

import re
from typing import List
from rag_evals.retrieval.hybrid import RetrievedChunk

class ContextCompressor:
    """Extracts only query-relevant sentences to minimize prompt token count and maximize density."""

    @staticmethod
    def compress_chunk(query: str, chunk: RetrievedChunk) -> RetrievedChunk:
        q_words = set(w.lower() for w in re.findall(r"\w+", query) if len(w) > 3)
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", chunk.text) if s.strip()]

        if not q_words or len(sentences) <= 2:
            return chunk

        relevant_sents = []
        for s in sentences:
            s_words = set(w.lower() for w in re.findall(r"\w+", s))
            if q_words.intersection(s_words):
                relevant_sents.append(s)

        if not relevant_sents:
            return chunk

        compressed_text = " ".join(relevant_sents)
        return RetrievedChunk(
            chunk_id=chunk.chunk_id,
            text=compressed_text,
            score=chunk.score,
            rank=chunk.rank,
            metadata=chunk.metadata
        )
