def build_prompt(context, question):

    prompt = f"""
You are an AI assistant that answers questions strictly based on the given context.

Instructions:
- Use ONLY the context below
- If answer is not in context, say "I don't know"
- Keep answer short and clear (2-3 lines max)

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt