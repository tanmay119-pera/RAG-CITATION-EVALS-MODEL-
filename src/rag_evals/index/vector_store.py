"""Dense vector store supporting cosine similarity nearest neighbor search."""

import json
from pathlib import Path
from typing import List, Dict, Any, Tuple

class VectorStore:
    def __init__(self):
        self.chunk_ids: List[str] = []
        self.vectors: List[List[float]] = []
        self.metadata_store: Dict[str, Dict[str, Any]] = {}

    def add(self, chunk_id: str, vector: List[float], metadata: Dict[str, Any]):
        self.chunk_ids.append(chunk_id)
        self.vectors.append(vector)
        self.metadata_store[chunk_id] = metadata

    @staticmethod
    def _cosine_similarity(a: List[float], b: List[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = sum(x * x for x in a) ** 0.5
        norm_b = sum(y * y for y in b) ** 0.5
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    def search(self, query_vector: List[float], top_k: int = 10) -> List[Tuple[str, float, Dict[str, Any]]]:
        if not self.vectors:
            return []

        results = []
        for cid, vec in zip(self.chunk_ids, self.vectors):
            score = self._cosine_similarity(query_vector, vec)
            results.append((cid, score, self.metadata_store.get(cid, {})))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]

    def save(self, path: Path):
        data = {
            "chunk_ids": self.chunk_ids,
            "vectors": self.vectors,
            "metadata_store": self.metadata_store
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load(self, path: Path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.chunk_ids = data["chunk_ids"]
        self.vectors = data["vectors"]
        self.metadata_store = data["metadata_store"]
