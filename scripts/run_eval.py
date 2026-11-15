"""Execute comprehensive evaluations across golden dataset and output results report."""

import json
from pathlib import Path
from rag_evals.config import load_config
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker
from rag_evals.generation.generator import GroundedGenerator
from rag_evals.generation.verifier import CitationVerifier
from rag_evals.eval.retrieval_metrics import RetrievalEvaluator

def run_benchmarks() -> dict:
    config = load_config()
    golden_path = config.eval_dir / "golden_set.jsonl"
    if not golden_path.is_file():
        raise FileNotFoundError(f"Missing evaluation dataset: {golden_path}")

    cases = []
    with open(golden_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                cases.append(json.loads(line))

    retriever = HybridRetriever(config)
    reranker = CrossEncoderReranker()
    generator = GroundedGenerator(config)

    retrieved_clauses = []
    refusal_correct = 0
    total_unanswerable = 0
    citation_valid_count = 0
    total_answered = 0

    print(f"Running benchmarks over {len(cases)} evaluation queries...")
    for case in cases:
        query = case["query"]
        raw = retriever.retrieve(query, top_k=5, mode="hybrid")
        reranked = reranker.rerank(query, raw)
        retrieved_clauses.append([c.text for c in reranked])

        ans, is_refused = generator.generate(query, reranked)
        if not case["is_answerable"]:
            total_unanswerable += 1
            if is_refused:
                refusal_correct += 1
        else:
            total_answered += 1
            valid_ids = {c.chunk_id for c in reranked}
            v_res = CitationVerifier.verify(ans, valid_ids)
            if v_res.is_valid:
                citation_valid_count += 1

    retrieval_stats = RetrievalEvaluator.evaluate(cases, retrieved_clauses)
    refusal_acc = refusal_correct / max(1, total_unanswerable)
    citation_prec = citation_valid_count / max(1, total_answered)

    report = {
        "total_cases": len(cases),
        "hit_at_1": round(retrieval_stats["hit_at_1"], 4),
        "hit_at_3": round(retrieval_stats["hit_at_3"], 4),
        "hit_at_5": round(retrieval_stats["hit_at_5"], 4),
        "mrr": round(retrieval_stats["mrr"], 4),
        "refusal_accuracy": round(refusal_acc, 4),
        "citation_precision": round(citation_prec, 4)
    }

    report_path = config.eval_dir / "eval_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\n================ EVALUATION BENCHMARK REPORT ================")
    print(f"Total Test Cases Evaluated : {report['total_cases']}")
    print(f"Hit@1 Retrieval Rate       : {report['hit_at_1'] * 100:.1f}%")
    print(f"Hit@3 Retrieval Rate       : {report['hit_at_3'] * 100:.1f}%")
    print(f"Hit@5 Retrieval Rate       : {report['hit_at_5'] * 100:.1f}%")
    print(f"Mean Reciprocal Rank (MRR) : {report['mrr']:.4f}")
    print(f"Refusal Accuracy (Negative): {report['refusal_accuracy'] * 100:.1f}%")
    print(f"Citation Precision         : {report['citation_precision'] * 100:.1f}%")
    print("=============================================================\n")
    return report

if __name__ == "__main__":
    run_benchmarks()
