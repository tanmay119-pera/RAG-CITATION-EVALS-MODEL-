# RAG HTTP API Reference

## Endpoints

### `POST /v1/query`
Executes an end-to-end RAG question answering pipeline with verifiable citation IDs.

#### Request Body
```json
{
  "query": "What is the penalty for a first-time plagiarism violation?",
  "top_k": 5,
  "retrieval_mode": "hybrid",
  "use_reranker": true
}
```

#### Response Body
```json
{
  "query": "What is the penalty for a first-time plagiarism violation?",
  "answer": "According to university policy, minor first-time violations receive a zero grade [handbook_p1_c1].",
  "is_refusal": false,
  "citations": [
    {
      "chunk_id": "handbook_p1_c1",
      "section_title": "SECTION 1: ACADEMIC INTEGRITY",
      "file_name": "university_regulations_handbook.txt",
      "page_number": 1,
      "text_snippet": "Clause 1.2 - Penalties for First-Time Violations: When an instructor suspects..."
    }
  ],
  "latency_ms": 14.5
}
```
