from __future__ import annotations

from brain.audio.embeddings.clap import CLAPEmbedding
from brain.audio.embeddings.factory import EmbeddingFactory
from brain.audio.embeddings.models import EmbeddingCapability
from brain.audio.embeddings.registry import EmbeddingRegistry
from brain.audio.embeddings.tasks import EmbeddingTask
from brain.runtime import DeviceManager


def create_embedding_registry() -> EmbeddingRegistry:

    registry = EmbeddingRegistry()

    provider = CLAPEmbedding()

    registry.register(
        capability=EmbeddingCapability(
            name=provider.name,
            dimension=provider.dimension,
            tasks=frozenset(
                {
                    EmbeddingTask.SEMANTIC_SEARCH.value,
                }
            ),
            backend="transformers",
            device=str(DeviceManager.detect()),
        ),
        provider=provider,
    )

    return registry


def create_embedding_factory() -> EmbeddingFactory:

    registry = create_embedding_registry()

    return EmbeddingFactory(
        registry=registry,
    )
