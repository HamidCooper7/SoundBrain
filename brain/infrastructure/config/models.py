from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class LLMConfig:

    provider: str = "lmstudio"

    model: str = "local-model"

    base_url: str = "http://127.0.0.1:1234/v1"

    api_key: str = "lm-studio"

    temperature: float = 0.0

    top_p: float = 0.9


@dataclass(slots=True)
class EmbeddingConfig:

    model_path: Path = Path("models/Qwen3-Embedding-0.6B")

    device: str = "auto"


@dataclass(slots=True)
class ChromaConfig:

    path: Path = Path("data/chroma")

    collection: str = "soundbrain"


@dataclass(slots=True)
class AppConfig:

    llm: LLMConfig

    embedding: EmbeddingConfig

    chroma: ChromaConfig