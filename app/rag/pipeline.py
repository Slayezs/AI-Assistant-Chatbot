from app.rag.retriever import get_retriever
from app.rag.llm import get_llm
from app.rag.prompt import build_prompt


retriever = get_retriever()
tokenizer, model = get_llm()


def ask_question(query):

    docs = retriever.invoke(query)
    docs = docs[:3]

    context = "\n".join([doc.page_content for doc in docs])

    prompt = build_prompt(context, query)

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=150
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer