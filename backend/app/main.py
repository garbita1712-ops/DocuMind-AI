import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from .config import settings
from .schemas import QueryRequest, QueryResponse, IngestResponse
from .rag_engine import rag_service

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Multimodal RAG & Neural Document Intelligence Platform"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "frontend")
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
async def root():
    index_file = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": f"Welcome to {settings.PROJECT_NAME} API", "version": settings.VERSION}

@app.get(f"{settings.API_PREFIX}/health")
async def health():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "indexed_chunks": len(rag_service.index.chunks),
        "registered_documents": len(rag_service.doc_registry),
        "embedding_dim": settings.VECTOR_DIM
    }

@app.post(f"{settings.API_PREFIX}/query", response_model=QueryResponse)
async def query_knowledge_base(payload: QueryRequest):
    if not payload.query.strip():
        raise HTTPException(status_code=400, detail="Query string cannot be empty.")
    res = rag_service.query(payload.query, top_k=payload.top_k or settings.TOP_K_RETRIEVAL)
    return res

@app.post(f"{settings.API_PREFIX}/query/stream")
async def stream_query_knowledge_base(payload: QueryRequest):
    if not payload.query.strip():
        raise HTTPException(status_code=400, detail="Query string cannot be empty.")
    return StreamingResponse(
        rag_service.stream_query(payload.query, top_k=payload.top_k or settings.TOP_K_RETRIEVAL),
        media_type="text/event-stream"
    )

@app.post(f"{settings.API_PREFIX}/ingest", response_model=IngestResponse)
async def ingest_document(file: UploadFile = File(...)):
    try:
        content_bytes = await file.read()
        text_content = content_bytes.decode("utf-8", errors="ignore")
        doc_id, count = rag_service.ingest_document(file.filename or "uploaded_doc.txt", text_content)
        return IngestResponse(
            doc_id=doc_id,
            filename=file.filename or "uploaded_doc.txt",
            num_chunks=count,
            message=f"Successfully indexed {count} dense vector chunks into knowledge base."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host=settings.HOST, port=settings.PORT, reload=True)
