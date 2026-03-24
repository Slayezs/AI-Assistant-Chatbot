from app.rag.retriever import get_retriever
from app.rag.llm import get_llm
from app.rag.prompt import build_prompt


retriever = get_retriever()
llm = get_llm()


def ask_question(query):

    # Step 1: Retrieve documents
    docs = retriever.invoke(query)

    # Step 2: Combine context
    context = "\n".join([doc.page_content for doc in docs])

    # Step 3: Build prompt
    prompt = build_prompt(context, query)

    # Step 4: Generate answer
    result = llm(prompt)

    raw_output = result[0]["generated_text"]

    # Remove prompt
    answer = raw_output.replace(prompt, "").strip()

    # Keep only first meaningful paragraph
    answer = answer.split("\n")[0].strip()


    return answer