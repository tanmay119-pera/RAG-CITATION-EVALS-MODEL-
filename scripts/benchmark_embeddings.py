"""Benchmark suite for embedding cosine similarity vs Euclidean distance."""

import json
import math
from pathlib import Path
from rag_evals.index.embedder import GeminiEmbedder

def benchmark_embeddings():
    embedder = GeminiEmbedder()
    queries = ["plagiarism penalty", "tuition refund deadline", "dean list gpa"]
    vectors = [embedder.embed_query(q) for q in queries]

    results = []
    for i, q1 in enumerate(queries):
        for j, q2 in enumerate(queries):
            v1, v2 = vectors[i], vectors[j]
            cos_sim = sum(a * b for a, b in zip(v1, v2))
            euc_dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))
            results.append({
                "pair": f"{q1} <-> {q2}",
                "cosine_similarity": round(cos_sim, 4),
                "euclidean_distance": round(euc_dist, 4)
            })

    out_file = Path("data/eval/embedding_benchmark.json")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Embedding benchmark written to {out_file}")

if __name__ == "__main__":
    benchmark_embeddings()
