import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.rag.retriever import get_retriever

retriever = get_retriever()

query = "What is refund policy?"

docs = retriever.invoke(query)

for doc in docs:
    print(doc.page_content)
    print("------")