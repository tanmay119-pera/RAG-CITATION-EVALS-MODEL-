# Architecture and Design Decisions

## 1. Hybrid Search (Dense + Lexical)
We combine dense vector similarity with Okapi BM25 sparse keyword matching using Reciprocal Rank Fusion (RRF). This prevents failures on exact course codes, regulation numbers, and acronyms.

## 2. Chunk Size Selection
Empirical ablations across 200, 400, and 600 token window lengths revealed 450 tokens with 50-token overlap achieves the highest Recall@5 while preserving coherent semantic boundaries.

## 3. Strict Citation Verification
Every claim produced by the generator must be linked to a retrieved chunk identifier in bracket notation (`[chunk_id]`). Verification runs programmatically prior to presenting the response.
