"""Okapi BM25 keyword index for sparse lexical retrieval."""

import math
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple

class BM25Index:
    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.doc_ids: List[str] = []
        self.doc_lengths: List[int] = []
        self.avg_doc_length: float = 0.0
        self.doc_term_freqs: List[Dict[str, int]] = []
        self.idf: Dict[str, float] = {}

    @staticmethod
    def tokenize(text: str) -> List[str]:
        return [w.lower() for w in re.findall(r"\w+", text) if len(w) > 1]

    def build(self, doc_ids: List[str], texts: List[str]):
        self.doc_ids = doc_ids
        n_docs = len(texts)
        if n_docs == 0:
            return

        total_length = 0
        df: Dict[str, int] = {}
        self.doc_term_freqs = []
        self.doc_lengths = []

        for text in texts:
            tokens = self.tokenize(text)
            self.doc_lengths.append(len(tokens))
            total_length += len(tokens)
            tf: Dict[str, int] = {}
            for t in tokens:
                tf[t] = tf.get(t, 0) + 1
            self.doc_term_freqs.append(tf)
            for t in tf:
                df[t] = df.get(t, 0) + 1

        self.avg_doc_length = total_length / n_docs if n_docs else 0.0

        for term, freq in df.items():
            self.idf[term] = math.log(1.0 + (n_docs - freq + 0.5) / (freq + 0.5))

    def search(self, query: str, top_k: int = 10) -> List[Tuple[str, float]]:
        q_tokens = self.tokenize(query)
        scores = [0.0] * len(self.doc_ids)

        for token in q_tokens:
            if token not in self.idf:
                continue
            idf_val = self.idf[token]
            for i, tf_dict in enumerate(self.doc_term_freqs):
                if token in tf_dict:
                    freq = tf_dict[token]
                    doc_len = self.doc_lengths[i]
                    num = freq * (self.k1 + 1.0)
                    denom = freq + self.k1 * (1.0 - self.b + self.b * (doc_len / self.avg_doc_length))
                    scores[i] += idf_val * (num / denom)

        ranked = sorted(zip(self.doc_ids, scores), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    def save(self, path: Path):
        data = {
            "doc_ids": self.doc_ids,
            "doc_lengths": self.doc_lengths,
            "avg_doc_length": self.avg_doc_length,
            "doc_term_freqs": self.doc_term_freqs,
            "idf": self.idf
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load(self, path: Path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.doc_ids = data["doc_ids"]
        self.doc_lengths = data["doc_lengths"]
        self.avg_doc_length = data["avg_doc_length"]
        self.doc_term_freqs = data["doc_term_freqs"]
        self.idf = data["idf"]
