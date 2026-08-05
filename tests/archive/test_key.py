from brain.audio.analysis.key import KeyAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

print(
    "Detected Key:",
    KeyAnalysis().analyze(audio),
)