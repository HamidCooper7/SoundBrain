from __future__ import annotations

import librosa
import numpy as np

from brain.audio.analysis.base import BaseAnalyzer
from brain.audio.io.models import AudioData


class ZeroCrossingRateAnalysis(BaseAnalyzer):

    def analyze(
        self,
        audio: AudioData,
    ) -> float:

        samples = self.prepare_samples(audio).astype(np.float32)

        zcr = librosa.feature.zero_crossing_rate(
            samples,
        )

        return float(
            np.mean(zcr)
        )