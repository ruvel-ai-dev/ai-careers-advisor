from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

TEMPLATE_ADVICE = """
You are a UK careers advisor. Below is a CV and a job advert.

Your task is to explain clearly how the candidate should tailor their CV to the job advert.
Only give advice, do not rewrite the CV.

--- CV ---
{cv}

--- Job Advert ---
{job}

Give specific, bullet-point suggestions.
"""

TEMPLATE_REWRITE = """
You are a UK careers advisor. Below is a CV and a job advert.

Rewrite the CV to tailor it specifically to the job advert.
Use plain UK English. Use UK spelling only.
Only include realistic examples. If inserting a template phrase, clearly mark it with [EXAMPLE] so it’s obvious it’s a placeholder.

--- CV ---
{cv}

--- Job Advert ---
{job}

Output only the rewritten CV.
"""

def tailor_cv_to_job(cv_text, job_text, mode="advice"):
    if mode == "advice":
        prompt = PromptTemplate.from_template(TEMPLATE_ADVICE)
    elif mode == "rewrite":
        prompt = PromptTemplate.from_template(TEMPLATE_REWRITE)
    else:
        raise ValueError("Invalid mode. Use 'advice' or 'rewrite'.")

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.invoke({"cv": cv_text, "job": job_text})
    return result["text"]
