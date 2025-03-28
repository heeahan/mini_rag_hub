VECTOR_DB = {}

def add_to_vectorstore(doc_id, chunks, tenant):
    if tenant not in VECTOR_DB:
        VECTOR_DB[tenant] = []
    for chunk in chunks:
        VECTOR_DB[tenant].append((doc_id, chunk))

def search_vectorstore(query, tenant):
    if tenant not in VECTOR_DB:
        return []
    return [chunk for _, chunk in VECTOR_DB[tenant][:3]]
