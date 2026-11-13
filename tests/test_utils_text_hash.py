"""Tests for TextHasher."""
import unittest
from rag_evals.utils.text_hash import TextHasher

class TestTextHasher(unittest.TestCase):
    def test_deterministic_hash(self):
        h1 = TextHasher.sha256_hex("hello", 12)
        h2 = TextHasher.sha256_hex("hello", 12)
        self.assertEqual(h1, h2)
        self.assertEqual(len(h1), 12)

    def test_make_chunk_id(self):
        cid = TextHasher.make_chunk_id("syllabus", 3, 1, "course policy")
        self.assertTrue(cid.startswith("syllabus_p3_c1_"))
