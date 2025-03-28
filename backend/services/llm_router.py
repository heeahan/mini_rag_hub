def query_llm(question, context_chunks, model):
    context = "\n".join(context_chunks)
    prompt = f"Answer based on context:\n{context}\n\nQ: {question}\nA:"
    return f"[Mock Answer from {model}]"
