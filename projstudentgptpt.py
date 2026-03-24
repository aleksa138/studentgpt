import streamlit as st
import pdfplumber
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("sk-xxxx"))

st.title("📚 AI Конспект лекций")

uploaded_file = st.file_uploader("Загрузи PDF лекции", type="pdf")

def extract_text_from_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        return f"Ошибка чтения PDF: {e}"

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Ты помощник для студентов."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if uploaded_file:
    with st.spinner("📖 Читаем PDF..."):
        lecture_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF загружен!")

    if st.button("Сделать конспект"):
        result = ask_gpt(f"Сделай краткий конспект:\n{lecture_text[:12000]}")
        st.write(result)
