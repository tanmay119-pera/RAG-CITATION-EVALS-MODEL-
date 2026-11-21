#!/usr/bin/env python3
"""Print summary statistics for the processed corpus."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.index.statistics import IndexStatistics

def main():
    p = Path("data/processed/chunks.jsonl")
    if not p.exists():
        print("No processed chunks found.")
        return
    chunks = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
    stats = IndexStatistics()
    print(json.dumps(stats.report(chunks), indent=2))

if __name__ == "__main__":
    main()
