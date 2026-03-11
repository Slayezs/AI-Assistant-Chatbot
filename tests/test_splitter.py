import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.document_processing.loader import load_pdf
from app.document_processing.splitter import split_documents

docs = load_pdf("data/documents/company_policy.pdf")

chunks = split_documents(docs)

print("Total Chunks:", len(chunks))

print(chunks[0].page_content)