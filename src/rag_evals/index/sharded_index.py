"""Categorical sharded index manager."""
from typing import Dict, List, Any
from rag_evals.index.bm25 import BM25Index

class ShardedIndex:
    """Maintains independent BM25 indices partitionable by document category."""
    def __init__(self):
        self.shards: Dict[str, BM25Index] = {}

    def get_or_create_shard(self, category: str) -> BM25Index:
        if category not in self.shards:
            self.shards[category] = BM25Index()
        return self.shards[category]

    def add_documents(self, category: str, doc_ids: List[str], texts: List[str]):
        shard = self.get_or_create_shard(category)
        shard.build(doc_ids, texts)

    def search_shard(self, category: str, query: str, top_k: int = 5):
        if category not in self.shards:
            return []
        return self.shards[category].search(query, top_k=top_k)

    def search_all(self, query: str, top_k_per_shard: int = 3):
        res = []
        for cat, shard in self.shards.items():
            for doc_id, score in shard.search(query, top_k=top_k_per_shard):
                res.append({"shard": cat, "doc_id": doc_id, "score": score})
        return sorted(res, key=lambda x: x["score"], reverse=True)
