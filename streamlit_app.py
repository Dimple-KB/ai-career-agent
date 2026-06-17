import streamlit as st

from pdf_reader import read_pdf
from rag import chunk_text, create_embeddings, search_chunks
from vector_store import create_vector_store
from llm import ask_llm


# ----------------------------
# CACHE RAG PIPELINE
# ----------------------------
@st.cache_resource
def load_rag():
    text = read_pdf("data/Dimple K B.pdf")
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)
    index = create_vector_store(embeddings)
    return chunks, index


chunks, index = load_rag()


# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="AI Career Agent", layout="wide")


# ----------------------------
# SIDEBAR NAVIGATION
# ----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Login", "Signup", "AI Assistant"])


# ----------------------------
# HOME PAGE
# ----------------------------
if page == "Home":
    st.title("🏠 Home")
    st.write("Welcome to AI Career Agent 🚀")
    st.write("Use the sidebar to navigate through the app.")


# ----------------------------
# LOGIN PAGE (UI ONLY)
# ----------------------------
elif page == "Login":
    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Login functionality not connected yet (demo UI).")


# ----------------------------
# SIGNUP PAGE (UI ONLY)
# ----------------------------
elif page == "Signup":
    st.title("📝 Signup")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        st.success("Signup functionality not connected yet (demo UI).")


# ----------------------------
# AI ASSISTANT (RAG APP)
# ----------------------------
elif page == "AI Assistant":
    st.title("📄 AI Resume RAG Assistant")

    question = st.text_input("Ask about the resume")

    if question:
        with st.spinner("Thinking..."):
            retrieved_chunks = search_chunks(question, chunks, index)
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
