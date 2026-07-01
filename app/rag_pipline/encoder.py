from app.utils.model_load import load_encoder
from app.utils.chunker import chunker


model = load_encoder()


def embedder(chunks = chunker()):
    
    for chunk in chunks:
        print()


"""
import numpy as np

from app.utils.model_load import load_encoder
from app.rag_pipline.vector_store import VectorStore

import torch
from sentence_transformers import SentenceTransformer

# Qwen3-Embedding models are instruction-tuned: prefixing the *query* (not the
# documents) with a task instruction measurably improves retrieval quality.
QUERY_INSTRUCTION = (
    "Instruct: Given a question about a driver-operator logistics chat log, "
    "retrieve the chat passages that answer it\nQuery: {query}"
)

_model = None


def get_encoder():
    global _model
    if _model is None:
        _model = load_encoder()
    return _model


def embed_texts(texts: list[str], batch_size: int = 32) -> np.ndarray:
 
    model = get_encoder()
    vectors = model.encode(
        texts,
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=len(texts) > 50,
    )
    return np.asarray(vectors, dtype="float32")


def embed_query(query: str) -> np.ndarray:
    model = get_encoder()
    prefixed = QUERY_INSTRUCTION.format(query=query)
    vector = model.encode([prefixed], normalize_embeddings=True)
    return np.asarray(vector[0], dtype="float32")


def build_vector_store(chunk_ids: list[int], chunk_texts: list[str]) -> VectorStore:
   
    vectors = embed_texts(chunk_texts)
    store = VectorStore().build(vectors, chunk_ids)
    return store
"""
