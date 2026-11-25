"""Tests for CorpusSafetyScanner."""
import unittest
from rag_evals.security.corpus_scanner import CorpusSafetyScanner

class TestCorpusScanner(unittest.TestCase):
    def test_flags_unsafe_script_and_email(self):
        res = CorpusSafetyScanner.scan("Contact admin@uni.edu <script>bad()</script>")
        self.assertFalse(res["clean"])
        self.assertTrue(res["has_script_tag"])
        self.assertEqual(res["email_count"], 1)
