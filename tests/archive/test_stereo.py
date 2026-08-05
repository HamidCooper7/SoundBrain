from brain.audio.analysis.stereo import StereoWidthAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Stereo Width:",
    StereoWidthAnalysis().analyze(audio),
)