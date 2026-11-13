"""Integration test combining tokenizer, hasher, and JSONL persistence."""
import unittest, tempfile
from pathlib import Path
from rag_evals.utils import SimpleTokenizer, TextHasher, write_jsonl, read_jsonl

class TestUtilsIntegration(unittest.TestCase):
    def test_tokenize_hash_store(self):
        text = "Students must complete 75 percent attendance."
        tokens = SimpleTokenizer.tokenize_words(text)
        cid = TextHasher.make_chunk_id("handbook", 1, 0, text)
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "out.jsonl"
            write_jsonl(p, [{"chunk_id": cid, "tokens": tokens}])
            loaded = read_jsonl(p)
            self.assertEqual(loaded[0]["chunk_id"], cid)
