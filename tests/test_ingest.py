"""Unit tests for loader, cleaner, chunker, and ingestion pipeline."""

import unittest
from pathlib import Path
from rag_evals.ingest.loader import Document, DocumentLoader
from rag_evals.ingest.cleaner import TextCleaner
from rag_evals.ingest.chunker import Chunker
from scripts.ingest import run_ingestion

class TestIngest(unittest.TestCase):
    def test_text_cleaner(self):
        dirty = "  Hello   world!  \r\n\n\n\nNext line.  "
        clean = TextCleaner.clean(dirty)
        self.assertEqual(clean, "Hello world!\n\nNext line.")

    def test_section_extraction(self):
        sample = "SECTION 2: COURSE REGISTRATION\nClause 2.1 - Add/Drop"
        title = TextCleaner.extract_section_title(sample)
        self.assertIn("SECTION 2", title)

    def test_chunker_metadata(self):
        doc = Document(
            doc_id="test_doc",
            content="SECTION 1: INTEGRITY\n\nClause 1.1\n\nSome academic rules here.",
            metadata={"file_name": "test.txt", "page_number": 1}
        )
        chunker = Chunker(target_chunk_tokens=50, overlap_tokens=5)
        chunks = chunker.split_document(doc)
        self.assertGreaterEqual(len(chunks), 1)
        self.assertTrue(chunks[0].chunk_id.startswith("test.txt_p1"))
        self.assertEqual(chunks[0].metadata["page_number"], 1)

    def test_run_ingestion(self):
        out = run_ingestion()
        self.assertTrue(out.exists())
        self.assertGreater(out.stat().st_size, 0)

if __name__ == "__main__":
    unittest.main()
