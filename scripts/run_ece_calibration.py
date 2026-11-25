#!/usr/bin/env python3
"""Evaluate mock confidence calibration."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.eval.calibration_metrics import CalibrationEvaluator

if __name__ == "__main__":
    ece = CalibrationEvaluator.expected_calibration_error([0.9, 0.8, 0.2], [1, 1, 0])
    print(f"Sample ECE: {ece}")
