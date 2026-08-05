from brain.audio.analysis.spectral_centroid import SpectralCentroidAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Spectral Centroid:",
    SpectralCentroidAnalysis().analyze(audio),
)