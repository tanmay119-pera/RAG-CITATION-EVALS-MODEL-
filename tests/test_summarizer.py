"""Unit tests for chunk summarizer."""

import unittest
from rag_evals.ingest.summarizer import ChunkSummarizer

class TestSummarizer(unittest.TestCase):
    def test_extractive_summary(self):
        text = "Welcome to campus. Academic integrity is foundational. Plagiarism is defined as stealing ideas."
        summary = ChunkSummarizer.summarize(text)
        self.assertIn("Plagiarism is defined as", summary)

if __name__ == "__main__":
    unittest.main()
