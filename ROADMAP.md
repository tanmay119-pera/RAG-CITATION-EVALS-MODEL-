# RAG System with Citations & Evals — 31-Day Build Roadmap (Nov 13 – Dec 13, 2026)

This repository implements an end-to-end **Retrieval-Augmented Generation (RAG)** system with **verifiable chunk-level citations**, **hybrid retrieval (Gemini embeddings + BM25 + cross-encoder reranking)**, **systematic evaluation**, **ablation studies**, and an **interactive UI**.

---

## Architecture Overview

1. **Corpus (50–200 pages)**: Real-world public PDF documents (university academic handbook or open technical policy manual) stored in `data/raw/`.
2. **Ingestion & Chunking**: PDF parsing with page numbers and section headers, cleaned and split into 300–600 token overlapping chunks with rich citation metadata.
3. **Hybrid Indexing**: Dense embeddings via `google-genai` (`gemini-embedding-001`) in FAISS/Chroma + sparse lexical index via `rank_bm25`.
4. **Retrieval & Reranking**: Top-K hybrid retrieval (Reciprocal Rank Fusion) with optional cross-encoder reranking.
5. **Grounded Generation & Verification**: `google-genai` (`gemini-3.8-flash`) constrained to retrieved chunks, inline `[chunk_id]` citations, explicit `"I don't know"` refusal on unanswerable queries, and programmatic citation ID verification.
6. **Evaluations**: 60+ golden Q&A pairs (including unanswerable negatives) measuring Retrieval (`Hit@5`, `Recall@5`, `MRR`), Faithfulness/Correctness, Citation Support, and Refusal Accuracy.
7. **Ablations & Error Analysis**: Controlled one-variable-at-a-time experiments recorded in a reproducible results table plus honest failure-case documentation.
8. **Demo UI**: Interactive Streamlit/Gradio app with clickable inline citations revealing source file, page number, section title, and exact passage.

---

## 31-Day Milestone Checklist (1 Commit / Day: Nov 13 – Dec 13, 2026)

### Step 1 — Corpus & Project Setup (Nov 13 – Nov 15)
- [x] **M01 (Nov 13)**: Project scaffolding (`pyproject.toml`, `requirements.txt`, `src/rag_evals/`, `.env.example`, config loader, initial smoke tests)
- [x] **M02 (Nov 14)**: Public 50–200 page PDF corpus acquisition script (`scripts/fetch_corpus.py`) with checksums and source URL tracking
- [x] **M03 (Nov 15)**: Corpus audit & manifest generator (`scripts/audit_corpus.py`, `data/corpus_manifest.json`) verifying page counts and metadata

### Step 2 — Ingestion & Chunking (Nov 16 – Nov 18)
- [x] **M04 (Nov 16)**: PDF loader & text cleaner (`src/rag_evals/ingest/pdf_loader.py`) preserving page numbers and section titles + unit tests
- [x] **M05 (Nov 17)**: Token-aware overlapping chunker (300–600 tokens) with citation metadata (`src/rag_evals/ingest/chunker.py`) + unit tests
- [x] **M06 (Nov 18)**: Ingestion CLI (`scripts/ingest.py`) producing `data/processed/chunks.jsonl` + chunk distribution summary

### Step 3 — Embeddings, Vector Store & BM25 (Nov 19 – Nov 22)
- [x] **M07 (Nov 19)**: Gemini embedding client (`google-genai`, `gemini-embedding-001`) with batching, retries, and mocked offline tests
- [x] **M08 (Nov 20)**: Persistent SQLite/disk embedding cache (`src/rag_evals/index/embed_cache.py`) keyed by `chunk_id` + content hash
- [x] **M09 (Nov 21)**: Persistent FAISS/Chroma vector store (`src/rag_evals/index/vector_store.py`) + build/query tests
- [x] **M10 (Nov 22)**: BM25 sparse keyword index (`src/rag_evals/index/bm25_index.py`) with serialization + unit tests

