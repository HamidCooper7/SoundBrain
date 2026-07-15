from __future__ import annotations

import torch
from sentence_transformers import SentenceTransformer

from brain.infrastructure.config import settings


DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print(f"Embedding Device: {DEVICE}")


_embedding_model = SentenceTransformer(
    str(settings.embedding.model_path),
    trust_remote_code=True,
    device=DEVICE,
)


def get_embedding_model() -> SentenceTransformer:

    return _embedding_model