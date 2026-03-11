from app.document_processing.ingest import ingest_document

vector_db = ingest_document("data/documents/company_policy.pdf")

print("Vector DB created successfully")