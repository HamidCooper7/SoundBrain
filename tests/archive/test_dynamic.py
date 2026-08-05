from brain.audio.analysis.crest_factor import CrestFactorAnalysis
from brain.audio.analysis.dynamic_range import DynamicRangeAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Dynamic Range:",
    DynamicRangeAnalysis().analyze(audio),
)

print(
    "Crest Factor:",
    CrestFactorAnalysis().analyze(audio),
)