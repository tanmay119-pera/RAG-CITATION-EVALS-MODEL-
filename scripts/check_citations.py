#!/usr/bin/env python3
"""Check normalized citation formatting."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.generation.citation_normalizer import CitationNormalizer

if __name__ == "__main__":
    sample = "Attendance must be 75% [chunk: doc_p1_c0]."
    print(CitationNormalizer.normalize(sample))
