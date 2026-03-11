import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.rag.embeddings import get_embeddings

embeddings = get_embeddings()

vector = embeddings.embed_query("What is refund policy?")

print("Vector length:", len(vector))
print(vector[:5])