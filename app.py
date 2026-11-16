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

config = load_config()
retriever = HybridRetriever(config)
reranker = CrossEncoderReranker()
generator = GroundedGenerator(config)

col1, col2 = st.columns([2, 1])
with col2:
    retrieval_mode = st.selectbox("Mode", ["hybrid", "dense", "bm25"], index=0)
    top_k = st.slider("Top K", 1, 10, 5)

with col1:
    user_query = st.text_input("Question:", placeholder="e.g. What is the deadline to appeal an ethics decision?")
    submit = st.button("Search & Answer", type="primary")

if submit and user_query:
    raw = retriever.retrieve(user_query, top_k=top_k, mode=retrieval_mode)
    final = reranker.rerank(user_query, raw)
    answer, is_refusal = generator.generate(user_query, final)
    v_res = CitationVerifier.verify(answer, {c.chunk_id for c in final})

    st.markdown("### Answer")
    st.markdown(answer)
    st.markdown("---")
    st.subheader("📑 Verified Source Citations")
    for cid in v_res.valid_ids:
        matching = next((c for c in final if c.chunk_id == cid), None)
        if matching:
            with st.expander(f"📍 Citation [{cid}] — {matching.metadata.get('section_title', '')}"):
                st.write(f"**Document**: `{matching.metadata.get('file_name', '')}` (Page {matching.metadata.get('page_number', 1)})")
                st.markdown(f"> {matching.text}")
