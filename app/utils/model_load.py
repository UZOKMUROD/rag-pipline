from sentence_transformers import SentenceTransformer, CrossEncoder
from app.config import save_encoder_path, save_reranker_path


def load_encoder():

    try:
        print("Loading encoder model......")
        model = SentenceTransformer(save_encoder_path)
    except OSError as e:
        raise ValueError(f"Loading is failed: {e}")
    
    return model

def load_reranker():

    try:
        print("Loading reranker model......")
        model = CrossEncoder(save_reranker_path)
    except OSError as e:
        raise ValueError(f"Loading is failed: {e}")
    
    return model