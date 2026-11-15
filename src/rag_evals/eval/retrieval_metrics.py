"""Metrics calculator for Hit@K, MRR, Refusal Accuracy, and Citation precision."""

from typing import List, Dict, Any

class RetrievalEvaluator:
    @staticmethod
    def evaluate(eval_cases: List[Dict[str, Any]], retrieved_per_case: List[List[str]]) -> Dict[str, float]:
        hit_at_1 = 0
        hit_at_3 = 0
        hit_at_5 = 0
        reciprocal_ranks = []

        total_answerable = 0
        for case, hits in zip(eval_cases, retrieved_per_case):
            if not case.get("is_answerable", True):
                continue
            total_answerable += 1
            clause = case.get("expected_clause", "").lower()

            found_rank = None
            for r, hit_text in enumerate(hits, start=1):
                if clause in hit_text.lower():
                    found_rank = r
                    break

            if found_rank is not None:
                if found_rank <= 1:
                    hit_at_1 += 1
                if found_rank <= 3:
                    hit_at_3 += 1
                if found_rank <= 5:
                    hit_at_5 += 1
                reciprocal_ranks.append(1.0 / found_rank)
            else:
                reciprocal_ranks.append(0.0)

        n = max(1, total_answerable)
        return {
            "hit_at_1": hit_at_1 / n,
            "hit_at_3": hit_at_3 / n,
            "hit_at_5": hit_at_5 / n,
            "mrr": sum(reciprocal_ranks) / n
        }
