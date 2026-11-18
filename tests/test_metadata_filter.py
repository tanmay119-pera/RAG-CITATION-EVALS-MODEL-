"""Unit tests for metadata filtering engine."""

import unittest
from rag_evals.retrieval.hybrid import RetrievedChunk
from rag_evals.retrieval.metadata_filter import MetadataFilter

class TestMetadataFilter(unittest.TestCase):
    def test_filter_by_section(self):
        c1 = RetrievedChunk("1", "Text 1", 0.9, 1, {"section_title": "SECTION 1: INTEGRITY", "page_number": 1})
        c2 = RetrievedChunk("2", "Text 2", 0.8, 2, {"section_title": "SECTION 6: TUITION", "page_number": 5})
        filtered = MetadataFilter.filter_chunks([c1, c2], section_prefix="INTEGRITY")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].chunk_id, "1")

    def test_filter_by_page_range(self):
        c1 = RetrievedChunk("1", "Text 1", 0.9, 1, {"page_number": 1})
        c2 = RetrievedChunk("2", "Text 2", 0.8, 2, {"page_number": 10})
        filtered = MetadataFilter.filter_chunks([c1, c2], min_page=5, max_page=15)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].chunk_id, "2")

if __name__ == "__main__":
    unittest.main()
