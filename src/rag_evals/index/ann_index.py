"""Approximate Nearest Neighbor (ANN) index wrapper for sub-millisecond retrieval."""

import math
from typing import List, Tuple, Dict, Any

class PartitionedANNIndex:
    """Partitions dense vectors into inverted buckets for accelerated approximate search."""

    def __init__(self, n_buckets: int = 4):
        self.n_buckets = n_buckets
        self.buckets: Dict[int, List[Tuple[str, List[float], Dict[str, Any]]]] = {i: [] for i in range(n_buckets)}

    def _hash_vector(self, vec: List[float]) -> int:
        first_components = sum(vec[:4]) if len(vec) >= 4 else vec[0]
        return int(abs(first_components * 100)) % self.n_buckets

    def add(self, chunk_id: str, vector: List[float], metadata: Dict[str, Any]):
        b_idx = self._hash_vector(vector)
        self.buckets[b_idx].append((chunk_id, vector, metadata))

    def search(self, query_vector: List[float], top_k: int = 5) -> List[Tuple[str, float]]:
        b_idx = self._hash_vector(query_vector)
        candidates = self.buckets.get(b_idx, [])
        # If bucket is sparse, search all
        if len(candidates) < top_k:
            candidates = [item for b in self.buckets.values() for item in b]

        scored = []
        for cid, vec, _ in candidates:
            dot = sum(x * y for x, y in zip(query_vector, vec))
            scored.append((cid, dot))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]
