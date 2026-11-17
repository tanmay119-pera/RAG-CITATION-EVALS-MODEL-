"""Unit tests for semantic splitter, table parser, and metadata enricher."""

import unittest
from rag_evals.ingest.semantic_chunker import SemanticSplitter
from rag_evals.ingest.table_parser import TableParser
from rag_evals.ingest.enricher import MetadataEnricher

class TestIngestAdvanced(unittest.TestCase):
    def test_semantic_splitter(self):
        text = "First rule. Second rule! Third question?"
        sents = SemanticSplitter.split_sentences(text)
        self.assertEqual(len(sents), 3)

    def test_table_parser(self):
        sample = "| Grade | Points |\n|---|---|\n| A | 4.0 |"
        tables = TableParser.extract_tables(sample)
        self.assertEqual(len(tables), 1)

    def test_metadata_enricher(self):
        text = "Under Clause 3.2, an Incomplete grade requires GPA verification."
        meta = MetadataEnricher.enrich(text, {"file_name": "handbook.txt"})
        self.assertIn("3.2", meta["detected_clauses"])
        self.assertIn("gpa", meta["keywords"])

if __name__ == "__main__":
    unittest.main()
