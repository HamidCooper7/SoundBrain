from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np

from brain.audio.io.models import AudioData
from .models import EmbeddingCapability


class AudioEmbeddingModel(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def dimension(self) -> int:
        ...

    @property
    @abstractmethod
    def capability(self) -> EmbeddingCapability:
        ...

    @abstractmethod
    def encode_audio(
        self,
        audio: AudioData,
    ) -> np.ndarray:
        ...

    @abstractmethod
    def encode_text(
        self,
        text: str | list[str],
    ) -> np.ndarray:
        ...