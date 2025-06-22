from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_interview_questions(job_description):
    prompt = PromptTemplate.from_template("""
You are a UK-based careers expert.

Based on the following job description, generate a list of **20 possible interview questions** the candidate might be asked. Use UK spelling only. Include:
- 5 technical questions,
- 10 competency-based questions,
- 5 general/behavioural questions.

Job Description:
{job_description}
""")

    llm = OllamaLLM(model="llama3")
    chain = LLMChain(prompt=prompt, llm=llm)
    response = chain.run(job_description)
    return response
