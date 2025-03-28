def ingest_document(doc_id, content, tenant):
    text = content.decode("utf-8")
    chunks = [text[i:i+200] for i in range(0, len(text), 200)]
    from .vectorstore import add_to_vectorstore
    add_to_vectorstore(doc_id, chunks, tenant)
