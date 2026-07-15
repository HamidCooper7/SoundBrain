from brain.pipeline import analyze_audio
from brain.analysis.engineer import engineer_report

results = analyze_audio("tests/audio.wav")

report = engineer_report(results)

print(report)