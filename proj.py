import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI
import os
from dotenv import load_dotenv

# Загрузка API ключа
load_dotenv()
client = OpenAI(api_key=os.getenv("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"))

st.set_page_config(page_title="AI Lecture Notes", layout="wide")

st.title("📚 AI Конспект лекций")

# Загрузка файла
uploaded_file = st.file_uploader("Загрузи PDF лекции", type="pdf")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Ты помощник для студентов."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

if uploaded_file:
    with st.spinner("📖 Читаем PDF..."):
        lecture_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF загружен!")

    option = st.selectbox(
        "Что сделать?",
        ["Краткий конспект", "Карточки (flashcards)", "Тест"]
    )

    if st.button("Сгенерировать"):
        with st.spinner("🤖 Генерируем через GPT..."):

            if option == "Краткий конспект":
                prompt = f"""
Сделай краткий и понятный конспект для студента:

Текст:
{lecture_text}
"""
            elif option == "Карточки (flashcards)":
                prompt = f"""
Создай flashcards (вопрос-ответ):

Текст:
{lecture_text}
"""
            elif option == "Тест":
                prompt = f"""
Создай тест из 5 вопросов с вариантами ответов:

Текст:
{lecture_text}
"""

            result = ask_gpt(prompt)

        st.subheader("📄 Результат:")
        st.write(result)