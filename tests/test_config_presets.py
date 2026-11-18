"""Unit tests for configuration presets."""

import unittest
from rag_evals.config import AppConfig

class TestConfigPresets(unittest.TestCase):
    def test_fast_preset(self):
        cfg = AppConfig.get_preset("fast")
        self.assertEqual(cfg.chunk_size_tokens, 300)
        self.assertFalse(cfg.use_reranker)

    def test_deep_preset(self):
        cfg = AppConfig.get_preset("deep")
        self.assertEqual(cfg.chunk_size_tokens, 600)
        self.assertEqual(cfg.top_k_retrieve, 15)

if __name__ == "__main__":
    unittest.main()
