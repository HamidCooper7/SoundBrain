from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from brain.audio.analysis.models import AnalysisResult
from brain.audio.io.models import AudioData, AudioMetadata
from brain.reference.models import (
    Category,
    DecisionType,
    EngineerDecision,
    ReferenceIntent,
    SegmentDeviation,
    Severity,
)
from brain.reference.reasoner import ReferenceReasoner
from brain.reference.service import ReferenceService

AUDIO_PATH = Path("tests/audio.wav")


def _analysis(
    *,
    lufs: float = -14.0,
    peak: float = -1.0,
    rms: float = -20.0,
) -> AnalysisResult:
    return AnalysisResult(
        tempo=120.0,
        pitch=440.0,
        key="C",
        lufs=lufs,
        peak=peak,
        rms=rms,
        dynamic_range=8.0,
        crest_factor=10.0,
        stereo_width=0.8,
        phase=0.1,
        spectral_centroid=2000.0,
        spectral_bandwidth=1500.0,
        spectral_rolloff=8000.0,
        spectral_flatness=0.2,
        spectral_contrast=15.0,
        zero_crossing_rate=0.05,
        mfcc=[0.0] * 13,
        chroma=[0.0] * 12,
        onset_count=100,
    )


@dataclass
class FakeEngineeringEngine:

    def process(self, metrics):
        return type(
            "Result",
            (),
            {"recommendations": []},
        )()


@dataclass
class FakeAudioAnalyzer:

    results: dict[str, AnalysisResult]

    def analyze(self, audio: AudioData) -> AnalysisResult:
        return self.results[audio.metadata.filename]


def _audio_data(name: str = "audio.wav", duration: float = 10.0) -> AudioData:
    return AudioData(
        samples=None,
        metadata=AudioMetadata(
            path=Path("tests") / name,
            filename=name,
            extension="wav",
            format="wav",
            codec=None,
            sample_rate=44100,
            channels=2,
            duration=duration,
            bit_depth=16,
            file_size=1000,
        ),
    )


def test_multi_reference_computes_similarity_and_variance():
    ref_a = _analysis(lufs=-12.0, peak=-1.0)
    ref_b = _analysis(lufs=-10.0, peak=-2.0)
    ref_c = _analysis(lufs=-14.0, peak=-3.0)
    current = _analysis(lufs=-16.0, peak=-4.0)

    service = ReferenceService(
        analyzer=FakeAudioAnalyzer(
            {
                "reference_a.wav": ref_a,
                "reference_b.wav": ref_b,
                "reference_c.wav": ref_c,
                "current.wav": current,
            }
        ),
        engineering=FakeEngineeringEngine(),
    )

    report = service.compare_multiple(
        references=[
            _audio_data("reference_a.wav"),
            _audio_data("reference_b.wav"),
            _audio_data("reference_c.wav"),
        ],
        current=_audio_data("current.wav"),
        reference_paths=["reference_a.wav", "reference_b.wav", "reference_c.wav"],
    )

    assert report.comparison.references == [
        "reference_a.wav",
        "reference_b.wav",
        "reference_c.wav",
    ]
    assert len(report.comparison.reference_similarities) == 3
    assert all(0.0 <= sim <= 100.0 for sim in report.comparison.reference_similarities.values())

    lufs_metric = next(metric for metric in report.comparison.metrics if metric.name == "lufs")
    assert lufs_metric.reference == -12.0
    assert report.comparison.metric_variance["lufs"] > 0.0
    assert report.comparison.segment_deviations


def test_segment_deviation_structure_for_failed_metric():
    reference = _analysis(lufs=-14.0)
    current = _analysis(lufs=-22.0)

    service = ReferenceService(
        analyzer=FakeAudioAnalyzer(
            {
                "reference.wav": reference,
                "current.wav": current,
            }
        ),
        engineering=FakeEngineeringEngine(),
    )

    report = service.compare(
        reference=_audio_data("reference.wav", duration=15.0),
        current=_audio_data("current.wav", duration=15.0),
    )

    assert report.comparison.segment_deviations
    first = report.comparison.segment_deviations[0]
    assert isinstance(first, SegmentDeviation)
    assert first.start_time == 0.0
    assert first.end_time == 15.0
    assert first.metric
    assert first.severity


def test_reference_intent_categorization_with_focus_areas():
    reasoner = ReferenceReasoner()

    decision = EngineerDecision(
        title="Loudness Adjustment",
        description="LUFS differs.",
        category=Category.LOUDNESS,
        severity=Severity.MEDIUM,
        confidence=0.90,
        recommendation="Adjust limiter.",
    )

    intent = ReferenceIntent(
        genre="pop",
        target="streaming",
        focus_areas=["loudness"],
    )

    categorized = reasoner._categorize(decision, intent=intent)

    assert categorized.decision_type == DecisionType.STYLISTIC_DIFFERENCE
    assert categorized.confidence > decision.confidence


def test_reference_intent_categorization_without_focus():
    reasoner = ReferenceReasoner()

    decision = EngineerDecision(
        title="Phase Issue",
        description="Phase differs.",
        category=Category.PHASE,
        severity=Severity.HIGH,
        confidence=0.95,
        recommendation="Check mono.",
    )

    categorized = reasoner._categorize(decision, intent=None)

    assert categorized.decision_type == DecisionType.TECHNICAL_ISSUE


def test_low_confidence_decision_is_insufficient_evidence():
    reasoner = ReferenceReasoner()

    decision = EngineerDecision(
        title="Transient",
        description="Maybe different.",
        category=Category.TRANSIENT,
        severity=Severity.LOW,
        confidence=0.80,
        recommendation="Investigate.",
    )

    categorized = reasoner._categorize(decision, intent=None)

    assert categorized.decision_type == DecisionType.INSUFFICIENT_EVIDENCE
