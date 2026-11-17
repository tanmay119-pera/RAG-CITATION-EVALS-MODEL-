"""Request and response schemas for RAG HTTP API."""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class QueryRequest:
    query: str
    top_k: int = 5
    retrieval_mode: str = "hybrid"
    use_reranker: bool = True

@dataclass
class CitationInfo:
    chunk_id: str
    section_title: str
    file_name: str
    page_number: int
    text_snippet: str

@dataclass
class QueryResponse:
    query: str
    answer: str
    is_refusal: bool
    citations: List[CitationInfo] = field(default_factory=list)
    latency_ms: float = 0.0
