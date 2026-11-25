"""Target SLA thresholds for release gates."""
EVAL_THRESHOLDS = {
    "recall_at_5": 0.75,
    "mrr": 0.65,
    "faithfulness": 0.85,
    "citation_fidelity": 0.80,
}

def passes_release_gates(metrics: dict) -> bool:
    return all(metrics.get(k, 0.0) >= v for k, v in EVAL_THRESHOLDS.items())
