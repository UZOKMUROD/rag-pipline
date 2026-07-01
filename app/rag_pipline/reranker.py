from app.utils.model_load import load_reranker

_model = None


def get_reranker():
    global _model
    if _model is None:
        _model = load_reranker()
    return _model


def rerank(query: str, candidates: list[dict], top_n: int = 5) -> list[dict]:

    if not candidates:
        return []

    model = get_reranker()
    pairs = [(query, c["text"]) for c in candidates]
    scores = model.predict(pairs)

    for c, s in zip(candidates, scores):
        c["rerank_score"] = float(s)

    ranked = sorted(candidates, key=lambda c: c["rerank_score"], reverse=True)
    return ranked[:top_n]
