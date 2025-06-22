from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_answers_from_cv(job_description, cv_text):
    prompt = PromptTemplate.from_template("""
You are a UK-based interview coach.

Using the CV and job description provided, generate tailored answers for each of the following interview questions the candidate might be asked. Use UK spelling only.

First, create a numbered list of:
- 5 technical questions
- 10 competency-based questions
- 5 general/behavioural questions

Then, for each question, provide a concise, UK-style model answer using only the candidate's CV content. If any assumptions or template examples are added, **clearly label them as examples**.

Job Description:
{job_description}

CV Content:
{cv_text}
""")

    llm = OllamaLLM(model="llama3")
    chain = LLMChain(prompt=prompt, llm=llm)
    response = chain.run({"job_description": job_description, "cv_text": cv_text})
    return response
