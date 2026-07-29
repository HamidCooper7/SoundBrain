from __future__ import annotations

from pathlib import Path

import pytest

from brain.audio.pipeline import AudioPipeline


AUDIO_PATH = Path("tests/assets/test.wav")
FALLBACK_PATH = Path("tests/audio.wav")


@pytest.mark.skipif(
    not AUDIO_PATH.exists() and not FALLBACK_PATH.exists(),
    reason="No test audio file is available",
)
def test_audio_pipeline_index_and_search():
    audio_path = AUDIO_PATH if AUDIO_PATH.exists() else FALLBACK_PATH

    pipeline = AudioPipeline()

    pipeline.index(
        audio_path,
        audio_id="song_001",
        metadata={
            "title": "Test Song",
            "artist": "SoundBrain",
        },
        document="First indexed audio",
    )

    result = pipeline.search(audio_path)

    assert len(result.ids) >= 1, "Search should return at least one indexed audio"
    assert "song_001" in result.ids, "Indexed audio should be found by identity search"
