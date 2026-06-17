import streamlit as st
from pdf_reader import read_pdf
from rag import chunk_text, create_embeddings, search_chunks
from vector_store import create_vector_store
from llm import ask_llm

st.title("📄 Resume Chat (AI Assistant)")

# Initialize session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chunks" not in st.session_state:
    st.session_state.chunks = None
    st.session_state.index = None


# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])


# Process resume only once
if uploaded_file and st.session_state.chunks is None:

    text = read_pdf(uploaded_file)

    st.session_state.chunks = chunk_text(text)
    embeddings = create_embeddings(st.session_state.chunks)
    st.session_state.index = create_vector_store(embeddings)

    st.success("Resume loaded successfully!")


# Show chat history
for role, message in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)


# Input box
if uploaded_file:

    question = st.chat_input("Ask about your resume...")

    if question:

        # Save user message
        st.session_state.messages.append(("user", question))
        st.chat_message("user").write(question)

        # RAG retrieval
        retrieved = search_chunks(
            question,
            st.session_state.chunks,
            st.session_state.index
        )

        context = "\n".join(retrieved)

        # ChatGPT-style prompt
        prompt = f"""
You are a helpful AI career assistant.

Use ONLY the resume context below:

{context}

User Question:
{question}

If answer is not in resume, say "Not found in resume".

Answer:
"""

        answer = ask_llm(prompt)

        # Save assistant message
        st.session_state.messages.append(("assistant", answer))
        st.chat_message("assistant").write(answer)
