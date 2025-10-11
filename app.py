import os
import pandas as pd
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Simple AI Data Analysis Agent")

uploaded_file = st.file_uploader("Upload your CSV data", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of your data:", df.head())
    question = st.text_input("Ask a question about your data")
    if st.button("Analyze") and question:
        prompt = (
            "You are an AI data analyst. Given this data:\n"
            + df.head(10).to_csv(index=False)
            + "\nPlease answer the following question:\n"
            + question
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content.strip()
        st.write("AI Analysis:")
        st.write(answer)
