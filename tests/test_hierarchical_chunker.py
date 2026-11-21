"""Tests for HierarchicalChunker."""
import unittest
from rag_evals.ingest.hierarchical_chunker import HierarchicalChunker

class TestHierarchicalChunker(unittest.TestCase):
    def test_chunking(self):
        hc = HierarchicalChunker(parent_size=10, child_size=5, overlap=1)
        doc = {"text": "one two three four five six seven eight nine ten eleven twelve", "source": "s1"}
        chunks = hc.chunk(doc)
        parents = [c for c in chunks if c["level"] == "parent"]
        children = [c for c in chunks if c["level"] == "child"]
        self.assertGreater(len(parents), 0)
        self.assertGreater(len(children), 0)
        self.assertIn("parent_id", children[0])
