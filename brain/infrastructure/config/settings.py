from __future__ import annotations

from brain.infrastructure.config.models import (
    AppConfig,
    ChromaConfig,
    EmbeddingConfig,
    LLMConfig,
)


settings = AppConfig(
    llm=LLMConfig(),
    embedding=EmbeddingConfig(),
    chroma=ChromaConfig(),
)