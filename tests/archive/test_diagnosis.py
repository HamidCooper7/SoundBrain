from brain.pipeline import analyze_audio
from brain.diagnosis.diagnosis import diagnose

results = analyze_audio("tests/audio.wav")

print(diagnose(results))