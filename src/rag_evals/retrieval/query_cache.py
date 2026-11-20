"""LRU cache for repeated query results."""
import hashlib, time
from collections import OrderedDict
from typing import Any, Optional

class QueryCache:
    """Thread-safe LRU cache with TTL expiration for retrieval queries."""
    def __init__(self, max_size: int = 256, ttl_seconds: float = 300):
        self.max_size = max_size
        self.ttl = ttl_seconds
        self._cache: OrderedDict = OrderedDict()

    def _key(self, query: str) -> str:
        return hashlib.sha256(query.strip().lower().encode("utf-8")).hexdigest()[:16]

    def get(self, query: str) -> Optional[Any]:
        k = self._key(query)
        if k in self._cache:
            entry = self._cache[k]
            if time.time() - entry["ts"] < self.ttl:
                self._cache.move_to_end(k)
                return entry["value"]
            del self._cache[k]
        return None

    def put(self, query: str, value: Any):
        k = self._key(query)
        self._cache[k] = {"value": value, "ts": time.time()}
        self._cache.move_to_end(k)
        while len(self._cache) > self.max_size:
            self._cache.popitem(last=False)

    def clear(self):
        self._cache.clear()

    @property
    def size(self) -> int:
        return len(self._cache)
