"""5-fold cross-validation splitter for golden evaluation benchmark sets."""

from typing import List, Dict, Any, Tuple

class CrossValidationSplitter:
    @staticmethod
    def split(cases: List[Dict[str, Any]], k_folds: int = 5) -> List[Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]]:
        folds = [[] for _ in range(k_folds)]
        for i, c in enumerate(cases):
            folds[i % k_folds].append(c)

        splits = []
        for i in range(k_folds):
            test_set = folds[i]
            train_set = []
            for j in range(k_folds):
                if j != i:
                    train_set.extend(folds[j])
            splits.append((train_set, test_set))
        return splits
