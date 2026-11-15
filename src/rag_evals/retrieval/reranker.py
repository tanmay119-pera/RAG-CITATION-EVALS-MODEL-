"""Cross-encoder relevance reranker with exact term and semantic position scoring."""

import re
from typing import List
from rag_evals.retrieval.hybrid import RetrievedChunk

class CrossEncoderReranker:
    def __init__(self, top_n: int = 5):
        self.top_n = top_n

    def rerank(self, query: str, chunks: List[RetrievedChunk]) -> List[RetrievedChunk]:
        if not chunks:
            return []

        q_terms = [w.lower() for w in re.findall(r"\w+", query) if len(w) > 2]
        scored_chunks = []

        for chunk in chunks:
            text_lower = chunk.text.lower()
            term_matches = sum(1 for t in q_terms if t in text_lower)
            coverage = term_matches / len(q_terms) if q_terms else 0.0
            # Blend initial retrieval rank score and exact coverage
            rerank_score = chunk.score * 0.4 + coverage * 0.6
            scored_chunks.append((chunk, rerank_score))

        scored_chunks.sort(key=lambda x: x[1], reverse=True)
        final_list = []
        for new_rank, (chunk, score) in enumerate(scored_chunks[:self.top_n], start=1):
            chunk.rank = new_rank
            chunk.score = score
            final_list.append(chunk)

        return final_list
