from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class DocumentChunk(BaseModel):
    chunk_id: str
    doc_id: str
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    score: Optional[float] = None

class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 4
    stream: Optional[bool] = False

class Citation(BaseModel):
    source: str
    chunk_id: str
    snippet: str
    relevance_score: float

class QueryResponse(BaseModel):
    query: str
    answer: str
    citations: List[Citation]
    retrieval_latency_ms: float
    total_latency_ms: float

class IngestResponse(BaseModel):
    doc_id: str
    filename: str
    num_chunks: int
    message: str
