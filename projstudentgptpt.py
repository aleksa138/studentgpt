import streamlit as st
from pypdf import PdfReader
import pypdf
st.write("pypdf работает")
from openai import OpenAI
import os
from dotenv import load_dotenv

# 🔐 Загрузка API ключа
load_dotenv()
client = OpenAI(api_key=os.environ.get("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"))

# 🎨 Настройки страницы
st.set_page_config(page_title="AI Lecture Notes", layout="wide")

st.title("📚 AI Конспект лекций")

# 📥 Загрузка PDF
uploaded_file = st.file_uploader("Загрузи PDF лекции", type="pdf")

# 📄 Извлечение текста
def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        return f"Ошибка чтения PDF: {e}"

# 🤖 Запрос к GPT
def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Ты помощник для студентов."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка GPT: {e}"

# 🚀 Основная логика
if uploaded_file:
    with st.spinner("📖 Читаем PDF..."):
        lecture_text = extract_text_from_pdf(uploaded_file)

    if not lecture_text.strip():
        st.error("Не удалось извлечь текст из PDF 😢")
    else:
        st.success("PDF успешно загружен!")

        option = st.selectbox(
            "Что сделать?",
            ["Краткий конспект", "Карточки (flashcards)", "Тест"]
        )

        if st.button("Сгенерировать"):
            with st.spinner("🤖 Генерируем через GPT..."):

                if option == "Краткий конспект":
                    prompt = f"""
Сделай краткий и понятный конспект для студента:

{text_limit(lecture_text)}
"""
                elif option == "Карточки (flashcards)":
                    prompt = f"""
Создай flashcards (вопрос-ответ):

{text_limit(lecture_text)}
"""
                else:
                    prompt = f"""
Создай тест из 5 вопросов с вариантами ответов:

{text_limit(lecture_text)}
"""

                result = ask_gpt(prompt)

            st.subheader("📄 Результат:")
            st.write(result)

# ✂️ Ограничение длины (важно!)
def text_limit(text, max_chars=12000):
    return text[:max_chars]
