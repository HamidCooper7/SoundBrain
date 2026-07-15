from __future__ import annotations

from dataclasses import dataclass, field



@dataclass
class ReportIssue:

    title: str

    severity: str

    description: str

    recommendation: str



@dataclass
class SoundBrainReport:


    audio_type: str


    source_type: str


    instrument: str | None


    is_full_mix: bool


    confidence: float



    semantic_labels: list[str] = field(
        default_factory=list
    )


    score: float = 0.0


    strengths: list[str] = field(
        default_factory=list
    )


    issues: list[ReportIssue] = field(
        default_factory=list
    )


    recommendations: list[str] = field(
        default_factory=list
    )


    ai_summary: str = ""