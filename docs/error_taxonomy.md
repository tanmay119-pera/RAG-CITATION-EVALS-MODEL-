# RAG Error Taxonomy & Mitigation Playbook

| Error Code | Error Mode | Symptom | Root Cause | Engineering Mitigation |
|---|---|---|---|---|
| `ERR_RET_01` | Retrieval Miss | Expected clause not in Top-5 | Lexical mismatch or embedding drift | Multi-Query expansion + Hybrid RRF search |
| `ERR_RET_02` | Reranker Drop | Clause in Top-10 dropped by reranker | Over-aggressive term filter | Blend initial retrieval rank score into reranker ($0.4 RRF + 0.6 coverage$) |
| `ERR_GEN_01` | Hallucinated ID | Model cites `[chunk_99]` (nonexistent) | LLM autoregressive token drift | Programmatic regex validation in `CitationVerifier` |
| `ERR_GEN_02` | Ungrounded Claim | Statement without corresponding citation | Context window overflow or prompt drift | Enforce sentence-level citation format in prompt |
| `ERR_REF_01` | False Refusal | Model says "I don't know" to valid query | High grounding refusal threshold | Calibrate keyword intersection cutoff |
