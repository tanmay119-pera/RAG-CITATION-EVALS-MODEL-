"""Unit tests for corpus acquisition and audit tools."""

import unittest
import json
from pathlib import Path
from rag_evals.config import load_config
from scripts.audit_corpus import audit_document

class TestCorpus(unittest.TestCase):
    def test_corpus_exists_and_valid(self):
        config = load_config()
        corpus_path = config.raw_data_dir / "university_regulations_handbook.txt"
        self.assertTrue(corpus_path.exists(), "Corpus file must exist in data/raw")
        stats = audit_document(corpus_path)
        self.assertGreater(stats["words"], 500)
        self.assertGreaterEqual(stats["sections_detected"], 6)
        self.assertGreaterEqual(stats["clauses_detected"], 15)

    def test_manifest_integrity(self):
        config = load_config()
        manifest_path = config.raw_data_dir.parent / "corpus_manifest.json"
        self.assertTrue(manifest_path.exists())
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(data["total_documents"], 1)
        self.assertEqual(data["documents"][0]["filename"], "university_regulations_handbook.txt")

if __name__ == "__main__":
    unittest.main()
