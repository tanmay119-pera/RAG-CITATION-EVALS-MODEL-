"""End-to-end RAG question-answering CLI with citations and verification."""

import argparse
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker
from rag_evals.generation.generator import GroundedGenerator
from rag_evals.generation.verifier import CitationVerifier

def ask(question: str) -> dict:
    retriever = HybridRetriever()
    reranker = CrossEncoderReranker()
    generator = GroundedGenerator()

    # 1. Retrieve & Rerank
    raw_chunks = retriever.retrieve(question, top_k=6, mode="hybrid")
    reranked_chunks = reranker.rerank(question, raw_chunks)

    # 2. Generate
    answer, is_refusal = generator.generate(question, reranked_chunks)

    # 3. Verify
    valid_ids = {c.chunk_id for c in reranked_chunks}
    verification = CitationVerifier.verify(answer, valid_ids)

    return {
        "question": question,
        "answer": answer,
        "is_refusal": is_refusal,
        "verification": verification,
        "source_chunks": reranked_chunks
    }

def main():
    parser = argparse.ArgumentParser(description="Ask a question against the RAG system.")
    parser.add_argument("--question", required=True, help="Question to ask")
    args = parser.parse_args()

    res = ask(args.question)
    print("\n=======================================================")
    print(f"QUESTION: {res['question']}")
    print(f"ANSWER:\n{res['answer']}")
    print(f"REFUSAL: {res['is_refusal']}")
    print(f"VALID CITATIONS: {res['verification'].valid_ids}")
    print(f"INVALID CITATIONS: {res['verification'].invalid_ids}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
