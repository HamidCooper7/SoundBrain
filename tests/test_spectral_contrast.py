from brain.audio.analysis.spectral_contrast import SpectralContrastAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Spectral Contrast:",
    SpectralContrastAnalysis().analyze(audio),
)