# Evaluation Methodology

## Golden Test Suite

Our evaluation suite uses 50-100 gold question-answer pairs curated from academic policies.
Each record specifies:
- `query`: User question
- `golden_answer`: Reference answer
- `golden_chunk_ids`: Source chunks containing ground-truth evidence
- `is_refusal`: Ground truth indication of unanswerable queries

## Metrics Overview

1. **Retrieval**: Recall@5, MRR, NDCG@5
2. **Faithfulness**: Hallucination detection rate and atomic claim verification
3. **Citations**: Precision, recall, and Citation Fidelity Index (CFI)
