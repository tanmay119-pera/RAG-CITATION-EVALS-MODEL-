"""Tests for HallucinationGrader."""
import unittest
from rag_evals.generation.hallucination_grader import HallucinationGrader

class TestHallucinationGrader(unittest.TestCase):
    def test_grade_high_grounding(self):
        hg = HallucinationGrader()
        ans = "Attendance must be 75 percent for semester exams."
        src = ["Students need 75 percent attendance to qualify for semester exams."]
        res = hg.grade(ans, src)
        self.assertGreater(res["grounding_ratio"], 0.7)
        self.assertLess(res["hallucination_risk"], 0.3)

    def test_grade_empty(self):
        hg = HallucinationGrader()
        res = hg.grade("", ["some text"])
        self.assertEqual(res["grounding_ratio"], 1.0)
