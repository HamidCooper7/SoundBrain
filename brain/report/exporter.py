from __future__ import annotations

import json
from pathlib import Path

from .models import SoundBrainReport



class ReportExporter:


    def to_dict(
        self,
        report: SoundBrainReport,
    ) -> dict:


        return {

            "metadata": {

                "audio_type": report.audio_type,

                "source_type": report.source_type,

                "instrument": report.instrument,

                "is_full_mix": report.is_full_mix,

                "confidence": round(
                    report.confidence,
                    2
                ),

            },


            "intelligence": {

                "semantic_labels": [

                    {

                        "label": item.split(":")[0].strip(),

                        "confidence": round(

                            float(
                                item.split(":")[1].strip()
                            ),

                            2

                        ),

                    }

                    for item in report.semantic_labels

                ],

            },


            "engineering": {

                "score": report.score,


                "strengths": report.strengths,


                "issues": [

                    {

                        "title": issue.title,

                        "severity": issue.severity,

                        "description": issue.description,

                        "recommendation": issue.recommendation,

                    }

                    for issue in report.issues

                ],

            },


            "recommendations": report.recommendations,


            "summary": report.ai_summary,

        }



    def save_json(

        self,

        report: SoundBrainReport,

        path: str,

    ) -> None:


        data = self.to_dict(
            report
        )


        Path(path).write_text(

            json.dumps(

                data,

                indent=4,

                ensure_ascii=False,

            ),

            encoding="utf-8"

        )