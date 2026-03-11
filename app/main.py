from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG Knowledge Assistant Running"}