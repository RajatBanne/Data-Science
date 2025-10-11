import streamlit as st
import requests

st.title("AI Data Analysis Agent")
backend = "http://localhost:8000"

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    res = requests.post(
        backend + "/upload-csv/",
        files={"file": uploaded_file.getvalue()},
        headers={"accept": "application/json"}
    )
    file_key = uploaded_file.name
    st.session_state["file_key"] = file_key
    st.success("CSV uploaded!")

if "file_key" in st.session_state:
    question = st.text_input("Ask a question about your data")
    if st.button("Analyze"):
        resp = requests.post(
            backend + "/ask/",
            data={"file_key": st.session_state["file_key"], "question": question},
        )
        st.write("AI Answer:")
        st.write(resp.json().get("answer"))
