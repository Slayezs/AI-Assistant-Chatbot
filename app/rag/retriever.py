from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embeddings


def get_retriever():

    embeddings = get_embeddings()

    vector_db = FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_db.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever