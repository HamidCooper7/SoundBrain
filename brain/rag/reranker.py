from sentence_transformers import CrossEncoder

from brain.runtime import ModelRuntime


MODEL_NAME = "bge-reranker-v2-m3"


def get_reranker(runtime: ModelRuntime | None = None) -> CrossEncoder:
    assets = (runtime or ModelRuntime.shared()).load(
        model_name=MODEL_NAME,
        model_cls=CrossEncoder,
        backend="sentence-transformers",
        trust_remote_code=True,
    )
    return assets.model


def rerank(
    query: str,
    documents: list,
    top_k: int = 5,
):

    if not documents:
        return []

    pairs = [
        (query, doc["text"])
        for doc in documents
    ]

    scores = get_reranker().predict(
        pairs,
        show_progress_bar=False,
    )

    for doc, score in zip(documents, scores):
        doc["rerank_score"] = float(score)

    documents.sort(
        key=lambda x: x["rerank_score"],
        reverse=True,
    )

    return documents[:top_k]
