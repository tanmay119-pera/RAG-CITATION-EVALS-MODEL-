"""End-to-end smoke test verifying clean imports across all modules."""
import unittest

class TestE2ESmoke(unittest.TestCase):
    def test_core_imports(self):
        modules = [
            "rag_evals.config",
            "rag_evals.ingest.loader",
            "rag_evals.ingest.cleaner",
            "rag_evals.ingest.chunker",
            "rag_evals.index.bm25",
            "rag_evals.index.vector_store",
            "rag_evals.retrieval.hybrid",
            "rag_evals.generation.generator",
            "rag_evals.generation.verifier",
            "rag_evals.eval.retrieval_metrics",
            "rag_evals.eval.faithfulness",
            "rag_evals.eval.citation_metrics",
            "rag_evals.eval.chunk_quality",
            "rag_evals.retrieval.synonyms",
        ]
        for m in modules:
            with self.subTest(module=m):
                __import__(m)
