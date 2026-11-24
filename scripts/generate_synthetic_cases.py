#!/usr/bin/env python3
"""CLI utility to generate synthetic QA pairs from processed chunks."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from rag_evals.eval.synthetic_eval_generator import SyntheticEvalGenerator

def main():
    p = Path("data/processed/chunks.jsonl")
    if not p.exists():
        print("No processed chunks found.")
        return
    chunks = [json.loads(l) for l in p.read_text().splitlines() if l.strip()][:5]
    gen = SyntheticEvalGenerator()
    cases = gen.batch_generate(chunks)
    print(f"Generated {len(cases)} synthetic test cases.")

if __name__ == "__main__":
    main()
