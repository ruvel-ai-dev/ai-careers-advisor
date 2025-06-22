from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import Ollama

# Load PDF
loader = PyPDFLoader("jobadvert.pdf")
pages = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(pages)

# Fix input variable name: must be "context"
prompt_template = """You are an AI careers assistant. Summarise the main job requirements in this job advert.
Return a clear, bullet-pointed list of key skills, experience, and qualifications required.

{context}

SUMMARY:"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context"])

# Use local LLaMA 3 model
llm = Ollama(model="llama3")

# Load the QA chain with corrected prompt
chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)

# Prepare inputs and invoke
inputs = {
    "input_documents": texts,
    "question": "Summarise the job requirements clearly and professionally."
}
response = chain.invoke(inputs)

# Print result
print("\n--- AI Job Summary ---\n")
print(response["output_text"])
