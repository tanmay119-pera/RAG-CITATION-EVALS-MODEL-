#!/usr/bin/env python3
"""Run A/B answer comparison between two configurations."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.eval.answer_comparator import AnswerComparator

def main():
    comparator = AnswerComparator()
    pair = {
        "a": "Students must maintain 75% attendance. [c1]",
        "cit_a": ["c1"],
        "b": "Attendance must be at least 75%. [c1][c2]",
        "cit_b": ["c1", "c2"]
    }
    res = comparator.compare(pair["a"], pair["cit_a"], pair["b"], pair["cit_b"])
    print(f"Similarity: {res.similarity:.2f} | Verdict: {res.verdict}")

if __name__ == "__main__":
    main()
