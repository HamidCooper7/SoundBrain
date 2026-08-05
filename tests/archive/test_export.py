from __future__ import annotations

import json


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
    ReportExporter,
)



def main() -> None:


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



    reasoning_engine = ReasoningEngine()


    result = reasoning_engine.ask(
        reasoning_context
    )



    report = ReportBuilder().build(

        analysis,

        engineer,

        context,

        result.answer,

    )



    exporter = ReportExporter()



    exporter.save_json(

        report,

        "reports/test_report_v2.json"

    )



    print()

    print(
        "========== EXPORT COMPLETE =========="
    )


    print(
        "File: reports/test_report_v2.json"
    )



    print()

    print(
        "========== JSON PREVIEW =========="
    )



    data = exporter.to_dict(
        report
    )



    print(
        json.dumps(

            data,

            indent=4,

            ensure_ascii=False,

        )
    )



if __name__ == "__main__":

    main()