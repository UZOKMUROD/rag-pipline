from app.utils.model_load import load_encoder
from app.utils.chunker import chunker


model = load_encoder()


def embedder(chunks = chunker()):
    
    for chunk in chunks:
        print(chunk)