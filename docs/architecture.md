# RAG System Architecture & Design Specification

## System Overview

```mermaid
flowchart TD
    UserQuery["User Query"] --> Retriever["Hybrid Retriever"]
    subgraph Ingestion ["Ingestion & Indexing"]
        PDF["University Policy Handbook"] --> Chunker["Token-Aware Chunker (450t, 50t overlap)"]
        Chunker --> BM25["BM25 Lexical Index"]
        Chunker --> Cache["SQLite Vector Cache"]
        Cache --> DenseStore["Dense Vector Store (gemini-embedding-001)"]
    end
    Retriever --> BM25
    Retriever --> DenseStore
    BM25 --> RRF["Reciprocal Rank Fusion (RRF k=60)"]
    DenseStore --> RRF
    RRF --> Reranker["Cross-Encoder Reranker (Top-N=5)"]
    Reranker --> Generator["Grounded Generator (gemini-3.8-flash)"]
    Generator --> Verifier["Programmatic Citation Verifier"]
    Verifier --> FinalResponse["Verified Answer with Clickable Citations"]
```

## Key Architectural Principles

1. **Strict Context Grounding**: The LLM system instruction enforces that answers must be derived solely from retrieved text, with an explicit string refusal if context is insufficient.
2. **Deterministic Citation Verification**: Regular expressions extract every `[chunk_id]` tag and verify against the retrieved chunk set, flagging ungrounded claims or hallucinated references.
3. **Hybrid RRF Fusion**: Combines exact lexical term matches (BM25) with semantic embeddings using `RRF = sum(1 / (k + rank))` with constant `k=60`.
4. **Persistent SQLite Caching**: Eliminates duplicate embedding calls to Google GenAI, enabling lightning-fast local re-indexing.
