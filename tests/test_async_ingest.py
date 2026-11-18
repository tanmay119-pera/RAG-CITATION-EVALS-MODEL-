"""Unit tests for concurrent loader and dynamic window adjuster."""

import unittest
from pathlib import Path
from rag_evals.config import load_config
from rag_evals.ingest.async_ingest import ConcurrentLoader
from rag_evals.ingest.dynamic_window import DynamicWindowAdjuster

class TestAsyncIngest(unittest.TestCase):
    def test_concurrent_loader(self):
        config = load_config()
        files = list(config.raw_data_dir.glob("*.txt"))
        loader = ConcurrentLoader(max_workers=2)
        docs = loader.load_files(files)
        self.assertGreaterEqual(len(docs), 1)

    def test_dynamic_window(self):
        dense_text = "\n".join([f"- Item {i}" for i in range(15)])
        target = DynamicWindowAdjuster.get_optimal_window(dense_text, base_tokens=400)
        self.assertEqual(target, 300)

if __name__ == "__main__":
    unittest.main()
