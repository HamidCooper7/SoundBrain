from __future__ import annotations

import numpy as np

from brain.audio.analysis.base import BaseAnalyzer
from brain.audio.io.models import AudioData


class DynamicRangeAnalysis(BaseAnalyzer):

    def analyze(
        self,
        audio: AudioData,
    ) -> float:

        samples = self.prepare_samples(audio).astype(np.float32)

        peak = np.max(np.abs(samples))

        rms = np.sqrt(
            np.mean(
                samples ** 2
            )
        )

        if peak <= 0.0 or rms <= 0.0:
            return 0.0

        peak_db = 20.0 * np.log10(peak)

        rms_db = 20.0 * np.log10(rms)

        return float(
            peak_db - rms_db
        )