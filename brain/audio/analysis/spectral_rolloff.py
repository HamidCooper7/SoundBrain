from __future__ import annotations

import librosa
import numpy as np

from brain.audio.analysis.base import BaseAnalyzer
from brain.audio.io.models import AudioData


class SpectralRolloffAnalysis(BaseAnalyzer):

    def analyze(
        self,
        audio: AudioData,
    ) -> float:

        samples = self.prepare_samples(audio).astype(np.float32)

        rolloff = librosa.feature.spectral_rolloff(
            y=samples,
            sr=audio.metadata.sample_rate,
        )

        return float(
            np.mean(rolloff)
        )