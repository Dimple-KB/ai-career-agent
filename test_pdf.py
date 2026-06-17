from pdf_reader import read_pdf
from rag import chunk_text, create_embeddings

text = read_pdf("data/Dimple K B.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print("Chunks:", len(chunks))

print("Embedding Shape:")

print(embeddings.shape)
