from flask import Flask, render_template, request, send_from_directory, abort, url_for
import os
import uuid
from docx import Document
from utils.extract_text import extract_text_from_file
from utils.cv_feedback import give_cv_feedback, improve_cv
from utils.tailor_cv import tailor_cv_to_job
from utils.interview_questions import generate_interview_questions
from utils.generate_answers import generate_answers_from_cv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload subdirectories exist
for folder in ['cvs', 'jobadverts']:
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], folder), exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    task = request.form.get('task')
    job_file = request.files.get('job_file')
    cv_file = request.files.get('cv_file')

    job_path = None
    cv_path = None

    if job_file and job_file.filename != "":
        job_filename = f"{uuid.uuid4()}_{job_file.filename}"
        job_path = os.path.join(app.config['UPLOAD_FOLDER'], 'jobadverts', job_filename)
        job_file.save(job_path)

    if cv_file and cv_file.filename != "":
        cv_filename = f"{uuid.uuid4()}_{cv_file.filename}"
        cv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cvs', cv_filename)
        cv_file.save(cv_path)

    try:
        if task == "extract_job":
            if not job_path:
                return render_template("results.html", error="Please upload a job advert.")
            job_text = extract_text_from_file(job_path)
            result = f"--- Job Requirements Extracted ---\n\n{job_text}"

        elif task == "cv_feedback":
            if not cv_path:
                return render_template("results.html", error="Please upload a CV.")
            cv_text = extract_text_from_file(cv_path)
            result = clean_output(give_cv_feedback(cv_text))

        elif task == "cv_rewrite":
            if not cv_path:
                return render_template("results.html", error="Please upload a CV.")
            cv_text = extract_text_from_file(cv_path)
            rewritten = clean_output(improve_cv(cv_text))

            output_file = f"{cv_path}_improved.docx"
            save_docx(output_file, rewritten)

            rel_path = os.path.relpath(output_file, app.config['UPLOAD_FOLDER'])
            download_url = url_for('download_file', filename=rel_path)
            return render_template("results.html", result="Improved CV generated below.", download_link=download_url)

        elif task == "tailor_advice":
            if not cv_path or not job_path:
                return render_template("results.html", error="Please upload both CV and job advert.")
            cv_text = extract_text_from_file(cv_path)
            job_text = extract_text_from_file(job_path)
            result = clean_output(tailor_cv_to_job(cv_text, job_text, mode="advice"))

        elif task == "tailor_rewrite":
            if not cv_path or not job_path:
                return render_template("results.html", error="Please upload both CV and job advert.")
            cv_text = extract_text_from_file(cv_path)
            job_text = extract_text_from_file(job_path)
            tailored = clean_output(tailor_cv_to_job(cv_text, job_text, mode="rewrite"))

            output_file = f"{cv_path}_tailored.docx"
            save_docx(output_file, tailored)

            rel_path = os.path.relpath(output_file, app.config['UPLOAD_FOLDER'])
            download_url = url_for('download_file', filename=rel_path)
            return render_template("results.html", result="Tailored CV generated below.", download_link=download_url)

        elif task == "interview_questions":
            if not job_path:
                return render_template("results.html", error="Please upload a job advert.")
            job_text = extract_text_from_file(job_path)
            result = clean_output(generate_interview_questions(job_text))

        elif task == "answer_questions":
            if not cv_path or not job_path:
                return render_template("results.html", error="Please upload both CV and job advert.")
            job_text = extract_text_from_file(job_path)
            cv_text = extract_text_from_file(cv_path)
            result = clean_output(generate_answers_from_cv(job_text, cv_text))

        else:
            result = "Invalid option selected."

        return render_template("results.html", result=result)

    except Exception as e:
        return render_template("results.html", error=f"An error occurred: {str(e)}")

@app.route('/download/<path:filename>')
def download_file(filename):
    safe_path = os.path.normpath(filename)
    if os.path.isabs(safe_path) or '..' in safe_path.split(os.path.sep):
        abort(400)
    return send_from_directory(app.config['UPLOAD_FOLDER'], safe_path, as_attachment=True)

def clean_output(text):
    """Remove markdown-style asterisks and unnecessary symbols from LLM output."""
    return text.replace("**", "").replace("*", "").strip()

def save_docx(path, text):
    doc = Document()
    for line in text.split('\n'):
        if line.strip():
            doc.add_paragraph(line.strip())
    doc.save(path)

if __name__ == '__main__':
    debug_env = os.getenv('FLASK_DEBUG', 'False')
    debug_mode = debug_env.lower() in ('1', 'true', 'yes', 'y', 't')
    app.run(debug=debug_mode)

