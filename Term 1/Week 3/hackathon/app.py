import streamlit as st
import re
import time
from google import genai
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from docx import Document

load_dotenv()

st.set_page_config(page_title="Anonymous CV Screening", page_icon="🕶️")

try:
    api_key = os.environ["GEMINI_API_KEY"]
except KeyError:
    st.error("No GEMINI_API_KEY found. Set it in your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

def read_document(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join(p.text for p in doc.paragraphs)
    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file type. Use .pdf, .docx or .txt")
        return None

def strip_contact_details(text):
    text = re.sub(r'\S+@\S+\.\S+', '[EMAIL REMOVED]', text)
    text = re.sub(r'(\+31|0)[\s-]?6[\s-]?\d{4}[\s-]?\d{4}', '[PHONE REMOVED]', text)
    text = re.sub(r'(\+31|0)[\s-]?\d{2,3}[\s-]?\d{6,7}', '[PHONE REMOVED]', text)
    text = re.sub(r'\b\d{4}\s?[A-Z]{2}\b', '[POSTAL CODE REMOVED]', text)
    return text

def anonymize_cv(cv_text, max_attempts=3):
    cleaned_text = strip_contact_details(cv_text)

    prompt = f"""Find the full name of the candidate in this CV.
Reply with ONLY the exact name as it appears in the text, or reply "NONE" if you cannot find a clear name.

CV:
{cleaned_text}"""

    for attempt in range(1, max_attempts + 1):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt,
            )
            detected_name = response.text.strip()
            if detected_name.upper() == "NONE" or detected_name not in cleaned_text:
                return cleaned_text, None
            anonymized = cleaned_text.replace(detected_name, "[CANDIDATE]")
            return anonymized, detected_name
        except Exception:
            if attempt < max_attempts:
                time.sleep(5)
            else:
                return cleaned_text, None

def evaluate_cv(anonymized_cv, vacancy_text, max_attempts=3):
    prompt = f"""You are a recruiter. Evaluate the CV below for this job vacancy, based only on qualifications, skills, and experience.

VACANCY:
{vacancy_text}

CV:
{anonymized_cv}

Give a score from 1-10 and a short, specific motivation focused only on job-relevant qualifications.

Answer in this exact format:
SCORE: <number>
MOTIVATION: <text>"""

    for attempt in range(1, max_attempts + 1):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt,
            )
            return response.text
        except Exception:
            if attempt < max_attempts:
                time.sleep(5)
            else:
                return None

# --- UI ---
st.title("🕶️ Anonymous CV Screening")
st.write(
    "Upload or paste a CV. It will first be anonymized (name, email, phone, and "
    "postal code removed) before being evaluated against a job vacancy — reducing "
    "the risk of bias based on a candidate's identity."
)

st.subheader("1. Provide the CV")
input_method = st.radio("How do you want to provide the CV?", ["Paste text", "Upload document"])

cv_text = ""
if input_method == "Paste text":
    cv_text = st.text_area("CV", height=200, placeholder="Paste the full CV here, including the candidate's name...")
else:
    uploaded_file = st.file_uploader("Upload CV", type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        extracted_text = read_document(uploaded_file)
        if extracted_text is not None:
            if len(extracted_text.strip()) < 20:
                st.warning("Very little text could be extracted. This might be a scanned document. Try pasting the text manually instead.")
            cv_text = extracted_text

st.subheader("2. Provide the vacancy")
vacancy_text = st.text_area("Vacancy text", height=150, placeholder="Paste the job vacancy here...")

if st.button("Anonymize and evaluate CV", type="primary"):
    if not cv_text.strip() or not vacancy_text.strip():
        st.error("Please provide both the CV and the vacancy text.")
    else:
        with st.spinner("Anonymizing CV..."):
            anonymized_cv, found_name = anonymize_cv(cv_text)

        st.subheader("🕶️ Anonymized CV")
        if found_name:
            st.info(f"Removed candidate name (\"{found_name}\"), email, phone number, and postal code before evaluation.")
        else:
            st.warning("Could not confidently detect a name to remove. Email, phone, and postal code were still removed. Please check the anonymized CV below before proceeding.")
        st.text_area("Review the anonymized CV", value=anonymized_cv, height=200, key="anon_preview")

        with st.spinner("Evaluating anonymized CV..."):
            result = evaluate_cv(anonymized_cv, vacancy_text)

        st.subheader("📋 Evaluation")
        if result is None:
            st.error("The AI did not return a result after several attempts. Please try again.")
        else:
            st.write(result)
            st.caption("This evaluation is based only on the anonymized CV. Always have a human review the final decision.")