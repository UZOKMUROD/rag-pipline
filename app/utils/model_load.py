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



"""

import os
import torch
from sentence_transformers import SentenceTransformer, CrossEncoder
from app.config import save_encoder_path, save_reranker_path

# Detect the best available hardware accelerator
if torch.cuda.is_available():
    DEVICE = "cuda"
elif torch.backends.mps.is_available():
    DEVICE = "mps" # For Apple Silicon Macs
else:
    DEVICE = "cpu"

def _check_downloaded(path: str, label: str):
    if not (os.path.isdir(path) and os.listdir(path)):
        raise FileNotFoundError(
            f"{label} model not found at '{path}'. "
            f"Run `python -m app.utils.download_models` first."
        )

def load_encoder():
    _check_downloaded(save_encoder_path, "Encoder")
    try:
        print(f"Loading encoder model on {DEVICE}......")
        model = SentenceTransformer(save_encoder_path, device=DEVICE)
    except OSError as e:
        raise ValueError(f"Loading is failed: {e}")

    return model

def load_reranker():
    _check_downloaded(save_reranker_path, "Reranker")
    try:
        print(f"Loading reranker model on {DEVICE}......")
        model = CrossEncoder(save_reranker_path, device=DEVICE)
    except OSError as e:
        raise ValueError(f"Loading is failed: {e}")

    return model

"""