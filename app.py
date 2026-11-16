"""Interactive Streamlit Demo for RAG with Citations and Evals."""

import streamlit as st
import json
from pathlib import Path
from rag_evals.config import load_config
from rag_evals.retrieval.hybrid import HybridRetriever
from rag_evals.retrieval.reranker import CrossEncoderReranker
from rag_evals.generation.generator import GroundedGenerator
from rag_evals.generation.verifier import CitationVerifier

st.set_page_config(page_title="RAG Citation & Evals System", page_icon="📚", layout="wide")
st.title("📚 RAG Academic Assistant with Verifiable Citations")
st.markdown("Search university academic regulations with citation verification and refusal guarantees.")

config = load_config()
retriever = HybridRetriever(config)
reranker = CrossEncoderReranker()
generator = GroundedGenerator(config)

user_query = st.text_input("Enter your policy question:", placeholder="e.g. What is the penalty for a first-time plagiarism violation?")
if st.button("Submit Question", type="primary") and user_query:
    raw_chunks = retriever.retrieve(user_query, top_k=5, mode="hybrid")
    final_chunks = reranker.rerank(user_query, raw_chunks)
    answer, is_refusal = generator.generate(user_query, final_chunks)
    st.markdown("### Answer")
    st.markdown(answer)
