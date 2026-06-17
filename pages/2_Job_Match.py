import streamlit as st
from llm import ask_llm
from pdf_reader import read_pdf

st.title("📊 AI Career Matcher (ATS + Skill Gap)")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:

    resume_text = read_pdf(uploaded_file)

    prompt = f"""
You are an expert AI Career Agent.

Follow this process:

1. Read the resume carefully
2. Read the job description carefully
3. Extract required skills from job description
4. Extract skills from resume
5. Compare both
6. Find matching skills
7. Find missing skills
8. Give ATS score (0–100)
9. Give improvement suggestions

IMPORTANT:
Be strict and base everything only on given data.

Return in this format:

1. ATS Match Score (0–100)
2. Matched Skills
3. Missing Skills
4. Skill Gap Analysis
5. Improvement Suggestions
6. Final Verdict (Hire / Not Ready / Strong Match)

Resume:
{resume_text}

Job Description:
{job_desc}
"""

    result = ask_llm(prompt)

    st.subheader("📌 AI Analysis Result")
    st.write(result)
