from tools import rag_tool, cover_letter_tool, skill_analyzer_tool


def agent_router(question, chunks, index):
    q = question.lower()

    # TOOL SELECTION LOGIC (agent brain)

    if "cover letter" in q:
        return cover_letter_tool(question)

    elif "skills" in q or "analyze" in q:
        return skill_analyzer_tool(question)

    else:
        return rag_tool(question, chunks, index)
