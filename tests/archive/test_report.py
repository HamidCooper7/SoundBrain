from brain.pipeline import analyze_audio
from brain.analysis.engineer import engineer_report
from brain.diagnosis.diagnosis import diagnose
from brain.recommendation.recommendation import recommend
from brain.report.report import build_report

results = analyze_audio("tests/audio.wav")

engineer = engineer_report(results)

diagnosis = diagnose(results)

recommendations = recommend(diagnosis)

print(

    build_report(

        engineer,

        diagnosis,

        recommendations

    )

)