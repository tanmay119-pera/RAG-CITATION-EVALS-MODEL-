"""Tests for AnswerCache."""
import unittest, tempfile
from rag_evals.generation.answer_cache import AnswerCache

class TestAnswerCache(unittest.TestCase):
    def test_cache_io(self):
        with tempfile.TemporaryDirectory() as td:
            ac = AnswerCache(cache_dir=td, ttl_seconds=3600)
            ac.put("Attendance rule", "75% required [c1]", ["c1"])
            cached = ac.get("Attendance rule")
            self.assertIsNotNone(cached)
            self.assertEqual(cached["answer"], "75% required [c1]")
