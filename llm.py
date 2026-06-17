import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

cache = {}


def ask_llm(prompt):

    clean_prompt = prompt.strip()

    if clean_prompt in cache:
        return cache[clean_prompt]

    response = model.generate_content(clean_prompt)
    result = response.text

    cache[clean_prompt] = result

    return result
