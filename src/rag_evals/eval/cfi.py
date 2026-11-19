"""Citation Faithfulness Index (CFI) metric harmonizing precision and recall."""

class CFIEvaluator:
    """Computes the harmonic mean of citation precision and citation recall."""

    @staticmethod
    def compute_cfi(precision: float, recall: float) -> float:
        if precision + recall == 0:
            return 0.0
        return round(2 * (precision * recall) / (precision + recall), 4)
