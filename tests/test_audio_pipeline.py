from pathlib import Path

from brain.audio.pipeline import AudioPipeline


pipeline = AudioPipeline()

pipeline.index(
    Path("tests/assets/test.wav"),
    audio_id="song_001",
    metadata={
        "title": "Test Song",
        "artist": "SoundBrain",
    },
    document="First indexed audio",
)

result = pipeline.search(
    Path("tests/assets/test.wav"),
)

print(result)