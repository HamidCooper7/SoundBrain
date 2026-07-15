from __future__ import annotations

import numpy as np
from sentence_transformers import SentenceTransformer

from brain.text.embeddings.base import TextEmbeddingModel


class SentenceTransformerEmbedding(TextEmbeddingModel):

    MODEL_NAME = "Qwen/Qwen3-Embedding-0.6B"

    def __init__(self) -> None:

        self._model = SentenceTransformer(
            self.MODEL_NAME,
            trust_remote_code=True,
        )

    @property
    def name(self) -> str:
        return "sentence-transformer"

    @property
    def dimension(self) -> int:
        return 1024

    def encode(
        self,
        text: str | list[str],
    ) -> np.ndarray:

        embedding = self._model.encode(
            text,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

        return embedding