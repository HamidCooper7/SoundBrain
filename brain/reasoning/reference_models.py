from __future__ import annotations

from dataclasses import dataclass

from brain.audio.analysis.models import AnalysisResult
from brain.audio.comparison.report_models import ComparisonReport


@dataclass(slots=True)
class ReferenceReasoningContext:
    """
    Context for reference-vs-current reasoning.
    """

    reference: AnalysisResult

    current: AnalysisResult

    comparison: ComparisonReport

    question: str