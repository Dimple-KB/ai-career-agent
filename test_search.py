from pdf_reader import read_pdf
from rag import chunk_text, create_embeddings, search_chunks
from vector_store import create_vector_store

text = read_pdf("data/Dimple K B.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = create_vector_store(embeddings)

question = "What internship experience does Dimple have?"

results = search_chunks(question, chunks, index)

print("\nRelevant Chunks:\n")

for chunk in results:
    print(chunk)
    print("\n---------------------\n")
