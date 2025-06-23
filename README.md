
# AI Careers Advisor (UK)

An AI-powered careers advisor designed specifically for UK job seekers. This web-based tool supports CV feedback, tailored CV rewriting, job requirement extraction, and interview preparation — all using local AI models (LLaMA 3 via Ollama) for complete offline functionality.

## 🔧 Features

- ✅ Extract key job requirements from job adverts (PDF/DOCX)
- ✅ Upload your CV for feedback and rewriting to UK standards
- ✅ Tailor your CV to a specific job (with or without rewriting)
- ✅ Generate interview questions based on job requirements
- ✅ Generate tailored answers based on your CV
- ✅ Offline, local AI via Ollama (LLaMA 3)
- ✅ Simple web interface (Flask + HTML)

---

## 📸 Screenshots

### 🏠 Main Page
![Main Page](docs/Main%20Page.jpg)

---

### 📄 Tailored CV Result Example
![Tailored CV Results Page](docs/Tailored%20CV%20Results%20Page.jpg)

---

### ❓ Likely Interview Questions Output
![Likely Interview Questions Results Page](docs/Likely%20Interview%20Questions%20Results%20Page.jpg)

---

## 🗂️ Project Structure

```
careers-advisor/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── results.html
├── uploads/
│   ├── cvs/
│   └── jobadverts/
├── utils/
│   ├── extract_text.py
│   ├── cv_feedback.py
│   ├── tailor_cv.py
│   ├── interview_questions.py
│   └── generate_answers.py
├── docs/
│   ├── Main Page.jpg
│   ├── Tailored CV Results Page.jpg
│   └── Likely Interview Questions Results Page.jpg
└── README.md
```

---

## 📦 Requirements

```text
flask
python-docx
pypdf
langchain
langchain-community
langchain-ollama
sentence-transformers
faiss-cpu
unstructured[local-inference]
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/ruvel-ai-dev/ai-careers-advisor.git
cd ai-careers-advisor

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Optional: enable debug output
export FLASK_DEBUG=True

# Run the app (defaults to non-debug mode)
python3 app.py
```

Then visit: `http://127.0.0.1:5000` in your browser.

---

## 🧠 Powered By

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [LLaMA 3](https://llama.meta.com/)
- [FAISS](https://github.com/facebookresearch/faiss)

---

## 📬 Contact

**Ruvel Miah**  
Email: [ruvel.ai.dev@gmail.com](mailto:ruvel.ai.dev@gmail.com)  
GitHub: [ruvel-ai-dev](https://github.com/ruvel-ai-dev)
