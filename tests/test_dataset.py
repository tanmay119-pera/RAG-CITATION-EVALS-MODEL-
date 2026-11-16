"""Unit tests for evaluation dataset integrity."""

import unittest
from pathlib import Path
from rag_evals.config import load_config
from scripts.validate_dataset import validate_dataset

class TestDataset(unittest.TestCase):
    def test_golden_dataset_validation(self):
        config = load_config()
        path = config.eval_dir / "golden_set.jsonl"
        stats = validate_dataset(path)
        self.assertGreaterEqual(stats["total_cases"], 50)
        self.assertGreaterEqual(stats["unanswerable"], 10)
        self.assertGreaterEqual(stats["answerable"], 35)

if __name__ == "__main__":
    unittest.main()
