from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.pipeline import ask_question

app = FastAPI()


# Request body schema
class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "RAG Chatbot API is running"}


@app.post("/ask")
def ask(request: QueryRequest):

    query = request.query

    answer = ask_question(query)

    return {
        "query": query,
        "answer": answer
    }