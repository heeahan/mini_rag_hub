from fastapi import FastAPI, UploadFile, File, Form
from services.llm_router import query_llm
from services.vectorstore import add_to_vectorstore, search_vectorstore
from services.document_ingest import ingest_document
import uuid

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...), tenant: str = Form(...)):
    doc_id = str(uuid.uuid4())
    content = await file.read()
    ingest_document(doc_id, content, tenant)
    return {"status": "uploaded", "doc_id": doc_id}

@app.post("/ask")
async def ask(question: str = Form(...), tenant: str = Form(...), model: str = Form("gpt-3.5")):
    context_chunks = search_vectorstore(question, tenant)
    answer = query_llm(question, context_chunks, model)
    return {"answer": answer}
