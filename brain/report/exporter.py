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
            "plugin_intelligence": self._serialize_plugin_intelligence(report.plugin_intelligence),
            "recommendations": report.recommendations,
            "summary": report.ai_summary,
        }

    def _serialize_plugin_intelligence(
        self,
        plugin_result,
    ) -> dict | None:
        if plugin_result is None:
            return None

        return {
            "goals": [
                {
                    "id": goal.id,
                    "description": goal.description,
                    "target": goal.target,
                    "root_cause": goal.root_cause,
                    "action": goal.action,
                    "confidence": goal.confidence,
                }
                for goal in plugin_result.goals
            ],
            "steps": [
                {
                    "order": step.order,
                    "plugin_category": step.plugin_category,
                    "plugin_type": step.plugin_type,
                    "suggestion": step.suggestion,
                    "estimated_impact": step.estimated_impact,
                    "confidence": step.confidence,
                    "goal": {
                        "id": step.goal.id,
                        "description": step.goal.description,
                        "target": step.goal.target,
                        "action": step.goal.action,
                    },
                    "parameter_recommendations": [
                        {
                            "name": param.name,
                            "value": param.value,
                            "unit": param.unit,
                            "range_min": param.range_min,
                            "range_max": param.range_max,
                            "confidence": param.confidence,
                            "reason": param.reason,
                        }
                        for param in step.parameter_recommendations
                    ],
                    "plugin_options": [
                        {
                            "brand": option.brand,
                            "name": option.name,
                            "formats": option.formats,
                            "category": option.category,
                            "identifier": option.identifier,
                        }
                        for option in step.plugin_options
                    ],
                }
                for step in plugin_result.steps
            ],
            "explanations": plugin_result.explanations,
            "confidence_scores": plugin_result.confidence_scores,
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
