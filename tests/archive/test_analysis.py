from brain.audio.analysis import AudioAnalyzer
from brain.audio.analysis.report import AnalysisReport
from brain.audio.io import AudioIOService

audio = AudioIOService().load("music/test.wav")

analysis = AudioAnalyzer().analyze(audio)

print(
    AnalysisReport().build(
        analysis
    )
)