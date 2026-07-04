import streamlit as st

st.title("📧 Email Support Agent")

user_input = st.text_area("Enter customer query:")

if st.button("Generate Reply"):
    if user_input:
        # your logic here
        response = "This is an automated reply"
        st.success(response)