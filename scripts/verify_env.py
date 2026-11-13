#!/usr/bin/env python3
"""Inspect runtime environment readiness."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.utils.env_check import EnvironmentInspector

if __name__ == "__main__":
    print(json.dumps(EnvironmentInspector.report(), indent=2))
