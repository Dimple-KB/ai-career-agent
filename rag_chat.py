from pdf_reader import read_pdf
from rag import chunk_text, create_embeddings, search_chunks
from vector_store import create_vector_store
from llm import ask_llm

# Load Resume
text = read_pdf("data/Dimple K B.pdf")

# Chunk
chunks = chunk_text(text)

# Create Embeddings
embeddings = create_embeddings(chunks)

# Build FAISS Index
index = create_vector_store(embeddings)

print("Resume RAG Assistant Started!")
print("Type exit to quit")

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    retrieved_chunks = search_chunks(
        question,
        chunks,
        index
    )

    context = "\n".join(retrieved_chunks)

    prompt = f"""
Use ONLY the information below.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_llm(prompt)

    print("\nAgent:", answer)
