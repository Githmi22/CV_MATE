import streamlit as st
import docx2txt
import fitz  # PyMuPDF
import tempfile
import os
import re
import spacy
from reportlab.pdfgen import canvas
from transformers import pipeline
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import openai

# ---- SETUP ----
st.set_page_config(page_title="CV Reviewer & Cover Letter Generator", layout="centered")
st.title("📄 CV Reviewer & ✉️ Cover Letter Generator")

spacy.load("en_core_web_sm")
openai.api_key = st.secrets["AIzaSyBmc5eTQeNFoYbtlAtQr4owXN4xAOW8MZQ"]

# Hugging Face text generator (GPT-2)
cover_letter_generator = pipeline("text-generation", model="gpt2")

# LangChain LLM for job-role enhancements
llm = ChatOpenAI(temperature=0.7)

enhancement_prompt = PromptTemplate(
    input_variables=["role", "cv_text"],
    template="""
You are a CV expert. The user is applying for the position of {role}.
Given the following CV content:

{cv_text}

Suggest missing sections or enhancements the user should include to improve their CV for the {role} role.
"""
)

# ---- FUNCTIONS ----
def extract_text(uploaded_file):
    suffix = os.path.splitext(uploaded_file.name)[1].lower()
    temp_dir = tempfile.mkdtemp()
    tmp_path = os.path.join(temp_dir, uploaded_file.name)

    with open(tmp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.write(f"Temporary file saved at: {tmp_path}")

    if suffix == '.pdf':
        text = ""
        with fitz.open(tmp_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif suffix == '.docx':
        return docx2txt.process(tmp_path)
    else:
        return ""

def generate_insights(text):
    insights = []
    if not re.search(r"(Experience|Work History)", text, re.IGNORECASE):
        insights.append("🟡 Consider adding a 'Work Experience' section.")
    if not re.search(r"(Education|Qualifications)", text, re.IGNORECASE):
        insights.append("🟡 Include an 'Education' section to highlight academic background.")
    if not re.search(r"(Skills|Technical Skills)", text, re.IGNORECASE):
        insights.append("🟡 List your relevant skills in a dedicated 'Skills' section.")
    if len(text.split()) < 150:
        insights.append("🔴 Your CV is very short. Aim for at least 1 page of content.")
    if len(text.split()) > 1000:
        insights.append("🔴 CV is too long. Try to keep it concise and under 2 pages.")
    if not re.search(r"[\w\.-]+@[\w\.-]+", text):
        insights.append("🟡 Make sure your email contact is included.")
    if not insights:
        insights.append("✅ Your CV contains all standard sections. Just make sure it's visually appealing!")
    return "\n".join(insights)

def role_based_enhancements(cv_text, role):
    prompt = enhancement_prompt.format(role=role, cv_text=cv_text[:1000])
    response = llm.predict(prompt)
    return response

def generate_cover_letter(cv_text, company, role):
    prompt = f"Write a professional, tailored cover letter for a job application to {company} for the role of {role}. Use key details from the following CV:\n\n{cv_text[:1000]}"
    result = cover_letter_generator(prompt, max_length=400, num_return_sequences=1)
    return result[0]['generated_text']

def generate_pdf(text, filename="cover_letter.pdf"):
    temp_pdf_path = os.path.join(tempfile.gettempdir(), filename)
    c = canvas.Canvas(temp_pdf_path)
    lines = text.split('\n')
    y = 800
    for line in lines:
        c.drawString(50, y, line)
        y -= 15
    c.save()
    return temp_pdf_path

# ---- STREAMLIT UI ----
uploaded_cv = st.file_uploader("Upload your CV (.pdf or .docx)", type=["pdf", "docx"])

if uploaded_cv:
    text = extract_text(uploaded_cv)
    st.subheader("✅ Extracted CV Text")
    st.text_area("CV Raw Text", text, height=200)

    st.subheader("📋 Automated CV Review")
    feedback = generate_insights(text)
    st.success(feedback)

    st.subheader("🧠 Role-Specific CV Enhancement Suggestions")
    job_role = st.text_input("Enter your target Job Role for feedback")
    if job_role:
        enhancement = role_based_enhancements(text, job_role)
        st.info(enhancement)

    st.subheader("✉️ Generate Cover Letter")
    company = st.text_input("Company Name")
    if company and job_role:
        if st.button("Generate Cover Letter"):
            with st.spinner("Generating cover letter..."):
                letter = generate_cover_letter(text, company, job_role)
                st.text_area("Generated Cover Letter", letter, height=300)

                pdf_path = generate_pdf(letter)
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Cover Letter as PDF",
                        data=f,
                        file_name="cover_letter.pdf",
                        mime="application/pdf"
                    )

st.markdown("---")
st.caption("Built by Githmi Punchihewa | BSc in Applied Data Science Communication | KDU")
