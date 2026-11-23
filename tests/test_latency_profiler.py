"""Tests for LatencyProfiler."""
import unittest, time
from rag_evals.eval.latency_profiler import LatencyProfiler

class TestLatencyProfiler(unittest.TestCase):
    def test_profiling(self):
        prof = LatencyProfiler()
        with prof.measure("retrieval"):
            time.sleep(0.01)
        with prof.measure("generation"):
            time.sleep(0.01)
        summary = prof.summary()
        self.assertIn("retrieval", summary["stages_ms"])
        self.assertGreater(summary["total_ms"], 10.0)
