# RAG System with Citations & Evals — 25-Day Build Roadmap (Nov 13 – Dec 13, 2026)

This repository implements an end-to-end **Retrieval-Augmented Generation (RAG)** system with **verifiable chunk-level citations**, **hybrid retrieval (Gemini embeddings + BM25 + cross-encoder reranking)**, **systematic evaluation**, **ablation studies**, and an **interactive UI**.

---

## Architecture Overview

1. **Corpus (50–200 pages)**: Real-world public PDF documents (e.g., university academic handbook / open technical policy manual) stored in `data/raw/`.
2. **Ingestion & Chunking**: PDF parsing with page numbers and section headers, cleaned and split into 300–600 token overlapping chunks with rich citation metadata.
3. **Hybrid Indexing**: Dense embeddings via `google-genai` (`gemini-embedding-001`) in FAISS/Chroma + sparse lexical index via `rank_bm25`.
4. **Retrieval & Reranking**: Top-K hybrid retrieval (Reciprocal Rank Fusion) with optional cross-encoder reranking.
5. **Grounded Generation & Verification**: `google-genai` (`gemini-3.8-flash`) constrained to retrieved chunks, inline `[chunk_id]` citations, explicit `"I don't know"` refusal on unanswerable queries, and programmatic citation ID verification.
6. **Evaluations**: 60+ golden Q&A pairs (including unanswerable negatives) measuring Retrieval (`Hit@5`, `Recall@5`, `MRR`), Faithfulness/Correctness, Citation Support, and Refusal Accuracy.
7. **Ablations & Error Analysis**: Controlled one-variable-at-a-time experiments recorded in a reproducible results table plus honest failure-case documentation.
8. **Demo UI**: Interactive Streamlit/Gradio app with clickable inline citations revealing source file, page number, section title, and exact passage.

---

## 25-Commit Milestone Checklist (1 Commit / Day)

### Step 1 — Corpus & Scaffolding
- [ ] **M01 (Day 01)**: Project scaffolding (`pyproject.toml`, `requirements.txt`, `src/rag_evals/`, `.env.example`, config loader, initial smoke tests)
- [ ] **M02 (Day 02)**: Public 50–200 page PDF corpus acquisition script (`scripts/fetch_corpus.py`) + page-count & metadata manifest (`data/corpus_manifest.json`)

### Step 2 — Ingestion & Chunking
- [ ] **M03 (Day 03)**: PDF loader & text cleaner (`src/rag_evals/ingest/pdf_loader.py`) preserving page numbers and section titles + unit tests
- [ ] **M04 (Day 04)**: Token-aware overlapping chunker (300–600 tokens) with citation metadata (`src/rag_evals/ingest/chunker.py`) + unit tests
- [ ] **M05 (Day 05)**: Ingestion CLI (`scripts/ingest.py`) producing `data/processed/chunks.jsonl` + chunk distribution summary

### Step 3 — Embeddings, Vector Store & BM25
- [ ] **M06 (Day 06)**: Gemini embedding client (`google-genai`, `gemini-embedding-001`) with batching, retries, and disk cache + mocked tests
- [ ] **M07 (Day 07)**: Persistent FAISS/Chroma vector store (`src/rag_evals/index/vector_store.py`) + build/query tests
- [ ] **M08 (Day 08)**: BM25 sparse keyword index (`src/rag_evals/index/bm25_index.py`) with serialization + unit tests

### Step 4 — Hybrid Retrieval & Reranking
- [ ] **M09 (Day 09)**: Hybrid retriever combining dense + BM25 via Reciprocal Rank Fusion (`src/rag_evals/retrieval/hybrid.py`) + unit tests
- [ ] **M10 (Day 10)**: Cross-encoder reranker module (`src/rag_evals/retrieval/reranker.py`) with configurable top-K/top-N & toggle + tests
- [ ] **M11 (Day 11)**: Unified retrieval CLI (`scripts/retrieve.py`) comparing Dense, BM25, Hybrid RRF, and Reranked results

### Step 5 — Generation with Verifiable Citations
- [ ] **M12 (Day 12)**: Citation-enforcing prompt template & Gemini (`gemini-3.8-flash`) generator (`src/rag_evals/generation/generator.py`) + mocked tests
- [ ] **M13 (Day 13)**: Programmatic citation verifier (`src/rag_evals/generation/verifier.py`) checking cited IDs against retrieved chunks & flagging ungrounded claims
- [ ] **M14 (Day 14)**: End-to-end RAG query pipeline & CLI (`scripts/ask.py`) returning answer, verified citations, sources, and refusal flag

### Step 6 — Golden Dataset & Evaluation Suite
- [ ] **M15 (Day 15)**: Golden evaluation schema & first 30 curated Q&A pairs with exact source passages (`data/eval/golden_set.jsonl`)
- [ ] **M16 (Day 16)**: Expand golden set to 60+ Q&A pairs including 12+ unanswerable refusal test cases + dataset validator script
- [ ] **M17 (Day 17)**: Retrieval metrics (`Hit@5`, `Recall@5`, `MRR`) & refusal accuracy evaluator (`src/rag_evals/eval/retrieval_metrics.py`) + tests
- [ ] **M18 (Day 18)**: Answer faithfulness, citation support judge & end-to-end eval runner (`scripts/run_eval.py`) + tests

### Step 7 — Ablations & Failure Analysis
- [ ] **M19 (Day 19)**: Ablation harness (`scripts/run_ablations.py`) testing chunk sizes (300 vs 450 vs 600 tokens) & overlap
- [ ] **M20 (Day 20)**: Retrieval/reranker ablations (BM25 vs Dense vs Hybrid RRF, Reranker Off vs On) & Markdown results table generator
- [ ] **M21 (Day 21)**: Failure-case analysis script & categorized error breakdown (`docs/failure_analysis.md`)

### Step 8 — Demo App & Final Write-Up
- [ ] **M22 (Day 22)**: Interactive Streamlit/Gradio demo app (`app.py`) with query box and retrieval configuration controls
- [ ] **M23 (Day 23)**: Clickable inline citations UI showing source file, page number, section title, and highlighted chunk text
- [ ] **M24 (Day 24)**: Evaluation & ablation results view in the demo app + UI smoke tests
- [ ] **M25 (Day 25)**: Complete `README.md` with architecture diagram, setup instructions, ablation results table, and honest failure-cases section + full test pass
