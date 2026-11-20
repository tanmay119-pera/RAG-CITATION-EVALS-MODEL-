"""Tests for HealthChecker."""
import unittest, tempfile
from pathlib import Path
from rag_evals.api.health import HealthChecker

class TestHealthChecker(unittest.TestCase):
    def test_missing_data(self):
        hc = HealthChecker(data_dir="/tmp/nonexistent_test_dir")
        self.assertEqual(hc.check_corpus()["status"], "missing")

    def test_valid_data(self):
        with tempfile.TemporaryDirectory() as td:
            corpus = Path(td) / "corpus"
            corpus.mkdir()
            (corpus / "sample.txt").write_text("sample")
            hc = HealthChecker(data_dir=td)
            self.assertEqual(hc.check_corpus()["status"], "ok")
