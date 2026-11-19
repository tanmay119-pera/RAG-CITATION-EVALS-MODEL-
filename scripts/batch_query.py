"""Batch query processor executing test queries and outputting results."""

import sys
import json
from pathlib import Path

# Add repo root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.ask import ask

def run_batch_queries():
    queries = [
        "What is the penalty for academic integrity violations?",
        "How many credits are required for graduation?",
        "When is the tuition refund deadline?"
    ]
    results = []
    for q in queries:
        res = ask(q)
        results.append({
            "query": q,
            "answer": res["answer"],
            "citations": res["verification"].valid_ids
        })

    out_file = REPO_ROOT / "data/eval/batch_results.json"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Batch processed {len(results)} queries -> {out_file}")

if __name__ == "__main__":
    run_batch_queries()
