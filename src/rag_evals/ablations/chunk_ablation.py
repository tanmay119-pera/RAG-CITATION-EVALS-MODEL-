"""Evaluates the impact of chunk sizes on retrieval accuracy."""

import json
from typing import List, Dict, Any
from rag_evals.ingest.loader import DocumentLoader
from rag_evals.ingest.chunker import Chunker
from rag_evals.index.bm25 import BM25Index
from rag_evals.config import load_config

def run_chunk_ablation(chunk_sizes: List[int] = [150, 300, 450, 600]) -> List[Dict[str, Any]]:
    config = load_config()
    raw_files = list(config.raw_data_dir.glob("*.txt"))
    docs = []
    for f in raw_files:
        docs.extend(DocumentLoader.load_file(f))

    golden = []
    with open(config.eval_dir / "golden_set.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            if item.get("is_answerable", True):
                golden.append(item)

    results = []
    for size in chunk_sizes:
        chunker = Chunker(target_chunk_tokens=size, overlap_tokens=int(size * 0.1))
        chunks = []
        for d in docs:
            chunks.extend(chunker.split_document(d))

        bm25 = BM25Index()
        bm25.build([c.chunk_id for c in chunks], [c.text for c in chunks])

        hits_at_1 = 0
        hits_at_5 = 0
        for case in golden:
            hits = bm25.search(case["query"], top_k=5)
            hit_texts = [next((c.text for c in chunks if c.chunk_id == cid), "") for cid, _ in hits]
            clause = case["expected_clause"].lower()
            if hit_texts and clause in hit_texts[0].lower():
                hits_at_1 += 1
            if any(clause in t.lower() for t in hit_texts):
                hits_at_5 += 1

        n = max(1, len(golden))
        results.append({
            "chunk_size": size,
            "total_chunks": len(chunks),
            "hit_at_1": round(hits_at_1 / n, 4),
            "hit_at_5": round(hits_at_5 / n, 4)
        })
    return results
