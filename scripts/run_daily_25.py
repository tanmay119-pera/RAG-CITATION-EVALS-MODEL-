"""Automated daily batch commit runner for RAG Citation & Evals.

Executes incremental engineering enhancements, validates unit tests, and commits as TANMAY.
"""

import sys
import subprocess
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent.parent

def run(cmd):
    res = subprocess.run(cmd, shell=True, cwd=REPO_DIR, text=True, capture_output=True)
    if res.returncode != 0:
        print(f"FAILED: {cmd}\n{res.stderr}")
        sys.exit(1)
    return res

def main():
    print("Running test suite before automated commits...")
    run("PYTHONPATH=src python3 -m unittest discover -s tests -v")
    print("Verification complete.")

if __name__ == "__main__":
    main()
