"""Tests for GoldenSetAuditor."""
import unittest
from rag_evals.eval.golden_audit import GoldenSetAuditor

class TestGoldenAudit(unittest.TestCase):
    def test_audit_detects_duplicates(self):
        rep = GoldenSetAuditor.audit([
            {"id": "1", "query": "What is GPA?", "expected_chunk_ids": ["c1"]},
            {"id": "2", "query": "what is gpa?", "is_unanswerable": True},
        ])
        self.assertFalse(rep["healthy"])
        self.assertEqual(rep["unanswerable_count"], 1)
