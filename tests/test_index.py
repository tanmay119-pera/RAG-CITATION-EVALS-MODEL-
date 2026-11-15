"""Unit tests for embedder, cache, BM25, and vector store."""

import unittest
import tempfile
from pathlib import Path
from rag_evals.index.embedder import GeminiEmbedder
from rag_evals.index.cache import EmbeddingCache
from rag_evals.index.bm25 import BM25Index
from rag_evals.index.vector_store import VectorStore
from scripts.build_index import build_all_indexes

class TestIndex(unittest.TestCase):
    def test_mock_embedder(self):
        embedder = GeminiEmbedder()
        vec = embedder.embed_query("academic integrity policy")
        self.assertEqual(len(vec), 128)
        self.assertAlmostEqual(sum(v * v for v in vec), 1.0, places=3)

    def test_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "test.db"
            cache = EmbeddingCache(db_path)
            cache.put("sample text", "model-x", [0.1, 0.2, 0.3])
            val = cache.get("sample text", "model-x")
            self.assertEqual(val, [0.1, 0.2, 0.3])

    def test_bm25(self):
        bm25 = BM25Index()
        bm25.build(["c1", "c2"], ["Academic integrity policy", "Course tuition refund"])
        results = bm25.search("integrity", top_k=1)
        self.assertEqual(results[0][0], "c1")

    def test_vector_store(self):
        vs = VectorStore()
        vs.add("c1", [1.0, 0.0], {"title": "Doc 1"})
        vs.add("c2", [0.0, 1.0], {"title": "Doc 2"})
        res = vs.search([1.0, 0.0], top_k=1)
        self.assertEqual(res[0][0], "c1")

    def test_build_all_indexes(self):
        build_all_indexes()
        self.assertTrue(Path("data/index/bm25.json").exists())
        self.assertTrue(Path("data/index/vector_store.json").exists())

if __name__ == "__main__":
    unittest.main()
