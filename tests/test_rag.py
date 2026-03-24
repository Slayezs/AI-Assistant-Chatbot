import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.rag.pipeline import ask_question

query = "What is the refund policy?"

response = ask_question(query)

print("\nAnswer:\n")
print(response)