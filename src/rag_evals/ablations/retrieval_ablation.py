"""Compares Dense-only vs BM25-only vs Hybrid RRF retrieval."""

import json
from typing import List, Dict, Any
from rag_evals.config import load_config
from rag_evals.retrieval.hybrid import HybridRetriever

def run_retrieval_ablation() -> List[Dict[str, Any]]:
    config = load_config()
    golden = []
    with open(config.eval_dir / "golden_set.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            if item.get("is_answerable", True):
                golden.append(item)

    retriever = HybridRetriever(config)
    modes = ["dense", "bm25", "hybrid"]
    results = []

    for mode in modes:
        hit_1 = 0
        hit_5 = 0
        mrr_total = 0.0

        for case in golden:
            hits = retriever.retrieve(case["query"], top_k=5, mode=mode)
            clause = case["expected_clause"].lower()
            found_rank = None
            for r, h in enumerate(hits, start=1):
                if clause in h.text.lower():
                    found_rank = r
                    break
            if found_rank is not None:
                if found_rank == 1:
                    hit_1 += 1
                hit_5 += 1
                mrr_total += 1.0 / found_rank

        n = max(1, len(golden))
        results.append({
            "retrieval_mode": mode.upper(),
            "hit_at_1": round(hit_1 / n, 4),
            "hit_at_5": round(hit_5 / n, 4),
            "mrr": round(mrr_total / n, 4)
        })
    return results
