from brain.audio.analysis.phase import PhaseCorrelationAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Phase Correlation:",
    PhaseCorrelationAnalysis().analyze(audio),
)