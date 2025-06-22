from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# Load and split the PDF
loader = PyPDFLoader("jobadvert.pdf")
pages = loader.load_and_split()

# Prompt setup
prompt_template = """
You are a helpful careers advisor in the UK. Use the following job advert content to answer the question.
{context}
Question: {question}
Helpful Answer:"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Set up the model
llm = OllamaLLM(model="llama3")

# Create QA chain
chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)

# Ask a question
query = "What are the main skills this job is looking for?"
response = chain.invoke({"input_documents": pages, "question": query})

print("\n--- AI Careers Advisor Answer ---\n")
print(response["output_text"])