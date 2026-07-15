from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Issue:

    title: str

    severity: str

    description: str

    recommendation: str


@dataclass(slots=True)
class Recommendation:

    title: str

    reason: str

    action: str


@dataclass(slots=True)
class EngineerResult:

    score: float

    strengths: list[str] = field(default_factory=list)

    issues: list[Issue] = field(default_factory=list)

    recommendations: list[Recommendation] = field(default_factory=list)