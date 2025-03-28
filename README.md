# MiniRAGHub

**MiniRAGHub** is a lightweight, multi-tenant RAG (Retrieval-Augmented Generation) platform designed for local development and enterprise prototyping. It integrates document upload, vector search, and LLM-based Q&A through a modular architecture.

---

## Features

- **Multi-tenant Support** – Isolate data by `namespace` or `tenant`.
- **Document Upload** – Upload `.txt` or `.pdf` files for semantic search.
- **Text Chunking** – Split documents into manageable chunks.
- **Vector Store (Pluggable)** – Built-in mock DB; Milvus-ready.
- **LLM Integration (Pluggable)** – Switch between GPT-3.5, Claude, Mistral, or mock LLMs.
- **Docker-Compose Setup** – One command to run backend + Milvus + MinIO.

---

## Tech Stack

| Layer     | Tech                  |
|-----------|-----------------------|
| Backend   | Python + FastAPI      |
| Storage   | MinIO (S3-compatible) |
| Vector DB | Milvus (v2.x)         |
| Model     | LLM via API (OpenAI / Claude / Local) |
| Deployment | Docker Compose       |

---

## Folder Structure

TBC

