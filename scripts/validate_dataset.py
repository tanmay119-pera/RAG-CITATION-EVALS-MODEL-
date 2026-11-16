"""Validate golden evaluation dataset integrity and clause consistency."""

import json
from pathlib import Path
from rag_evals.config import load_config

def validate_dataset(filepath: Path) -> dict:
    if not filepath.is_file():
        raise FileNotFoundError(f"Dataset not found: {filepath}")

    cases = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))

    queries = set()
    categories = {}
    answerable_count = 0
    unanswerable_count = 0

    for c in cases:
        q = c.get("query", "").strip()
        if not q or q in queries:
            raise ValueError(f"Invalid or duplicate query: {q}")
        queries.add(q)
        cat = c.get("category", "general")
        categories[cat] = categories.get(cat, 0) + 1
        if c.get("is_answerable", True):
            answerable_count += 1
        else:
            unanswerable_count += 1

    stats = {
        "total_cases": len(cases),
        "answerable": answerable_count,
        "unanswerable": unanswerable_count,
        "categories": categories
    }
    print(f"Validated {len(cases)} cases successfully.")
    return stats

if __name__ == "__main__":
    config = load_config()
    validate_dataset(config.eval_dir / "golden_set.jsonl")
