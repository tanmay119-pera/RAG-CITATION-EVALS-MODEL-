"""Interactive terminal REPL for querying the RAG system with citations."""

from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker
from rag_evals.generation.generator import GroundedGenerator
from rag_evals.generation.verifier import CitationVerifier
from rag_evals.ui.highlighter import TextHighlighter

def main():
    print("=== Academic Regulations RAG Interactive Shell ===")
    print("Type your question or 'exit' to quit.\n")

    retriever = HybridRetriever()
    reranker = CrossEncoderReranker()
    generator = GroundedGenerator()

    while True:
        try:
            q = input("Query > ").strip()
            if not q or q.lower() in ("exit", "quit"):
                break

            raw = retriever.retrieve(q, top_k=5, mode="hybrid")
            final = reranker.rerank(q, raw)
            ans, is_refused = generator.generate(q, final)

            v_res = CitationVerifier.verify(ans, {c.chunk_id for c in final})
            print("\n[ANSWER]")
            print(ans)
            print("\n[CITATIONS]")
            for cid in v_res.valid_ids:
                matching = next((c for c in final if c.chunk_id == cid), None)
                if matching:
                    highlighted = TextHighlighter.highlight_ansi(matching.text[:120], q.split())
                    print(f" - [{cid}] {matching.metadata.get('section_title', '')}: {highlighted}...")
            print("-" * 50 + "\n")
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
