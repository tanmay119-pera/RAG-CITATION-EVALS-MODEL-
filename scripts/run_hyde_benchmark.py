#!/usr/bin/env python3
"""Benchmark standard retrieval vs HyDE-expanded retrieval."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.retrieval.hypothetical_document import HyDERetriever

def main():
    hyde = HyDERetriever()
    q = "What is the policy for medical leave?"
    expanded = hyde.expand_query(q)
    print("Original:", q)
    print("Expanded:", expanded)

if __name__ == "__main__":
    main()
