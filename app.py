from flask import Flask, render_template, request, send_file
import os
import uuid

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
            result = give_cv_feedback(cv_text)

        elif task == "cv_rewrite":
            if not cv_path:
                return render_template("results.html", error="Please upload a CV.")
            cv_text = extract_text_from_file(cv_path)
            rewritten = improve_cv(cv_text)
            output_file = f"{cv_path}_improved.txt"
            with open(output_file, 'w') as f:
                f.write(rewritten)
            return render_template("results.html", result="Improved CV generated below.", download_link=output_file)

        elif task == "tailor_advice":
            if not cv_path or not job_path:
                return render_template("results.html", error="Please upload both CV and job advert.")
            cv_text = extract_text_from_file(cv_path)
            job_text = extract_text_from_file(job_path)
            result = tailor_cv_to_job(cv_text, job_text, mode="advice")

        elif task == "tailor_rewrite":
            if not cv_path or not job_path:
                return render_template("results.html", error="Please upload both CV and job advert.")
            cv_text = extract_text_from_file(cv_path)
            job_text = extract_text_from_file(job_path)
            tailored = tailor_cv_to_job(cv_text, job_text, mode="rewrite")
            output_file = f"{cv_path}_tailored.txt"
            with open(output_file, 'w') as f:
                f.write(tailored)
            return render_template("results.html", result="Tailored CV generated below.", download_link=output_file)

        elif task == "interview_questions":
            if not job_path:
                return render_template("results.html", error="Please upload a job advert.")
            job_text = extract_text_from_file(job_path)
            result = generate_interview_questions(job_text)

        elif task == "answer_questions":
            if not cv_path or not job_path:
                return render_template("results.html", error="Please upload both CV and job advert.")
            job_text = extract_text_from_file(job_path)
            cv_text = extract_text_from_file(cv_path)
            result = generate_answers_from_cv(job_text, cv_text)

        else:
            result = "Invalid option selected."

        return render_template("results.html", result=result)

    except Exception as e:
        return render_template("results.html", error=f"An error occurred: {str(e)}")

@app.route('/<path:filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
