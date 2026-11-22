"""Tests for ConfigValidator."""
import unittest
from rag_evals.config_validator import ConfigValidator

class TestConfigValidator(unittest.TestCase):
    def test_validation(self):
        cv = ConfigValidator()
        self.assertEqual(len(cv.validate({"chunk_size": 400, "overlap": 50, "top_k": 5})), 0)
        self.assertGreater(len(cv.validate({"chunk_size": 10, "overlap": 20})), 0)
