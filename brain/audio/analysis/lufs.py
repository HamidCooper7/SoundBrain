from __future__ import annotations

import numpy as np
import pyloudnorm as pyln

from brain.audio.io.models import AudioData

from .base import BaseAnalyzer


class LUFSAnalyzer(BaseAnalyzer):
    """
    Computes Integrated Loudness (LUFS)
    using ITU-R BS.1770.
    """

    def analyze(
        self,
        audio: AudioData,
    ) -> float:

        samples = np.asarray(audio.samples)

        meter = pyln.Meter(
            audio.metadata.sample_rate,
        )

        loudness = meter.integrated_loudness(
            samples,
        )

        return float(loudness)
