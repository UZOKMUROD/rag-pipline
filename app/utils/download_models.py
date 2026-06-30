import os
from app.config import encoder_model, reranker_model, save_encoder_path, save_reranker_path
from huggingface_hub import snapshot_download


BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ensure_all_directories():
    """Create all necessary directories for the project."""
    directories = [
        os.path.join(BACKEND_DIR, "models"),
        os.path.join(BACKEND_DIR, "models", "encoder"),
        os.path.join(BACKEND_DIR, "models", "reranker"),
        os.path.join(BACKEND_DIR, "data"),
        os.path.join(BACKEND_DIR, "data", "victorDB"),
    ]


    for path in directories:
        if os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            print(f"📁 Created directory: {path}")


    return True


def download_encoder():

    try:
        os.makedirs(save_encoder_path, exist_ok=True)
        if os.path.exists(save_encoder_path) and os.listdir(save_encoder_path):
            print(f"✅ Encoder model already exists at: {save_encoder_path}")
        else:
            print(f"📥 Downloading encoder model: {encoder_model}")
            snapshot_download(
                repo_id=encoder_model,
                local_dir=save_encoder_path,
                local_dir_use_symlinks=False,  
                resume_download=True
            )
            print(f"✅ Encoder model saved to: {save_encoder_path}")
    except OSError as e:
        raise ValueError(f"Failed to create or access directory: {e}")
    
    return True

def download_decoder():
        try:
            os.makedirs(save_reranker_path, exist_ok=True)
            if os.path.exists(save_reranker_path) and os.listdir(save_reranker_path):
                print(f"✅ Reranker model already exists at: {save_reranker_path}")
            else:
                print(f"📥 Downloading reranker model: {reranker_model}")
                snapshot_download(
                    repo_id=reranker_model,
                    local_dir=save_reranker_path,
                    local_dir_use_symlinks=False,  
                    resume_download=True
                    )
                print(f"✅ Reranker model saved to: {save_reranker_path}")
        except OSError as e:
            raise ValueError(f"Failed to create or access directory: {e}")
        
        return True

    

