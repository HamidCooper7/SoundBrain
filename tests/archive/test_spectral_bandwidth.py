from brain.audio.analysis.spectral_bandwidth import SpectralBandwidthAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Spectral Bandwidth:",
    SpectralBandwidthAnalysis().analyze(audio),
)