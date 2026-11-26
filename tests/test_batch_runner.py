"""Tests for BatchPipelineRunner."""
import unittest
from rag_evals.api.batch_runner import BatchPipelineRunner

class TestBatchRunner(unittest.TestCase):
    def test_executes_queries(self):
        runner = BatchPipelineRunner(lambda q: {"answer": f"Mock: {q}", "citations": ["c1"]})
        out = runner.run_all(["Q1", "Q2"])
        self.assertEqual(len(out), 2)
        self.assertEqual(out[1]["query"], "Q2")
