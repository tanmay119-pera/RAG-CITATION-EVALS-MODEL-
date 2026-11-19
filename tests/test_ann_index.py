"""Unit tests for partitioned ANN vector index."""

import unittest
from rag_evals.index.ann_index import PartitionedANNIndex

class TestANNIndex(unittest.TestCase):
    def test_ann_partitioning(self):
        ann = PartitionedANNIndex(n_buckets=2)
        ann.add("c1", [1.0, 0.0, 0.0, 0.0], {"title": "Doc 1"})
        ann.add("c2", [0.0, 1.0, 0.0, 0.0], {"title": "Doc 2"})
        hits = ann.search([1.0, 0.0, 0.0, 0.0], top_k=1)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][0], "c1")

if __name__ == "__main__":
    unittest.main()
