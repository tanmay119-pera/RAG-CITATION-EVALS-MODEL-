"""Tests for Stopwatch."""
import unittest, time
from rag_evals.utils.timer import Stopwatch

class TestStopwatch(unittest.TestCase):
    def test_measures_elapsed(self):
        with Stopwatch() as sw:
            time.sleep(0.01)
        self.assertGreater(sw.elapsed_ms, 5.0)
