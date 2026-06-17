from rag import search_chunks
from llm import ask_llm


def rag_tool(question, chunks, index):
    results = search_chunks(question, chunks, index)
    context = "\n".join(results)

    prompt = f"""
Use only this context:
{context}

Question: {question}
If not found say "Not available in resume."
Answer:
"""
    return ask_llm(prompt)


def cover_letter_tool(skills):
    prompt = f"""
Write a professional cover letter based on these skills:
{skills}
"""
    return ask_llm(prompt)


def skill_analyzer_tool(text):
    prompt = f"""
Extract technical and soft skills from:
{text}
"""
    return ask_llm(prompt)
