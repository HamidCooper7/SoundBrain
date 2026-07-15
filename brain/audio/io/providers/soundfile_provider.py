from __future__ import annotations

from pathlib import Path

import soundfile as sf

from brain.audio.io.backend import AudioBackend


class SoundFileProvider(AudioBackend):
    """
    SoundFile backend implementation.
    """

    def load(
        self,
        path: Path,
    ):

        samples, sample_rate = sf.read(
            file=path,
            always_2d=False,
        )

        return {
            "samples": samples,
            "sample_rate": sample_rate,
        }

    def save(
        self,
        data,
        path: Path,
    ) -> None:

        sf.write(
            file=path,
            data=data["samples"],
            samplerate=data["sample_rate"],
        )