#!/usr/bin/env python3
"""CLI utility to validate pipeline configuration files."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.config_validator import ConfigValidator

def main():
    cfg = {"chunk_size": 450, "overlap": 50, "top_k": 5}
    validator = ConfigValidator()
    errs = validator.validate(cfg)
    if errs:
        print("Validation errors:", errs)
        sys.exit(1)
    print("Configuration is valid.")

if __name__ == "__main__":
    main()
