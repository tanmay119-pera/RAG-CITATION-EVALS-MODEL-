"""Tests for SectionStackTracker."""
import unittest
from rag_evals.ingest.section_tracker import SectionStackTracker

class TestSectionTracker(unittest.TestCase):
    def test_breadcrumb_hierarchy(self):
        st = SectionStackTracker()
        st.update("# Academics")
        st.update("## Attendance")
        self.assertEqual(st.current_path(), "Academics > Attendance")
        st.update("# Examinations")
        self.assertEqual(st.current_path(), "Examinations")
