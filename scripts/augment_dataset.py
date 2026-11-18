"""Dataset augmentation tool generating query variations for robustness testing."""

import json
from pathlib import Path
from rag_evals.retrieval.multi_query import MultiQueryGenerator

def augment_dataset():
    golden_path = Path("data/eval/golden_set.jsonl")
    cases = [json.loads(line) for line in golden_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    augmented = []
    for c in cases[:10]:
        variations = MultiQueryGenerator.expand(c["query"])
        for idx, var in enumerate(variations[1:], start=1):
            aug_case = dict(c)
            aug_case["case_id"] = f"{c['case_id']}_aug_{idx}"
            aug_case["query"] = var
            aug_case["is_augmented"] = True
            augmented.append(aug_case)

    out_path = Path("data/eval/augmented_queries.jsonl")
    out_path.write_text("\n".join(json.dumps(a) for a in augmented) + "\n", encoding="utf-8")
    print(f"Generated {len(augmented)} augmented test cases in {out_path}")

if __name__ == "__main__":
    augment_dataset()
