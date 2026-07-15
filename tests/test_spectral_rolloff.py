from brain.audio.analysis.spectral_rolloff import SpectralRolloffAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Spectral Rolloff:",
    SpectralRolloffAnalysis().analyze(audio),
)