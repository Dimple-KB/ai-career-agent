import streamlit as st
from auth import login, signup
from pdf_reader import read_pdf
from database import save_resume, save_result
from tools import resume_tool

st.title("🧠 AI Career Agent SaaS")

menu = st.sidebar.selectbox("Menu", ["Login", "Signup"])

# ---------------- LOGIN ----------------
if menu == "Signup":
    u = st.text_input("Username")
    p = st.text_input("Password")

    if st.button("Create Account"):
        signup(u, p)
        st.success("Account created")


elif menu == "Login":

    u = st.text_input("Username")
    p = st.text_input("Password")

    if st.button("Login"):

        user = login(u, p)

        if user:
            st.session_state.user = user[0]
            st.success("Login successful")
        else:
            st.error("Invalid login")


# ---------------- MAIN APP ----------------
if "user" in st.session_state:

    uploaded_file = st.file_uploader("Upload Resume")
    question = st.text_input("Ask Question")
    job_desc = st.text_area("Paste Job Description")

    if uploaded_file:

        resume_text = read_pdf(uploaded_file)

        save_resume(st.session_state.user, resume_text)

        st.success("Resume saved")

    if question:

        result = resume_tool(uploaded_file, question)

        st.subheader("AI Response")
        st.write(result)

        # OPTIONAL: STORE RESULT (SIMPLE VERSION)
        save_result(
            st.session_state.user,
            "N/A",
            "N/A",
            "N/A",
            result
        )
