"""Integration test for ingest structural metadata helpers."""
import unittest
from rag_evals.ingest import LayoutHintExtractor, SectionStackTracker, PageOffsetMapper

class TestIngestMetadataPipeline(unittest.TestCase):
    def test_structural_tracking(self):
        st = SectionStackTracker()
        st.update("# Academic Regulations")
        st.update("## Attendance Rule")
        self.assertTrue(LayoutHintExtractor.is_heading("SECTION 2"))
        pm = PageOffsetMapper([50, 50])
        self.assertEqual(st.current_path(), "Academic Regulations > Attendance Rule")
        self.assertEqual(pm.page_for_offset(75), 2)
