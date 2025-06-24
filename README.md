# AI Careers Advisor (UK)

An AI-powered careers advisor built for UK job seekers. This web-based tool runs fully offline using LLaMA 3 via Ollama, helping users prepare high-quality CVs and job applications with no internet or cloud dependencies.

## 🔧 Features

- ✅ Extract key job requirements from job adverts (PDF/DOCX)
- ✅ Upload your CV for feedback and rewriting to UK standards
- ✅ Tailor your CV to a specific job advert (with or without rewriting)
- ✅ Generate likely interview questions based on the job
- ✅ Generate tailored interview answers using your CV
- ✅ Clean, professional .docx exports (no asterisks, well-formatted)
- ✅ Copy-to-clipboard functionality for all results
- ✅ Fully offline (local AI via Ollama + LLaMA 3)
- ✅ Clean Flask-based web interface

---

## 🧾 Project Summary

This AI Careers Advisor supports five practical use cases through a clean offline web interface:

1. **Extract job advert requirements** (PDF or Word)
2. **Upload a CV** to:
   - a) get detailed feedback, or  
   - b) rewrite it to UK standards using a clean `.docx` export
3. **Upload CV + job advert** to:
   - a) receive specific advice on how to tailor the CV, or  
   - b) generate a rewritten version tailored to the job advert (with clear `[EXAMPLE]` markers)
4. **Upload a job advert** to generate likely interview questions (20 in total)
5. **Upload CV + job advert** to generate tailored answer suggestions using actual CV content

The entire system runs locally on your machine using Ollama and LLaMA 3. No internet, APIs, or external tools are required — making it fully private, secure, and fast.

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
This section outlines the structured development roadmap for the AI Careers Advisor platform. It helps track feature completion, prioritise future work, and present progress for stakeholders or collaborators.

## ✅ Phase 1: Local AI Assistant Foundation (Completed)

| Step | Description                                                                                  | Status   |
|------|----------------------------------------------------------------------------------------------|----------|
| 1.   | Set up project folder with `app.py`, `index.html`, utils, etc.                              | ✅ Done  |
| 2.   | Integrated LLaMA 3 via Ollama locally using `langchain_ollama`                               | ✅ Done  |
| 3.   | Created routes for all 6 user tasks (feedback, rewrite, tailor, extract, interview, answer) | ✅ Done  |
| 4.   | Parsed job/CV PDFs and extracted text using `extract_text_from_file`                        | ✅ Done  |
| 5.   | Used LangChain + prompt templates to generate results                                        | ✅ Done  |
| 6.   | Displayed output cleanly on `results.html`                                                   | ✅ Done  |

---

## ✅ Phase 2: UX & Output Upgrades (Completed)

| Step | Description                                                                                           | Status   |
|------|-------------------------------------------------------------------------------------------------------|----------|
| 7.   | Exported improved and tailored CVs as **`.docx`** files                                               | ✅ Done  |
| 8.   | Cleaned LLM output to remove ugly `*` bullet formatting                                               | ✅ Done  |
| 9.   | Added **copy-to-clipboard** button for readable AI results                                            | ✅ Done  |
| 10.  | Prevented copy box from appearing on `download-only` pages                                            | ✅ Done  |
| 11.  | Cleaned up HTML and preserved original visual layout                                                  | ✅ Done  |

---

## 🟡 Phase 3: Optional Visual & Styling Enhancements (Paused)

| Step | Description                                                                 | Status        |
|------|-----------------------------------------------------------------------------|---------------|
| 12.  | Add Google Fonts (Roboto), improve overall UI look and spacing             | 🟡 Reverted   |
| 13.  | Improve layout for professional aesthetic (legibility, spacing, branding)  | 🟡 Reverted   |
| 14.  | Add favicon, footer, or logo if desired                                    | 🔜 Optional   |

---

## 🔜 Phase 4: Advanced Features (Planned)

| Step | Description                                                                                      | Status |
|------|--------------------------------------------------------------------------------------------------|--------|
| 15.  | Add session memory so users can revisit or re-download past results                              | 🔜     |
| 16.  | Offer multiple rewrite styles (academic, creative, etc.)                                         | 🔜     |
| 17.  | Add optional editing interface for users to adjust CV content before download                    | 🔜     |
| 18.  | Enable comparison view: original vs tailored/improved CV side-by-side                            | 🔜     |
| 19.  | Implement job ad scraping or LinkedIn import for real examples                                   | 🔜     |

---

## 🔜 Phase 5: Deployment (Azure VM / Web Hosting)

| Step | Description                                                                              | Status |
|------|------------------------------------------------------------------------------------------|--------|
| 20.  | Finalise `requirements.txt` and production-ready `app.py`                               | 🔜     |
| 21.  | Set up WSGI (Gunicorn or similar) + Flask production server                              | 🔜     |
| 22.  | Deploy to Azure VM or alternative host for web access                                    | 🔜     |
| 23.  | Secure upload/download (e.g. file type checks, size limits)                              | 🔜     |
| 24.  | Add optional login or session management (e.g. user email or login token, if needed)     | 🔜     |

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

Install dependencies:
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

# Run the app
python3 app.py
```

Then go to: `http://127.0.0.1:5000` in your browser.

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

