from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Severity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Category(str, Enum):
    FREQUENCY = "frequency"
    DYNAMICS = "dynamics"
    STEREO = "stereo"
    LOUDNESS = "loudness"
    TRANSIENT = "transient"
    PHASE = "phase"
    TONAL = "tonal"
    CLIPPING = "clipping"
    ARTIFACT = "artifact"
    SEMANTIC = "semantic"


@dataclass(slots=True)
class ReferenceMetric:

    name: str

    reference: float

    current: float

    difference: float

    unit: str

    tolerance: float

    passed: bool


@dataclass(slots=True)
class EngineerDecision:

    title: str

    description: str

    category: Category

    severity: Severity

    confidence: float

    recommendation: str

    plugin: str | None = None

    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class BandDifference:

    band: str

    start_hz: float

    end_hz: float

    reference_energy: float

    current_energy: float

    difference_db: float

    severity: Severity


@dataclass(slots=True)
class ReferenceComparison:

    similarity: float

    confidence: float

    frequency_score: float

    dynamic_score: float

    stereo_score: float

    loudness_score: float

    transient_score: float

    phase_score: float

    tonal_score: float

    semantic_score: float

    band_differences: list[BandDifference]

    engineer_decisions: list[EngineerDecision]

    metrics: list[ReferenceMetric]


@dataclass(slots=True)
class ReferenceReport:

    comparison: ReferenceComparison

    summary: str

    strengths: list[str]

    weaknesses: list[str]

    priorities: list[str]

    next_actions: list[str]