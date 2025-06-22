
# AI Careers Advisor (UK)

A web-based AI assistant to support UK-based job seekers throughout the job application process, including CV improvement, tailoring, job advert analysis, and interview preparation.

## 🎯 Features

This AI-powered platform offers:

1. **Extract key requirements from job adverts**
2. **Upload a CV** to either:
   - Get feedback and advice on improvement (UK standards)
   - Rewrite it to UK industry norms (clearly marking example/template content)
3. **Upload both CV and job advert** to:
   - Receive advice on tailoring
   - Automatically generate a rewritten CV tailored to the job (no embellishments, UK spelling only)
4. **Interview preparation:**
   - Generate 20 likely questions from the job advert (including 5 technical + 10 competency-based)
   - Generate tailored answers based on your CV

---

## 🗂️ Folder Structure

```
careers-advisor/
├── app.py                      # Main Flask app
├── requirements.txt            # Python dependencies
├── templates/                  # HTML templates
│   ├── index.html              # Homepage form
│   └── results.html            # Results display
├── static/
│   └── style.css               # Page styling
├── uploads/                    # Uploaded documents
│   ├── cvs/
│   └── jobadverts/
├── utils/                      # Backend logic
│   ├── extract_text.py         # Extract text from PDF/DOCX
│   ├── cv_feedback.py          # Feedback and rewriting logic
│   ├── tailor_cv.py            # Tailoring logic for job adverts
│   ├── interview_questions.py  # Question generation
│   └── generate_answers.py     # Answer generation using CV
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/careers-advisor.git
cd careers-advisor
```

### 2. Set up virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

- Built using **Flask** for the web interface.
- Uses **LangChain** with **LLaMA 3 (via Ollama)** for all LLM-based features.
- Handles PDF and DOCX file input.
- Generates text output and downloadable rewritten CVs.

All outputs follow **British spelling**, are free of embellishment, and label any suggested example content clearly.

---

## 🔐 Notes

- Make sure **Ollama** is installed and running locally.
- Ensure all models used (e.g. `llama3`) are downloaded in Ollama.

---

## 📄 License

MIT License – feel free to fork and adapt for educational or career support purposes.
