from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# Ask user for PDF file name
pdf_file = input("Enter the name of the PDF file to analyse (e.g. jobadvert.pdf): ").strip()

# Load and split the PDF
loader = PyPDFLoader(pdf_file)
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
docs = splitter.split_documents(pages)

# Use HuggingFace sentence embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)

# Set up local LLaMA 3 via Ollama
llm = Ollama(model="llama3")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type="stuff"
)

# Ask questions in a loop
print("\n✅ PDF loaded. You can now ask questions. Type 'exit' to quit.\n")
while True:
    query = input("Ask a question: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Exiting.")
        break
    answer = qa_chain.run(query)
    print("\n🔎 Answer:\n", answer, "\n")