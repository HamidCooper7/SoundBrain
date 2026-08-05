from brain.audio.analysis import AudioAnalyzer
from brain.audio.engineer import (
    AudioEngineer,
    EngineerReport,
)
from brain.audio.io import AudioIOService


audio = AudioIOService().load(
    "music/test.wav"
)

analysis = AudioAnalyzer().analyze(
    audio
)

engineer = AudioEngineer().analyze(
    analysis
)

print(
    EngineerReport().build(
        engineer
    )
)