from __future__ import annotations

from pathlib import Path

from .engine import ReferenceEngine
from .reasoner import ReferenceReasoner
from .report_builder import ReferenceReportBuilder
from .models import ReferenceReport


class ReferencePipeline:
    """
    SoundBrain Reference Intelligence Pipeline

    Pipeline

        Reference Audio
                │
                ▼
          Audio Analysis
                │
                ▼
        Metric Comparison
                │
                ▼
      Engineering Comparison
                │
                ▼
      AI Engineering Reasoning
                │
                ▼
         Professional Report
                │
                ▼
          JSON / Markdown
    """

    def __init__(
        self,
        engine: ReferenceEngine | None = None,
        reasoner: ReferenceReasoner | None = None,
        report_builder: ReferenceReportBuilder | None = None,
    ) -> None:

        self.engine = (
            engine
            or ReferenceEngine()
        )

        self.reasoner = (
            reasoner
            or ReferenceReasoner()
        )

        self.report_builder = (
            report_builder
            or ReferenceReportBuilder()
        )

    def run(
        self,
        reference_audio: str | Path,
        current_audio: str | Path,
        output_directory: str | Path | None = None,
    ) -> ReferenceReport:

        report = self.engine.compare_files(
            reference_audio,
            current_audio,
        )

        report.comparison = self.reasoner.reason(
            report.comparison,
        )

        if output_directory is not None:

            output_directory = Path(
                output_directory,
            )

            output_directory.mkdir(
                parents=True,
                exist_ok=True,
            )

            self.report_builder.save_json(
                report,
                output_directory
                / "reference_report.json",
            )

            self.report_builder.save_markdown(
                report,
                output_directory
                / "reference_report.md",
            )

        return report

    def compare(
        self,
        reference_audio: str | Path,
        current_audio: str | Path,
    ) -> ReferenceReport:

        return self.run(
            reference_audio=reference_audio,
            current_audio=current_audio,
        )

    def compare_and_export(
        self,
        reference_audio: str | Path,
        current_audio: str | Path,
        output_directory: str | Path,
    ) -> ReferenceReport:

        return self.run(
            reference_audio=reference_audio,
            current_audio=current_audio,
            output_directory=output_directory,
        )