from __future__ import annotations

from brain.infrastructure.config import settings
from brain.runtime import ModelRuntime


def get_embedding_model():
    """
    Lazily load the configured sentence-transformer embedding model.

    ``sentence_transformers`` is imported inside the function so that importing
    ``brain.embedding`` does not pull heavy dependencies at module level.
    """
    from sentence_transformers import SentenceTransformer

    assets = ModelRuntime.shared().load(
        model_name=str(settings.embedding.model_path),
        model_cls=SentenceTransformer,
        backend="sentence-transformers",
        trust_remote_code=True,
    )
    return assets.model


__all__ = ["get_embedding_model"]
