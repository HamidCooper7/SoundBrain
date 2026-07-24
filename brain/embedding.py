from __future__ import annotations

from sentence_transformers import SentenceTransformer

from brain.infrastructure.config import settings
from brain.runtime import ModelRuntime


def get_embedding_model() -> SentenceTransformer:
    assets = ModelRuntime.shared().load(
        model_name=str(settings.embedding.model_path),
        model_cls=SentenceTransformer,
        backend="sentence-transformers",
        trust_remote_code=True,
    )
    return assets.model
