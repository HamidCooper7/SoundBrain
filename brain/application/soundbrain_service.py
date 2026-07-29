from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from brain.audio.analysis.models import AnalysisResult
from brain.audio.context.models import AudioContext
from brain.audio.engineer.models import EngineerResult
from brain.audio.io.models import AudioData
from brain.reference.models import ReferenceComparison
from brain.report.models import SoundBrainReport


@dataclass(slots=True, frozen=True)
class AnalysisRequest:
    """
    V1 SoundBrain analysis request.

    The deterministic audio review flow is always executed. Optional features
    (reference comparison, LLM reasoning, RAG retrieval) are flag-gated and
    gracefully degrade when disabled or unavailable.
    """

    audio_path: str | Path
    reference_path: str | Path | None = None
    intent: str = ""
    delivery_target: str = ""
    include_reasoning: bool = False
    include_rag: bool = False
    output_path: str | Path | None = None


@dataclass(slots=True)
class AnalysisResponse:
    """
    V1 SoundBrain analysis response.

    Contains the full deterministic pipeline output plus any optional results
    that were successfully produced (e.g. reference comparison).
    """

    audio: AudioData
    analysis: AnalysisResult
    context: AudioContext
    engineering: EngineerResult
    report: SoundBrainReport
    comparison: ReferenceComparison | None = None


class SoundBrainService:
    """
    Single entry point for the V1 SoundBrain workflow.

    The service composes the deterministic ``AudioReviewService`` and optionally
    the ``ReferencePipeline``. Heavy modules are imported inside methods so that
    importing this module does not load torch, transformers, or audio models.
    """

    def __init__(
        self,
        *,
        audio_review_service: Any | None = None,
        reference_pipeline: Any | None = None,
    ) -> None:
        self._audio_review_service = audio_review_service
        self._reference_pipeline = reference_pipeline

    def analyze(
        self,
        request: AnalysisRequest,
    ) -> AnalysisResponse:
        """
        Run the V1 SoundBrain analysis workflow.

        Optional stages are executed only when explicitly requested and only when
        their dependencies are available. A missing optional stage never breaks
        the deterministic report.
        """
        from brain.application.audio_review_service import (
            AudioReviewRequest,
            AudioReviewService,
        )

        review_service = (
            self._audio_review_service
            or AudioReviewService()
        )

        review_request = AudioReviewRequest(
            audio_path=request.audio_path,
            include_semantic_analysis=False,
            summary=request.intent or request.delivery_target or "",
            output_path=request.output_path,
        )
        review_result = review_service.review(review_request)

        comparison = self._run_reference_comparison(request)

        return AnalysisResponse(
            audio=review_result.audio,
            analysis=review_result.analysis,
            context=review_result.context,
            engineering=review_result.engineering,
            report=review_result.report,
            comparison=comparison,
        )

    def _run_reference_comparison(
        self,
        request: AnalysisRequest,
    ) -> ReferenceComparison | None:
        """
        Run the reference comparison pipeline when a reference path is provided.

        Returns ``None`` if no reference path is supplied or if the comparison
        fails. This keeps the deterministic report intact.
        """
        if request.reference_path is None:
            return None

        try:
            from brain.reference.pipeline import ReferencePipeline

            pipeline = self._reference_pipeline or ReferencePipeline()
            report = pipeline.run(
                reference_audio=request.reference_path,
                current_audio=request.audio_path,
            )
            return report.comparison
        except Exception:
            return None
