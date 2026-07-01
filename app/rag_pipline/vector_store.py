import faiss
import numpy as np


class VectorStore:
    
    def __init__(self, dim: int | None=None):
        self.dim = dim
        self.ids: list[int] = []
        self.index = None
        
    
    def build(self, vector: np.ndarray, ids:list[int]):
        
        vector = _normalize(vector=vector.astype(np.float32))
        self.dim = vector.shape[1]
        self.index = faiss.IndexFlatIP(self.dim)
        self.index.add(vector)
        self.ids = list(ids)
        return self
    
    def add(self, vector: np.ndarray, ids:list[int]):
        if self.index is None:
            return self.build(vector, ids)
        vector = _normalize(vector=vector.astype(np.float32))
        self.index.add(vector)
        self.ids.extend(ids)
        return self
    
    def search(self, query_vector: np.ndarray, top_k:int = 50):
        if self.index is None or self.index.ntotal==0:
            return []
        
        query_vector = _normalize(query_vector.astype(np.float32).reshape(1, -1))
        top_k = min(top_k, self.index.ntotal)
        scores, positions = self.index.search(query_vector, top_k)
        results = []
        for pos, score in zip(positions[0], scores[0]):
            if pos == -1:
                continue
            
            results.append((self.ids[pos], float(score)))
            
        return results
        
    def save():
        
        print()
        
        
def _normalize(vector: np.ndarray) -> np.ndarray:
    
    norms = np.linalg.norm(vector, axis=1, keepdims=True)
    norms[norms == 0] = 1e-12
    return vector/norms
