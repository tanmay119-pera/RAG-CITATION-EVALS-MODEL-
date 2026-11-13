"""Tests for EnvironmentInspector."""
import unittest
from rag_evals.utils.env_check import EnvironmentInspector

class TestEnvCheck(unittest.TestCase):
    def test_report_shape(self):
        rep = EnvironmentInspector.report()
        self.assertIn("python_version", rep)
        self.assertTrue(rep["offline_mock_ready"])
