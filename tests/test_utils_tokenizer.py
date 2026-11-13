"""Tests for SimpleTokenizer."""
import unittest
from rag_evals.utils.tokenizer import SimpleTokenizer

class TestTokenizer(unittest.TestCase):
    def test_tokenize_and_ngrams(self):
        words = SimpleTokenizer.tokenize_words("University Rules 2026!")
        self.assertEqual(words, ["university", "rules", "2026"])
        bigrams = SimpleTokenizer.word_ngrams("a b c", 2)
        self.assertEqual(bigrams, [("a", "b"), ("b", "c")])

    def test_split_sentences(self):
        sents = SimpleTokenizer.split_sentences("First rule. Second rule! Third?")
        self.assertEqual(len(sents), 3)
