"""Tests for QueryCache."""
import unittest, time
from rag_evals.retrieval.query_cache import QueryCache

class TestQueryCache(unittest.TestCase):
    def test_cache_hit_and_miss(self):
        qc = QueryCache()
        qc.put("hello", 123)
        self.assertEqual(qc.get("hello"), 123)
        self.assertIsNone(qc.get("world"))

    def test_lru_eviction(self):
        qc = QueryCache(max_size=2)
        qc.put("a", 1)
        qc.put("b", 2)
        qc.put("c", 3)
        self.assertIsNone(qc.get("a"))
        self.assertEqual(qc.get("b"), 2)