### Step 4 — Hybrid Retrieval & Reranking (Nov 23 – Nov 26)
- [x] **M11 (Nov 23)**: Unified index builder CLI (`scripts/build_index.py`) building dense vector store and BM25 index from `chunks.jsonl`
- [x] **M12 (Nov 24)**: Hybrid retriever combining dense + BM25 via Reciprocal Rank Fusion (`src/rag_evals/retrieval/hybrid.py`) + unit tests
- [x] **M13 (Nov 25)**: Cross-encoder reranker module (`src/rag_evals/retrieval/reranker.py`) with configurable top-K/top-N & toggle + tests
- [x] **M14 (Nov 26)**: Unified retrieval CLI (`scripts/retrieve.py`) comparing Dense, BM25, Hybrid RRF, and Reranked scores side-by-side

### Step 5 — Generation with Verifiable Citations (Nov 27 – Nov 30)
- [x] **M15 (Nov 27)**: Citation-enforcing prompt template & Gemini (`gemini-3.8-flash`) generator (`src/rag_evals/generation/generator.py`) + mocked tests
- [x] **M16 (Nov 28)**: Programmatic citation verifier (`src/rag_evals/generation/verifier.py`) checking cited IDs against retrieved chunks & flagging ungrounded claims
- [x] **M17 (Nov 29)**: Citation post-processor linking verified IDs to full source metadata (`source_file`, `page_number`, `section_title`, snippet) + tests
- [x] **M18 (Nov 30)**: End-to-end RAG query pipeline & CLI (`scripts/ask.py`) returning answer, verified citations, sources, and refusal flag

### Step 6 — Golden Dataset & Evaluation Suite (Dec 01 – Dec 05)
- [x] **M19 (Dec 01)**: Golden evaluation schema & validator (`src/rag_evals/eval/schema.py`) enforcing Q&A, passage, and `answerable` fields
- [x] **M20 (Dec 02)**: Initial 30 curated answerable Q&A pairs with exact source passages (`data/eval/golden_set.jsonl`)
- [x] **M21 (Dec 03)**: Expand golden set to 60+ Q&A pairs adding 12–15 unanswerable refusal test cases
- [x] **M22 (Dec 04)**: Retrieval metrics (`Hit@5`, `Recall@5`, `MRR`) & refusal accuracy evaluator (`src/rag_evals/eval/retrieval_metrics.py`) + tests
- [x] **M23 (Dec 05)**: Answer faithfulness, correctness, and citation-support evaluator + full eval runner (`scripts/run_eval.py`)

### Step 7 — Ablations & Failure Analysis (Dec 06 – Dec 08)
- [x] **M24 (Dec 06)**: Chunking ablation harness (`scripts/run_ablations.py`) testing chunk sizes (300 vs 450 vs 600 tokens) & overlap
- [x] **M25 (Dec 07)**: Retrieval/reranker ablations (BM25 vs Dense vs Hybrid RRF, Reranker Off vs On) & Markdown table generator (`eval/ablation_results.md`)
- [x] **M26 (Dec 08)**: Automated failure-case sampler & categorized error breakdown (`docs/failure_analysis.md`)

### Step 8 — Demo App, Polish & Final Write-Up (Dec 09 – Dec 13)
- [x] **M27 (Dec 09)**: Interactive Streamlit/Gradio demo app (`app.py`) with query box and retrieval configuration controls
- [x] **M28 (Dec 10)**: Clickable inline citations UI showing source file, page number, section title, and highlighted chunk text
- [x] **M29 (Dec 11)**: Evaluation & ablation results view in the demo app rendering metrics and comparison tables
- [x] **M30 (Dec 12)**: End-to-end integration tests, UI smoke tests, and lint/code-quality pass across `src/` and `tests/`
- [x] **M31 (Dec 13)**: Final flagship `README.md` with architecture diagram, setup instructions, ablation results table, and honest failure-cases section + full test pass
