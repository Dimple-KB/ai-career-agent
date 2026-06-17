import streamlit as st

st.set_page_config(page_title="AI Career Agent")

page = st.sidebar.radio("Navigate", ["Home", "Login", "Signup"])

if page == "Home":
    st.title("Home Page")

elif page == "Login":
    st.title("Login Page")
    st.text_input("Email")
    st.text_input("Password", type="password")
    st.button("Login")

elif page == "Signup":
    st.title("Signup Page")
    st.text_input("Email")
    st.text_input("Password", type="password")
    st.button("Create Account")
