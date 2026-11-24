#!/usr/bin/env python3
"""CLI utility to quantize vector embeddings."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.index.vector_quantizer import ScalarQuantizer

def main():
    sq = ScalarQuantizer()
    dummy_vec = [0.12, -0.45, 0.88, 0.03]
    q, mi, ma = sq.quantize(dummy_vec)
    print(f"Quantized vector: {q} (min={mi:.2f}, max={ma:.2f})")

if __name__ == "__main__":
    main()
