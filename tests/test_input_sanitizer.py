"""Tests for InputSanitizer."""
import unittest
from rag_evals.security.input_sanitizer import InputSanitizer

class TestInputSanitizer(unittest.TestCase):
    def test_sanitization(self):
        s = InputSanitizer()
        raw = "Hello\u200B <b>World</b>!   How are   you?"
        clean = s.sanitize(raw)
        self.assertEqual(clean, "Hello World! How are you?")
