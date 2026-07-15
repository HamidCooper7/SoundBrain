from brain.audio.analysis import AudioAnalyzer
from brain.audio.context import AudioContextDetector
from brain.audio.engineer import AudioEngineer
from brain.audio.io import AudioIOService

from brain.reasoning import (
    ReasoningContext,
    ReasoningEngine,
)

from brain.audio.engineer.report import EngineerReport
from brain.audio.analysis.report import AnalysisReport



def main() -> None:


    audio = AudioIOService().load(
        "music/full-mix.mp3",
    )


    analysis = AudioAnalyzer().analyze(
        audio,
    )


    audio_context = AudioContextDetector().detect(
        analysis,
        audio,
    )


    engineer = AudioEngineer().analyze(
        analysis,
        context=audio_context,
    )


    reasoning_context = ReasoningContext(
        analysis=analysis,
        engineer=engineer,
        audio_context=audio_context,
        question="Is this audio too loud?",
    )



    print()

    print(
        "========== AUDIO CONTEXT =========="
    )


    print(
        f"Type        : {audio_context.audio_type}"
    )


    print(
        f"Source      : {audio_context.source_type}"
    )


    print(
        f"Instrument  : {audio_context.instrument}"
    )


    print(
        f"Full Mix    : {audio_context.is_full_mix}"
    )


    print(
        f"Confidence  : {audio_context.confidence:.2f}"
    )



    print()

    print(
        "Semantic Labels:"
    )


    for label in audio_context.semantic_labels:

        print(
            f"- {label.name}: {label.confidence:.2f}"
        )



    print()

    print(
        "Detected Elements:"
    )


    for element in audio_context.detected_elements:

        print(
            f"- {element}"
        )



    print()

    print(
        "Notes:"
    )


    for note in audio_context.notes:

        print(
            f"- {note}"
        )



    print()

    print(
        "========== ENGINEER OBJECT =========="
    )


    print(
        engineer
    )



    print()

    print(
        "========== ENGINEER REPORT =========="
    )


    report = EngineerReport().build(
        engineer,
    )


    print(
        report
    )



    print()

    print(
        "========== ANALYSIS =========="
    )


    analysis_report = AnalysisReport().build(
        analysis,
    )


    print(
        analysis_report
    )



    engine = ReasoningEngine()


    result = engine.ask(
        reasoning_context,
    )



    print()

    print(
        "========== QWEN RESPONSE =========="
    )


    print()

    print(
        result.answer
    )



    print()

    print(
        "========== REASONING =========="
    )


    print(
        f"Confidence : {result.confidence:.2f}"
    )


    for item in result.reasoning:

        print(
            f"- {item}"
        )



if __name__ == "__main__":

    main()