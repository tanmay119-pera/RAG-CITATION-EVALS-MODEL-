"""UI and citation formatter smoke tests."""

import unittest
from pathlib import Path
from rag_evals.generation.verifier import CitationVerifier

class TestUI(unittest.TestCase):
    def test_app_script_exists(self):
        self.assertTrue(Path("app.py").is_file())

    def test_citation_badge_extraction(self):
        text = "Under Clause 1.2 [univ_reg_p1_c1], penalties are strictly enforced."
        cids = CitationVerifier.extract_citations(text)
        self.assertEqual(cids, ["univ_reg_p1_c1"])

if __name__ == "__main__":
    unittest.main()
