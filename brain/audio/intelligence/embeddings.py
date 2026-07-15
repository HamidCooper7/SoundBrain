from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

import numpy as np
import torch
import torchaudio

from transformers import (
    ClapModel,
    ClapProcessor,
)


class AudioEmbeddingModel(ABC):

    @abstractmethod
    def encode(
        self,
        audio,
    ) -> list[float]:
        ...


class CLAPAudioEmbeddingModel(
    AudioEmbeddingModel
):

    MODEL_PATH = Path(
        r"E:\SoundBrain\models\clap-htsat-unfused"
    )

    TARGET_SAMPLE_RATE = 48000


    def __init__(
        self,
        device: str | None = None,
    ) -> None:


        self.device = (
            device
            or (
                "cuda"
                if torch.cuda.is_available()
                else "cpu"
            )
        )


        self.processor = ClapProcessor.from_pretrained(
            str(self.MODEL_PATH),
            local_files_only=True,
        )


        self.model = ClapModel.from_pretrained(
            str(self.MODEL_PATH),
            local_files_only=True,
        )


        self.model.to(
            self.device
        )


        self.model.eval()



    def _prepare_audio(
        self,
        samples,
        sample_rate: int,
    ):


        waveform = np.asarray(
            samples,
            dtype=np.float32,
        )


        if waveform.ndim > 1:

            waveform = np.mean(
                waveform,
                axis=1,
            )


        if sample_rate != self.TARGET_SAMPLE_RATE:

            tensor = torch.tensor(
                waveform,
                dtype=torch.float32,
            )


            tensor = tensor.unsqueeze(0)


            resampler = torchaudio.transforms.Resample(
                orig_freq=sample_rate,
                new_freq=self.TARGET_SAMPLE_RATE,
            )


            tensor = resampler(
                tensor
            )


            waveform = (
                tensor
                .squeeze(0)
                .numpy()
            )


        return waveform



    def encode(
        self,
        audio,
    ) -> list[float]:


        waveform = self._prepare_audio(
            audio.samples,
            audio.metadata.sample_rate,
        )


        inputs = self.processor(
            audio=[
                waveform
            ],
            sampling_rate=self.TARGET_SAMPLE_RATE,
            return_tensors="pt",
        )


        inputs = {
            key: value.to(
                self.device
            )
            for key, value in inputs.items()
        }


        with torch.no_grad():

            embedding = (
                self.model.get_audio_features(
                    **inputs
                )
            )


        return (
            embedding
            .squeeze(0)
            .cpu()
            .tolist()
        )



    def encode_text(
        self,
        texts: list[str],
    ) -> list[list[float]]:


        inputs = self.processor(
            text=texts,
            return_tensors="pt",
            padding=True,
        )


        inputs = {
            key: value.to(
                self.device
            )
            for key, value in inputs.items()
        }


        with torch.no_grad():

            embeddings = (
                self.model.get_text_features(
                    **inputs
                )
            )


        return (
            embeddings
            .cpu()
            .tolist()
        )