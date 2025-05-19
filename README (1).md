# 📄 CV Reviewer & ✉️ Cover Letter Generator

An AI-powered web app built with **Streamlit** that analyzes uploaded CVs and helps you generate **professional cover letters** tailored to specific job roles. This tool is perfect for job seekers who want quick, smart feedback and personalized application materials.

## 🚀 Features

- ✅ Upload your CV in `.pdf` or `.docx` format  
- 🧠 Get intelligent insights on CV structure and missing sections  
- 🎯 Role-specific enhancement suggestions using NLP  
- ✍️ Automatically generate a personalized cover letter based on your CV and target job  
- 📥 Download your cover letter as a clean PDF  

## 🛠️ Technologies Used

- `Streamlit` for the web interface  
- `spaCy` for natural language processing  
- `Transformers (GPT-2)` from Hugging Face for text generation  
- `PyMuPDF` & `docx2txt` for CV text extraction  
- `ReportLab` for PDF cover letter creation  

## 💡 How to Run Locally

1. Clone the repository  
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

## 📌 Notes

- The app currently uses `GPT-2` for text generation. You can swap this with any Hugging Face-supported model.
- CV enhancement tips are basic but can be extended with domain-specific logic.

---

Built by **Githmi Punchihewa**  
BSc in Applied Data Science and Communication | KDU