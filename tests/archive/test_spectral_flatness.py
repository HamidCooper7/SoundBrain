from brain.audio.analysis.spectral_flatness import SpectralFlatnessAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Spectral Flatness:",
    SpectralFlatnessAnalysis().analyze(audio),
)