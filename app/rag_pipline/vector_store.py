"""
Thin wrapper around a FAISS flat index (cosine similarity via inner product
on L2-normalized vectors). Row position in the index == position in the
parallel `ids` list == the SQLite `chunks.id` for that vector.
"""

import json
import os
import numpy as np
import faiss

from app.config import faiss_index_path, faiss_ids_path


class VectorStore:
    def __init__(self, dim: int | None = None):
        self.dim = dim
        self.index = None
        self.ids: list[int] = []

    def build(self, vectors: np.ndarray, ids: list[int]):
        vectors = _normalize(vectors.astype("float32"))
        self.dim = vectors.shape[1]
        self.index = faiss.IndexFlatIP(self.dim)
        self.index.add(vectors)
        self.ids = list(ids)
        return self

    def add(self, vectors: np.ndarray, ids: list[int]):
        if self.index is None:
            return self.build(vectors, ids)
        vectors = _normalize(vectors.astype("float32"))
        self.index.add(vectors)
        self.ids.extend(ids)
        return self

    def search(self, query_vector: np.ndarray, top_k: int = 20):
        """Returns list of (chunk_id, score) sorted by descending similarity."""
        if self.index is None or self.index.ntotal == 0:
            return []
        q = _normalize(query_vector.astype("float32").reshape(1, -1))
        top_k = min(top_k, self.index.ntotal)
        scores, positions = self.index.search(q, top_k)
        results = []
        for pos, score in zip(positions[0], scores[0]):
            if pos == -1:
                continue
            results.append((self.ids[pos], float(score)))
        return results

    def save(self, index_path: str = None, ids_path: str = None):
        index_path = index_path or faiss_index_path
        ids_path = ids_path or faiss_ids_path
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        faiss.write_index(self.index, index_path)
        with open(ids_path, "w") as f:
            json.dump(self.ids, f)

    @classmethod
    def load(cls, index_path: str = None, ids_path: str = None) -> "VectorStore":
        index_path = index_path or faiss_index_path
        ids_path = ids_path or faiss_ids_path
        if not (os.path.exists(index_path) and os.path.exists(ids_path)):
            raise FileNotFoundError(
                f"No FAISS index found at {index_path}. Run ingestion first."
            )
        store = cls()
        store.index = faiss.read_index(index_path)
        with open(ids_path) as f:
            store.ids = json.load(f)
        store.dim = store.index.d
        return store


def _normalize(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1e-12
    return vectors / norms
