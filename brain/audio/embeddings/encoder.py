from __future__ import annotations

from brain.audio.embeddings.bootstrap import create_embedding_factory
from brain.audio.embeddings.factory import EmbeddingFactory
from brain.audio.embeddings.manager import EmbeddingManager
from brain.audio.embeddings.models import AudioEmbedding
from brain.audio.embeddings.tasks import EmbeddingTask
from brain.audio.io.models import AudioData


class AudioEncoder:

    def __init__(
        self,
        provider: str = "clap",
        factory: EmbeddingFactory | None = None,
    ) -> None:

        if factory is None:
            factory = create_embedding_factory()

        self._provider = provider

        self._manager = EmbeddingManager(factory)

    def encode(
        self,
        audio: AudioData,
        task: EmbeddingTask | None = None,
    ) -> AudioEmbedding:

        return self._manager.encode(
            provider=self._provider,
            audio=audio,
            task=task,
        )

    def encode_text(
        self,
        text: str | list[str],
    ) -> AudioEmbedding:

        return self._manager.encode_text(
            provider=self._provider,
            text=text,
        )