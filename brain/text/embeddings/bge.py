from __future__ import annotations

import numpy as np

from sentence_transformers import SentenceTransformer

from brain.runtime import ModelRuntime

from .base import TextEmbeddingModel
from .models import EmbeddingCapability


class BGEEmbedding(TextEmbeddingModel):

    MODEL_NAME = "BAAI/bge-m3"

    def __init__(self) -> None:

        self._runtime = ModelRuntime()

        self._assets = self._runtime.load(
            model_name=self.MODEL_NAME,
            model_cls=SentenceTransformer,
        )

    @property
    def name(self) -> str:

        return "bge-m3"

    @property
    def dimension(self) -> int:

        return 1024

    @property
    def capability(self) -> EmbeddingCapability:

        return EmbeddingCapability(
            backend="sentence-transformers",
            device=str(self._assets.device),
        )

    def encode(
        self,
        text: str | list[str],
    ) -> np.ndarray:

        model: SentenceTransformer = self._assets.model

        embedding = model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return np.asarray(
            embedding,
            dtype=np.float32,
        )