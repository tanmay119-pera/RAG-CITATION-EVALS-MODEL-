"""Unit tests for cross-validation splitter."""

import unittest
from rag_evals.eval.cv_splitter import CrossValidationSplitter

class TestCVSplitter(unittest.TestCase):
    def test_k_fold_split(self):
        cases = [{"id": i} for i in range(25)]
        splits = CrossValidationSplitter.split(cases, k_folds=5)
        self.assertEqual(len(splits), 5)
        for train, test in splits:
            self.assertEqual(len(test), 5)
            self.assertEqual(len(train), 20)

if __name__ == "__main__":
    unittest.main()
