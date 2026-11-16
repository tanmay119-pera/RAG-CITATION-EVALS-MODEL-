"""Measures the performance delta with and without Cross-Encoder Reranker."""

import json
from typing import List, Dict, Any
from rag_evals.config import load_config
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker

def run_reranker_ablation() -> List[Dict[str, Any]]:
    config = load_config()
    golden = []
    with open(config.eval_dir / "golden_set.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            if item.get("is_answerable", True):
                golden.append(item)

    retriever = HybridRetriever(config)
    reranker = CrossEncoderReranker(top_n=5)

    configs = [
        {"name": "No Reranker (Hybrid RRF)", "rerank": False},
        {"name": "With Reranker (Cross-Encoder)", "rerank": True}
    ]
    results = []
    for cfg in configs:
        hit_1 = 0
        mrr_total = 0.0
        for case in golden:
            hits = retriever.retrieve(case["query"], top_k=5, mode="hybrid")
            if cfg["rerank"]:
                hits = reranker.rerank(case["query"], hits)
            clause = case["expected_clause"].lower()
            for r, h in enumerate(hits, start=1):
                if clause in h.text.lower():
                    if r == 1:
                        hit_1 += 1
                    mrr_total += 1.0 / r
                    break
        n = max(1, len(golden))
        results.append({
            "configuration": cfg["name"],
            "hit_at_1": round(hit_1 / n, 4),
            "mrr": round(mrr_total / n, 4)
        })
    return results
