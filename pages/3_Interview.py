import streamlit as st
from llm import ask_llm
from pdf_reader import read_pdf

st.title("🧠 Interview Questions")

if st.button("Generate Questions"):

    resume = read_pdf("data/Dimple K B.pdf")

    prompt = f"""
Generate 10 interview questions from this resume:

{resume}
"""

    response = ask_llm(prompt)
    st.write(response)
