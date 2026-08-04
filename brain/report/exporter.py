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
                "confidence": round(report.confidence, 2),
                "confidence_scores": report.confidence_scores,
            },
            "intelligence": {
                "semantic_labels": [
                    {
                        "label": item.split(":")[0].strip(),
                        "confidence": round(
                            float(item.split(":")[1].strip()),
                            2,
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
                        "confidence": issue.confidence,
                    }
                    for issue in report.issues
                ],
            },
            "mix_intelligence": {
                "root_causes": [
                    {
                        "symptom": cause.symptom,
                        "likely_causes": cause.likely_causes,
                        "priority": cause.priority,
                        "confidence": cause.confidence,
                    }
                    for cause in report.root_causes
                ],
                "prioritized_issues": [
                    {
                        "title": issue.title,
                        "severity": issue.severity,
                        "priority_score": issue.priority_score,
                        "user_action_order": issue.user_action_order,
                        "category": issue.category,
                        "description": issue.description,
                        "recommendation": issue.recommendation,
                        "confidence": issue.confidence,
                    }
                    for issue in report.prioritized_issues
                ],
                "processing_chain": [
                    {
                        "order": step.order,
                        "target": step.target,
                        "plugin_type": step.plugin_type,
                        "suggestion": step.suggestion,
                        "estimated_impact": step.estimated_impact,
                        "confidence": step.confidence,
                    }
                    for step in report.processing_chain
                ],
                "explanations": report.explanations,
            },
            "recommendations": report.recommendations,
            "summary": report.ai_summary,
        }

    def save_json(
        self,
        report: SoundBrainReport,
        path: str,
    ) -> None:
        data = self.to_dict(report)

        Path(path).write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
