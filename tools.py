import streamlit as st
from pdf_reader import read_pdf
from rag import chunk_text, create_embeddings, search_chunks
from vector_store import create_vector_store
from llm import ask_llm


def resume_tool(uploaded_file, question):

    if "rag_ready" not in st.session_state:

        text = read_pdf(uploaded_file)

        chunks = chunk_text(text)
        embeddings = create_embeddings(chunks)
        index = create_vector_store(embeddings)

        st.session_state.chunks = chunks
        st.session_state.index = index
        st.session_state.rag_ready = True

    chunks = st.session_state.chunks
    index = st.session_state.index

    results = search_chunks(question, chunks, index)
    context = "\n".join(results)

    prompt = f"""
Answer ONLY using this resume context:

{context}

Question: {question}
"""

    return ask_llm(prompt)
