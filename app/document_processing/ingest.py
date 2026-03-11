from app.document_processing.loader import load_pdf
from app.document_processing.splitter import split_documents
from app.rag.embeddings import get_embeddings
from app.vector_db.faiss_store import create_vector_store


def ingest_document(file_path):

    docs = load_pdf(file_path)

    chunks = split_documents(docs)

    embeddings = get_embeddings()

    vector_db = create_vector_store(chunks, embeddings)

    return vector_db