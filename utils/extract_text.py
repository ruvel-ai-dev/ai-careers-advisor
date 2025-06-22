from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader

def extract_text_from_file(file_path):
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext in [".docx", ".doc"]:
        loader = UnstructuredWordDocumentLoader(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or Word document.")

    documents = loader.load()
    return "\n\n".join(doc.page_content for doc in documents)
