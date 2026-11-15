"""CLI utility to test and inspect retrieval modes and reranking."""

import argparse
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker

def main():
    parser = argparse.ArgumentParser(description="Test retrieval on a user query.")
    parser.add_argument("--query", required=True, help="Question or query string")
    parser.add_argument("--mode", default="hybrid", choices=["dense", "bm25", "hybrid"])
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--rerank", action="store_true")
    args = parser.parse_args()

    retriever = HybridRetriever()
    results = retriever.retrieve(args.query, top_k=args.top_k, mode=args.mode)

    if args.rerank:
        reranker = CrossEncoderReranker(top_n=args.top_k)
        results = reranker.rerank(args.query, results)

    print(f"\n--- Query: '{args.query}' (Mode: {args.mode}, Rerank: {args.rerank}) ---")
    for r in results:
        print(f"[{r.rank}] ID: {r.chunk_id} | Score: {r.score:.4f} | Section: {r.metadata.get('section_title', '')}")

if __name__ == "__main__":
    main()
