from brain.audio.analysis.zero_crossing import ZeroCrossingRateAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Zero Crossing Rate:",
    ZeroCrossingRateAnalysis().analyze(audio),
)