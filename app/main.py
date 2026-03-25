from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os

from app.rag.pipeline import ask_question
from app.document_processing.ingest import ingest_document
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Ensure documents folder exists
os.makedirs("data/documents", exist_ok=True)


# Request schema for /ask
class QueryRequest(BaseModel):
    query: str


# Root endpoint
@app.get("/")
def home():
    return {"message": "RAG Chatbot API is running"}


# Ask question endpoint
@app.post("/ask")
def ask(request: QueryRequest):

    try:
        answer = ask_question(request.query)
        return {
            "query": request.query,
            "answer": answer,
            "status": "success"
        }
    except Exception as e:
        return {
            "error": str(e),
            "status": "failed"
        }


# Upload document endpoint
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):

    file_path = f"data/documents/{file.filename}"

    # Save file locally
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Ingest into vector database
    ingest_document(file_path)

    return {
        "message": f"{file.filename} uploaded and processed successfully"
    }