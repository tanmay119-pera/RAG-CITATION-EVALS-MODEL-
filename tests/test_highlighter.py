"""Unit tests for keyword highlighter."""

import unittest
from rag_evals.ui.highlighter import TextHighlighter

class TestHighlighter(unittest.TestCase):
    def test_highlight_markdown(self):
        text = "Penalties for plagiarism are strictly enforced."
        res = TextHighlighter.highlight_markdown(text, ["plagiarism"])
        self.assertIn("**plagiarism**", res)

    def test_highlight_ansi(self):
        text = "Attendance is compulsory."
        res = TextHighlighter.highlight_ansi(text, ["attendance"])
        self.assertIn("\033[1;33mAttendance\033[0m", res)

if __name__ == "__main__":
    unittest.main()
