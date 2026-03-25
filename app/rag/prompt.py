def build_prompt(context, question):

    prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the context below.
- If answer is not found, say "I don't know"
- Keep answer short (1-3 lines)
- Do NOT add extra information
- Do not repeat the question

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt