"""REST API router and query handler."""

import time
from typing import Dict, Any
from rag_evals.config import load_config
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker
from rag_evals.generation.generator import GroundedGenerator
from rag_evals.generation.verifier import CitationVerifier
from rag_evals.api.schemas import QueryRequest, QueryResponse, CitationInfo

class RAGApiServer:
    """Lightweight API server logic for handling HTTP queries."""

    def __init__(self):
        self.config = load_config()
        self.retriever = HybridRetriever(self.config)
        self.reranker = CrossEncoderReranker()
        self.generator = GroundedGenerator(self.config)

    def handle_query(self, req: QueryRequest) -> QueryResponse:
        start = time.time()
        raw = self.retriever.retrieve(req.query, top_k=req.top_k, mode=req.retrieval_mode)
        final = self.reranker.rerank(req.query, raw) if req.use_reranker else raw
        answer, is_refused = self.generator.generate(req.query, final)

        v_res = CitationVerifier.verify(answer, {c.chunk_id for c in final})

        citations = []
        for cid in v_res.valid_ids:
            chunk = next((c for c in final if c.chunk_id == cid), None)
            if chunk:
                citations.append(CitationInfo(
                    chunk_id=cid,
                    section_title=chunk.metadata.get("section_title", "General"),
                    file_name=chunk.metadata.get("file_name", "handbook.txt"),
                    page_number=chunk.metadata.get("page_number", 1),
                    text_snippet=chunk.text[:120]
                ))

        latency = round((time.time() - start) * 1000, 2)
        return QueryResponse(
            query=req.query,
            answer=answer,
            is_refusal=is_refused,
            citations=citations,
            latency_ms=latency
        )
