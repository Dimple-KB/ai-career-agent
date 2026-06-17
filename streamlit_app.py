import streamlit as st

from pdf_reader import read_pdf
from rag import chunk_text, create_embeddings, search_chunks
from vector_store import create_vector_store
from llm import ask_llm


@st.cache_resource
def load_rag():

    text = read_pdf("data/Dimple K B.pdf")

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    index = create_vector_store(embeddings)

    return chunks, index


chunks, index = load_rag()

st.title("AI Resume RAG Assistant")

question = st.text_input("Ask about the resume")

if question:

    retrieved_chunks = search_chunks(
        question,
        chunks,
        index
    )

    context = "\n".join(retrieved_chunks)

    prompt = f"""
Use ONLY the information provided below.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
'I could not find that information in the resume.'

Answer:
"""

    answer = ask_llm(prompt)

    st.write(answer)
