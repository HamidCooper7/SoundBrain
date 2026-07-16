from __future__ import annotations

import numpy as np
import torch

from transformers import (
    ClapAudioModelWithProjection,
    ClapModel,
    ClapProcessor,
)

from brain.audio.embeddings.base import AudioEmbeddingModel
from brain.audio.embeddings.models import EmbeddingCapability
from brain.audio.io.models import AudioData
from brain.runtime import ModelRuntime


class CLAPEmbedding(AudioEmbeddingModel):

    MODEL_NAME = "laion/clap-htsat-unfused"

    def __init__(self, runtime: ModelRuntime | None = None) -> None:
        self._runtime = runtime or ModelRuntime.shared()

    @property
    def _audio_assets(self):
        return self._runtime.load(
            model_name=self.MODEL_NAME,
            model_cls=ClapAudioModelWithProjection,
            processor_cls=ClapProcessor,
        )

    @property
    def _text_assets(self):
        return self._runtime.load(
            model_name=self.MODEL_NAME,
            model_cls=ClapModel,
            processor_cls=ClapProcessor,
        )

    @property
    def name(self) -> str:

        return "clap"

    @property
    def dimension(self) -> int:

        return 512

    @property
    def capability(self) -> EmbeddingCapability:

        return EmbeddingCapability(
            backend="transformers",
            device=str(self._audio_assets.device),
        )

    @torch.inference_mode()
    def encode_audio(
        self,
        audio: AudioData,
    ) -> np.ndarray:

        processor = self._audio_assets.processor

        model = self._audio_assets.model

        inputs = processor(
            audio=audio.samples,
            sampling_rate=audio.metadata.sample_rate,
            return_tensors="pt",
        )

        inputs = {
            k: v.to(self._audio_assets.device)
            for k, v in inputs.items()
        }

        outputs = model(**inputs)

        embedding = torch.nn.functional.normalize(
            outputs.audio_embeds,
            dim=-1,
        )

        return embedding.squeeze(0).float().cpu().numpy()

    @torch.inference_mode()
    def encode_text(
        self,
        text: str | list[str],
    ) -> np.ndarray:

        if isinstance(text, str):
            text = [text]

        processor = self._text_assets.processor

        model = self._text_assets.model

        inputs = processor(
            text=text,
            return_tensors="pt",
            padding=True,
        )

        inputs = {
            k: v.to(self._text_assets.device)
            for k, v in inputs.items()
        }

        outputs = model.get_text_features(**inputs)

        outputs = torch.nn.functional.normalize(
            outputs,
            dim=-1,
        )

        return outputs.squeeze(0).float().cpu().numpy()

    def encode(
        self,
        audio: AudioData,
    ) -> np.ndarray:

        return self.encode_audio(audio)
