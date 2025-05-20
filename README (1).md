## 📄 CV Reviewer & ✉️ Cover Letter Generator

An AI-powered web app built with **Streamlit** that analyzes uploaded CVs and helps you generate **professional cover letters** tailored to specific job roles. This tool is perfect for job seekers who want quick, smart feedback and personalized application materials.

## 🚀 Features

- ✅ Upload your CV in `.pdf` or `.docx` format  
- 🧠 Get intelligent insights on CV structure and missing sections  
- 🎯 Role-specific enhancement suggestions using NLP  
- ✍️ Automatically generate a personalized cover letter based on your CV and target job  
- 📥 Download your cover letter as a clean PDF  
- 🔐 Uses **API keys** for OpenAI or Hugging Face model access  
- 🔗 Integrated with **LangChain** for flexible LLM workflows

## 🛠️ Technologies Used

- `Streamlit` for the interactive web interface  
- `spaCy` for natural language processing  
- `Hugging Face Transformers` (e.g. GPT-2) for text generation  
- `LangChain` for chaining LLM components  
- `PyMuPDF` & `docx2txt` for CV text extraction  
- `ReportLab` for PDF cover letter creation  
- `OpenAI API` (optional) for enhanced generation capabilities

##💡 How to Run Locally

1. Clone the repository  
2. Set your OpenAI API key or Hugging Face token as environment variables:

```bash
export OPENAI_API_KEY=your-key
export HUGGINGFACEHUB_API_TOKEN=your-token
````

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

## 📌 Notes

* The app currently defaults to GPT-2 via Hugging Face. You can switch to other models (e.g., LLaMA, Flan-T5) by updating the pipeline.
* LangChain integration allows swapping models or workflows easily.
* CV insights are basic and can be expanded with more structured resume parsing logic.

---

Built by **Githmi Punchihewa**
BSc in Applied Data Science and Communication | KDU

