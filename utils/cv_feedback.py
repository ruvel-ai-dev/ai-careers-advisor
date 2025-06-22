from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM  # ✅ Fixed name

llm = OllamaLLM(model="llama3")  # ✅ Fixed name

# Option 2a – CV feedback
def give_cv_feedback(cv_text):
    prompt = PromptTemplate(
        input_variables=["cv"],
        template="""
You are a UK careers advisor. Give detailed feedback on the following CV. Use UK spelling only.

Be constructive, use bullet points, and cover structure, formatting, skills, and clarity.

CV:
{cv}
"""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"cv": cv_text})
    return result

# Option 2b – Rewrite CV to UK industry standard
def improve_cv(cv_text):
    prompt = PromptTemplate(
        input_variables=["cv"],
        template="""
You are an expert UK careers advisor.

Rewrite this CV in a professional UK format, using clear headings, bullet points, and correct spelling. Use UK spelling only.

If sections are missing (like personal profile or achievements), add appropriate content.

Mark any invented content or examples with [EXAMPLE] so the user knows what to replace.

Do NOT embellish or make up unrealistic achievements.

CV:
{cv}
"""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"cv": cv_text})
    return result
