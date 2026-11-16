"""Generate detailed failure analysis report in docs/failure_analysis.md."""

import json
from pathlib import Path
from rag_evals.config import load_config
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker
from rag_evals.generation.generator import GroundedGenerator
from rag_evals.generation.verifier import CitationVerifier
from rag_evals.eval.failure_analysis import FailureClassifier

def analyze_failures() -> Path:
    config = load_config()
    with open(config.eval_dir / "golden_set.jsonl", "r", encoding="utf-8") as f:
        cases = [json.loads(line) for line in f if line.strip()]

    retriever = HybridRetriever(config)
    reranker = CrossEncoderReranker()
    generator = GroundedGenerator(config)

    failures = []
    for c in cases:
        raw = retriever.retrieve(c["query"], top_k=5, mode="hybrid")
        reranked = reranker.rerank(c["query"], raw)
        texts = [chunk.text for chunk in reranked]
        ans, is_refused = generator.generate(c["query"], reranked)
        v_res = CitationVerifier.verify(ans, {chunk.chunk_id for chunk in reranked})
        record = FailureClassifier.classify(c, texts, ans, is_refused, v_res.is_valid)
        if record:
            failures.append(record)

    doc_path = Path("docs/failure_analysis.md")
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# RAG System Failure Analysis and Diagnostics",
        "",
        f"Total Evaluated Cases: {len(cases)}",
        f"Total Diagnosed Failures: {len(failures)}",
        f"System Success Rate: {((len(cases) - len(failures)) / len(cases)) * 100:.1f}%",
        "",
        "## Diagnostic Breakdown",
        ""
    ]
    by_type = {}
    for f in failures:
        by_type[f.failure_type] = by_type.get(f.failure_type, 0) + 1
    for ft, count in by_type.items():
        lines.append(f"- **{ft}**: {count} instances")

    lines.extend(["", "## Detailed Log", "", "| Case ID | Mode | Query | Details |", "|---|---|---|---|"])
    for f in failures:
        lines.append(f"| `{f.case_id}` | `{f.failure_type}` | {f.query[:45]}... | {f.details} |")

    doc_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Failure analysis written to {doc_path}")
    return doc_path

if __name__ == "__main__":
    analyze_failures()
