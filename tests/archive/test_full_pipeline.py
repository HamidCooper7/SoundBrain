from __future__ import annotations


from brain.audio.analysis import AudioAnalyzer
from brain.audio.context import AudioContextDetector
from brain.audio.engineer import AudioEngineer
from brain.audio.io import AudioIOService


from brain.reasoning import (
    ReasoningContext,
    ReasoningEngine,
)


from brain.report import (
    ReportBuilder,
)



def main():


    audio = AudioIOService().load(
        "music/full-mix.mp3"
    )


    analysis = AudioAnalyzer().analyze(
        audio
    )


    context = AudioContextDetector().detect(
        analysis,
        audio,
    )


    engineer = AudioEngineer().analyze(
        analysis,
        context=context,
    )



    reasoning_context = ReasoningContext(

        analysis=analysis,

        engineer=engineer,

        audio_context=context,

        question="Analyze this audio professionally."

    )



    reasoning = ReasoningEngine()


    result = reasoning.ask(
        reasoning_context
    )



    report = ReportBuilder().build(

        analysis,

        engineer,

        context,

        result.answer,

    )



    print()

    print(
        "========== FINAL SOUNDBRAIN REPORT =========="
    )


    print()

    print(
        f"Audio Type: {report.audio_type}"
    )


    print(
        f"Source: {report.source_type}"
    )


    print(
        f"Score: {report.score}/100"
    )


    print()


    print(
        "Semantic Understanding:"
    )


    for item in report.semantic_labels:

        print(
            f"- {item}"
        )


    print()


    print(
        "Strengths:"
    )


    for item in report.strengths:

        print(
            f"- {item}"
        )


    print()


    print(
        "Issues:"
    )


    for issue in report.issues:

        print(
            f"[{issue.severity}] {issue.title}"
        )

        print(
            issue.description
        )


    print()


    print(
        "Recommendations:"
    )


    for item in report.recommendations:

        print(
            f"- {item}"
        )


    print()


    print(
        "========== AI SUMMARY =========="
    )


    print(
        report.ai_summary
    )



if __name__ == "__main__":

    main()