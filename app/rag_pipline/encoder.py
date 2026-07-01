import numpy as np

from app.utils.model_load import load_encoder
from app.rag_pipline.vector_store import VectorStore



_model = None


def get_encoder():
    global _model
    if _model is None:
        _model = load_encoder()
    return _model


def embed_chunks(chunks: list[str], batch_size: int = 32):
    
    model = get_encoder()
    vector = model.encode(
        chunks,
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=len(chunks)>50
    )
    
    return np.asarray(vector, dtype=np.float32)
    
    
def embed_query(query):
    
    model = get_encoder()
    vector = model.encode(query, normalize_embeddings=True)
    
    return np.asarray(vector, dtype=np.float32)

    
def build_vector_store():
    print()
    
    
    


 