from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text):
    return text.split("\n")


def create_embeddings(chunks):
    return model.encode(chunks)


def search_chunks(question, chunks, index, k=2):
    question_embedding = model.encode([question])
    distances, indices = index.search(question_embedding, k)

    return [chunks[i] for i in indices[0]]
