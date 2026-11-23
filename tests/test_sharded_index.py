"""Tests for ShardedIndex."""
import unittest
from rag_evals.index.sharded_index import ShardedIndex

class TestShardedIndex(unittest.TestCase):
    def test_sharded_search(self):
        si = ShardedIndex()
        si.add_documents("rules", ["r1"], ["attendance policy requirements"])
        si.add_documents("syllabus", ["s1"], ["computer science data structures"])
        res_rules = si.search_shard("rules", "attendance")
        self.assertEqual(len(res_rules), 1)
        self.assertEqual(res_rules[0][0], "r1")
        all_res = si.search_all("data")
        self.assertGreater(len(all_res), 0)
