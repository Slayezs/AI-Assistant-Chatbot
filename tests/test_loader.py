import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.document_processing.loader import load_pdf

docs = load_pdf("data/documents/company_policy.pdf")

print(len(docs))

print(docs[0].page_content)