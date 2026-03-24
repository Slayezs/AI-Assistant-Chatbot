from transformers import pipeline


def get_llm():

    generator = pipeline(
        "text-generation",   
        model="gpt2",
        max_new_tokens=150, 
    )

    return generator