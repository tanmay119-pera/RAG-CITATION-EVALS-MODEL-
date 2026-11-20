#!/usr/bin/env python3
"""CLI health check runner."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.api.health import HealthChecker

def main():
    hc = HealthChecker()
    print(json.dumps(hc.check_all(), indent=2))

if __name__ == "__main__":
    main()
