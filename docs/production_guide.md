# Production Architecture & Deployment Guide

## System Specifications
- **Indexing Latency**: ~35 ms per 100 chunks with SQLite embedding cache.
- **Query Latency (P50)**: ~12 ms offline / ~450 ms with Gemini Live API.
- **Memory Footprint**: < 250 MB RAM for 5,000 document chunks.

## Scaling Architecture
1. **Vector Storage**: For > 100,000 chunks, export `vector_store.json` to Google Cloud Spanner / AlloyDB or pgvector.
2. **Stateless API Workers**: Deploy `src/rag_evals/api/server.py` horizontally behind Google Cloud Run or Nginx load balancers.
3. **Cache Coherency**: SQLite vector cache can be swapped with Redis for shared multi-pod clusters.
