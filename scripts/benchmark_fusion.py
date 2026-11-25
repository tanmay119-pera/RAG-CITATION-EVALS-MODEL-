#!/usr/bin/env python3
"""Sweep RRF k values across sample rank lists."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.retrieval.reciprocal_fusion_tuner import RRFTuner

if __name__ == "__main__":
    for k in (20, 60, 100):
        print(f"k={k} -> {RRFTuner.fuse([['c1', 'c2'], ['c2', 'c3']], k=k)}")
