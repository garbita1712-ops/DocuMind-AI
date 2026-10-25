import os

class Settings:
    PROJECT_NAME: str = "DocuMind AI"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    VECTOR_DIM: int = 384
    TOP_K_RETRIEVAL: int = 4
    SIMILARITY_THRESHOLD: float = 0.65
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 80
    HOST: str = "0.0.0.0"
    PORT: int = 8000

settings = Settings()
