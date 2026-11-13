"""Tests for AppConfig and load_config."""

import tempfile
import unittest
from pathlib import Path

from rag_evals.config import AppConfig, _parse_bool, _read_env_file, load_config


class TestConfig(unittest.TestCase):
    def test_default_config(self):
        config = load_config(env_path=Path("/nonexistent/file.env"), overrides={})
        self.assertEqual(config.embedding_model, "gemini-embedding-001")
        self.assertEqual(config.generation_model, "gemini-3.8-flash")
        self.assertEqual(config.chunk_size_tokens, 450)
        self.assertEqual(config.chunk_overlap_tokens, 50)
        self.assertTrue(config.use_hybrid)
        self.assertTrue(config.use_reranker)
        self.assertFalse(config.has_api_key)

    def test_parse_bool(self):
        self.assertTrue(_parse_bool("true"))
        self.assertTrue(_parse_bool("1"))
        self.assertTrue(_parse_bool("YES"))
        self.assertFalse(_parse_bool("0"))
        self.assertFalse(_parse_bool("false"))
        self.assertFalse(_parse_bool(None, default=False))

    def test_load_from_env_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            env_file = Path(tmp_dir) / ".env.test"
            env_file.write_text(
                "GEMINI_API_KEY=test-secret-key\n"
                "CHUNK_SIZE_TOKENS=512\n"
                "USE_RERANKER=false\n"
                "# A comment line\n",
                encoding="utf-8",
            )
            config = load_config(env_path=env_file)
            self.assertEqual(config.gemini_api_key, "test-secret-key")
            self.assertTrue(config.has_api_key)
            self.assertEqual(config.chunk_size_tokens, 512)
            self.assertFalse(config.use_reranker)

    def test_ensure_directories(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            base = Path(tmp_dir)
            config = AppConfig(
                raw_data_dir=base / "raw",
                processed_data_dir=base / "processed",
                index_dir=base / "index",
                eval_dir=base / "eval",
            )
            config.ensure_directories()
            self.assertTrue((base / "raw").is_dir())
            self.assertTrue((base / "processed").is_dir())
            self.assertTrue((base / "index").is_dir())
            self.assertTrue((base / "eval").is_dir())


if __name__ == "__main__":
    unittest.main()
