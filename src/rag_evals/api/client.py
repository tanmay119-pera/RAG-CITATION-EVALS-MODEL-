"""Python client SDK for calling the RAG API."""

from typing import Dict, Any, Optional
from rag_evals.api.schemas import QueryRequest, QueryResponse
from rag_evals.api.server import RAGApiServer

class RAGClient:
    """High-level client SDK for integrating RAG citations into applications."""

    def __init__(self):
        self._server = RAGApiServer()

    def query(self, question: str, mode: str = "hybrid", top_k: int = 5) -> QueryResponse:
        req = QueryRequest(query=question, retrieval_mode=mode, top_k=top_k)
        return self._server.handle_query(req)
