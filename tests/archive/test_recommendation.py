from brain.pipeline import analyze_audio
from brain.diagnosis.diagnosis import diagnose
from brain.recommendation.recommendation import recommend

results = analyze_audio("tests/audio.wav")

diagnosis = diagnose(results)

recommendations = recommend(diagnosis)

print(recommendations)