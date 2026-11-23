# HyDE Retrieval Architecture

## Overview
Hypothetical Document Embeddings (HyDE) generate a hypothetical answer passage prior to vector similarity calculation.
This aligns the query representation closer to document manifold space than raw user questions.

## Workflow
1. User provides natural language query.
2. Generator synthesizes a speculative domain-aligned answer.
3. Expanded query concatenated: `q_expanded = f"{query} {hypothetical_answer}"`.
4. Embedded representation sent to VectorStore and BM25 hybrid fusion.
