from sentence_transformers import CrossEncoder

MODEL_PATH = r"E:\SoundBrain\models\bge-reranker-v2-m3"

print("Loading Reranker...")

model = CrossEncoder(
    MODEL_PATH,
    trust_remote_code=True,
)

print("Reranker Ready")


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

    scores = model.predict(
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