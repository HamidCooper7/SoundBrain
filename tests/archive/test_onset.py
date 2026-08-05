from brain.audio.analysis.onset import OnsetAnalysis
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

onsets = OnsetAnalysis().analyze(audio)

print("Onsets:", len(onsets))

print(onsets[:20])