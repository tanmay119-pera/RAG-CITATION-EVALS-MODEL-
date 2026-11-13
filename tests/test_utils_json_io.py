"""Tests for json_io."""
import unittest, tempfile
from pathlib import Path
from rag_evals.utils.json_io import write_jsonl, read_jsonl

class TestJsonIO(unittest.TestCase):
    def test_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "chunks.jsonl"
            n = write_jsonl(p, [{"id": 1}, {"id": 2}])
            self.assertEqual(n, 2)
            rows = read_jsonl(p)
            self.assertEqual(rows[1]["id"], 2)
