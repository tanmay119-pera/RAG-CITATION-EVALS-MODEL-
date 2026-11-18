"""Latency profiling harness across retrieval and generation stages."""

import time
import json
from pathlib import Path
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker
from rag_evals.generation.generator import GroundedGenerator

def benchmark_latency(n_runs: int = 15) -> dict:
    retriever = HybridRetriever()
    reranker = CrossEncoderReranker()
    generator = GroundedGenerator()
    query = "What is the penalty for a first-time plagiarism violation?"

    retrieval_times = []
    rerank_times = []
    generation_times = []
    total_times = []

    for _ in range(n_runs):
        t0 = time.time()
        raw = retriever.retrieve(query, top_k=5, mode="hybrid")
        t1 = time.time()
        final = reranker.rerank(query, raw)
        t2 = time.time()
        ans, _ = generator.generate(query, final)
        t3 = time.time()

        retrieval_times.append((t1 - t0) * 1000)
        rerank_times.append((t2 - t1) * 1000)
        generation_times.append((t3 - t2) * 1000)
        total_times.append((t3 - t0) * 1000)

    retrieval_times.sort()
    total_times.sort()
    p50 = total_times[len(total_times) // 2]
    p90 = total_times[int(len(total_times) * 0.9)]

    profile = {
        "runs": n_runs,
        "avg_retrieval_ms": round(sum(retrieval_times) / n_runs, 2),
        "avg_rerank_ms": round(sum(rerank_times) / n_runs, 2),
        "avg_generation_ms": round(sum(generation_times) / n_runs, 2),
        "total_p50_ms": round(p50, 2),
        "total_p90_ms": round(p90, 2)
    }

    out_file = Path("data/eval/latency_benchmark.json")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(profile, indent=2), encoding="utf-8")
    print(f"Latency profile saved to {out_file}: P50={p50:.1f}ms, P90={p90:.1f}ms")
    return profile

if __name__ == "__main__":
    benchmark_latency()
