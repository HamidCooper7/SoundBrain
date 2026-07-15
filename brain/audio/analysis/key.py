from __future__ import annotations

import librosa
import numpy as np

from brain.audio.analysis.base import BaseAnalyzer
from brain.audio.io.models import AudioData


class KeyAnalysis(BaseAnalyzer):

    KEYS = (
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B",
    )

    def analyze(
        self,
        audio: AudioData,
    ) -> str:

        samples = self.prepare_samples(audio).astype(np.float32)

        chroma = librosa.feature.chroma_stft(
            y=samples,
            sr=audio.metadata.sample_rate,
        )

        chroma_mean = np.mean(
            chroma,
            axis=1,
        )

        index = int(
            np.argmax(chroma_mean)
        )

        return self.KEYS[index]