"""Hybrid retriever combining dense vector search and sparse BM25 with Reciprocal Rank Fusion (RRF)."""

from dataclasses import dataclass, field
from typing import List, Dict, Any
from rag_evals.config import AppConfig, load_config
from rag_evals.index.bm25 import BM25Index
from rag_evals.index.vector_store import VectorStore
from rag_evals.index.embedder import GeminiEmbedder

@dataclass
class RetrievedChunk:
    chunk_id: str
    text: str
    score: float
    rank: int
    metadata: Dict[str, Any] = field(default_factory=dict)

class HybridRetriever:
    def __init__(self, config: AppConfig | None = None):
        self.config = config or load_config()
        self.bm25 = BM25Index()
        self.vstore = VectorStore()
        self.embedder = GeminiEmbedder(self.config)
        self._load_indexes()

    def _load_indexes(self):
        bm25_path = self.config.index_dir / "bm25.json"
        vstore_path = self.config.index_dir / "vector_store.json"
        if bm25_path.is_file():
            self.bm25.load(bm25_path)
        if vstore_path.is_file():
            self.vstore.load(vstore_path)

    def retrieve(self, query: str, top_k: int = 10, mode: str = "hybrid") -> List[RetrievedChunk]:
        if mode == "bm25":
            return self._retrieve_bm25(query, top_k)
        elif mode == "dense":
            return self._retrieve_dense(query, top_k)
        else:
            return self._retrieve_hybrid(query, top_k)

    def _retrieve_bm25(self, query: str, top_k: int) -> List[RetrievedChunk]:
        bm25_hits = self.bm25.search(query, top_k=top_k)
        chunks = []
        for rank, (cid, score) in enumerate(bm25_hits, start=1):
            meta = self.vstore.metadata_store.get(cid, {})
            chunks.append(RetrievedChunk(chunk_id=cid, text=meta.get("text", ""), score=score, rank=rank, metadata=meta))
        return chunks

    def _retrieve_dense(self, query: str, top_k: int) -> List[RetrievedChunk]:
        q_vec = self.embedder.embed_query(query)
        v_hits = self.vstore.search(q_vec, top_k=top_k)
        chunks = []
        for rank, (cid, score, meta) in enumerate(v_hits, start=1):
            chunks.append(RetrievedChunk(chunk_id=cid, text=meta.get("text", ""), score=score, rank=rank, metadata=meta))
        return chunks

    def _retrieve_hybrid(self, query: str, top_k: int, rrf_k: int = 60) -> List[RetrievedChunk]:
        bm25_hits = self.bm25.search(query, top_k=top_k * 2)
        q_vec = self.embedder.embed_query(query)
        v_hits = self.vstore.search(q_vec, top_k=top_k * 2)

        rrf_scores: Dict[str, float] = {}
        for rank, (cid, _) in enumerate(bm25_hits, start=1):
            rrf_scores[cid] = rrf_scores.get(cid, 0.0) + (1.0 / (rrf_k + rank))

        for rank, (cid, _, _) in enumerate(v_hits, start=1):
            rrf_scores[cid] = rrf_scores.get(cid, 0.0) + (1.0 / (rrf_k + rank))

        ranked = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
        result = []
        for rank, (cid, score) in enumerate(ranked, start=1):
            meta = self.vstore.metadata_store.get(cid, {})
            result.append(RetrievedChunk(chunk_id=cid, text=meta.get("text", ""), score=score, rank=rank, metadata=meta))
        return result
