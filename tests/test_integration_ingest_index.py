"""Integration test from document loading through BM25 indexing."""
import unittest, tempfile
from pathlib import Path
from rag_evals.ingest.loader import DocumentLoader
from rag_evals.ingest.cleaner import TextCleaner
from rag_evals.ingest.chunker import Chunker
from rag_evals.index.bm25 import BM25Index

class TestIngestToIndexPipeline(unittest.TestCase):
    def test_pipeline_integration(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "sample.txt"
            f.write_text("University rules specify that attendance must be at least 75 percent for semester exams.")
            docs = DocumentLoader.load_file(f)
            self.assertEqual(len(docs), 1)

            chunker = Chunker(target_chunk_tokens=50, overlap_tokens=5)
            chunks = chunker.split_document(docs[0])
            self.assertGreater(len(chunks), 0)

            bm25 = BM25Index()
            bm25.build([c.chunk_id for c in chunks], [c.text for c in chunks])
            results = bm25.search("attendance")
            self.assertGreater(len(results), 0)
