from __future__ import annotations

from pathlib import Path

from brain.audio.analysis.analyzer import AudioAnalyzer
from brain.audio.io.loader import AudioLoader
from brain.audio.io.models import AudioData
from brain.engineering.engine import EngineeringEngine

from .comparator import ReferenceComparator
from .models import ReferenceReport


class ReferenceService:

    """
    Reference Intelligence V1

    Workflow

    Reference Audio
            │
            ▼
       Audio Analysis

    Current Audio
            │
            ▼
       Audio Analysis

            ▼

      Metric Comparison

            ▼

    Engineering Decisions

            ▼

      Reference Report
    """

    def __init__(
        self,
        loader: AudioLoader | None = None,
        analyzer: AudioAnalyzer | None = None,
        engineering: EngineeringEngine | None = None,
        comparator: ReferenceComparator | None = None,
    ) -> None:

        self.loader = loader or AudioLoader()

        self.analyzer = analyzer or AudioAnalyzer()

        self.engineering = (
            engineering
            or EngineeringEngine()
        )

        self.comparator = (
            comparator
            or ReferenceComparator()
        )

    def compare_files(
        self,
        reference_audio: str | Path,
        current_audio: str | Path,
    ) -> ReferenceReport:

        reference = self.loader.load(
            reference_audio
        )

        current = self.loader.load(
            current_audio
        )

        return self.compare(
            reference,
            current,
        )

    def compare(
        self,
        reference: AudioData,
        current: AudioData,
    ) -> ReferenceReport:

        reference_metrics = (
            self.analyzer.analyze(
                reference
            )
        )

        current_metrics = (
            self.analyzer.analyze(
                current
            )
        )

        comparison = (
            self.comparator.compare_metrics(
                reference_metrics,
                current_metrics,
            )
        )

        engineering_result = (
            self.engineering.process(
                comparison.metrics
            )
        )

        summary = self._build_summary(
            comparison.similarity
        )

        strengths = []

        weaknesses = []

        priorities = []

        next_actions = []

        for decision in comparison.engineer_decisions:

            priorities.append(
                decision.title
            )

            next_actions.append(
                decision.recommendation
            )

        if comparison.similarity >= 90:

            strengths.append(
                "Reference quality is very close."
            )

        elif comparison.similarity >= 75:

            strengths.append(
                "Overall mix balance is acceptable."
            )

            weaknesses.append(
                "Fine tuning recommended."
            )

        else:

            weaknesses.append(
                "Major engineering differences detected."
            )

        if hasattr(
            engineering_result,
            "recommendations",
        ):

            for recommendation in engineering_result.recommendations:

                text = getattr(
                    recommendation,
                    "text",
                    None,
                )

                if text:

                    next_actions.append(
                        text
                    )

        return ReferenceReport(
            comparison=comparison,
            summary=summary,
            strengths=strengths,
            weaknesses=weaknesses,
            priorities=priorities,
            next_actions=next_actions,
        )

    def _build_summary(
        self,
        similarity: float,
    ) -> str:

        if similarity >= 95:

            return (
                "Reference match is excellent."
            )

        if similarity >= 90:

            return (
                "Reference match is very good."
            )

        if similarity >= 80:

            return (
                "Reference match is good with minor improvements required."
            )

        if similarity >= 70:

            return (
                "Reference match is moderate. Engineering adjustments are recommended."
            )

        return (
            "Reference differs significantly from the target mix."
        )