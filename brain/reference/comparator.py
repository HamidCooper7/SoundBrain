from __future__ import annotations

from typing import Iterable

from .models import (
    BandDifference,
    Category,
    EngineerDecision,
    ReferenceComparison,
    ReferenceMetric,
    Severity,
)


class ReferenceComparator:

    DEFAULT_TOLERANCE = 1.0

    BAND_LIMITS = (
        ("Sub", 20, 60),
        ("Bass", 60, 120),
        ("Low Mid", 120, 500),
        ("Mid", 500, 2000),
        ("High Mid", 2000, 6000),
        ("High", 6000, 12000),
        ("Air", 12000, 20000),
    )

    def compare_metrics(
        self,
        reference: dict,
        current: dict,
    ) -> ReferenceComparison:

        metrics: list[ReferenceMetric] = []
        decisions: list[EngineerDecision] = []
        bands: list[BandDifference] = []

        scores: list[float] = []

        for key, ref_value in reference.items():

            if key not in current:
                continue

            cur_value = current[key]

            if not isinstance(ref_value, (int, float)):
                continue

            if not isinstance(cur_value, (int, float)):
                continue

            diff = cur_value - ref_value

            passed = abs(diff) <= self.DEFAULT_TOLERANCE

            metrics.append(
                ReferenceMetric(
                    name=key,
                    reference=float(ref_value),
                    current=float(cur_value),
                    difference=float(diff),
                    tolerance=self.DEFAULT_TOLERANCE,
                    passed=passed,
                    unit="",
                )
            )

            similarity = max(
                0.0,
                100.0 - abs(diff) * 10,
            )

            scores.append(similarity)

            severity = self._severity(diff)

            if not passed:

                decisions.append(
                    EngineerDecision(
                        title=f"{key} Adjustment",
                        description=f"{key} differs by {diff:.2f}",
                        category=self._category(key),
                        severity=severity,
                        confidence=0.90,
                        recommendation=self._recommendation(
                            key,
                            diff,
                        ),
                    )
                )

        if "bands" in reference and "bands" in current:

            bands = self._compare_bands(
                reference["bands"],
                current["bands"],
            )

        overall = (
            sum(scores) / len(scores)
            if scores
            else 100.0
        )

        return ReferenceComparison(
            similarity=overall,
            confidence=0.95,
            frequency_score=overall,
            dynamic_score=overall,
            stereo_score=overall,
            loudness_score=overall,
            transient_score=overall,
            phase_score=overall,
            tonal_score=overall,
            semantic_score=overall,
            band_differences=bands,
            engineer_decisions=decisions,
            metrics=metrics,
        )

    def _compare_bands(
        self,
        reference: dict,
        current: dict,
    ) -> list[BandDifference]:

        result = []

        for name, low, high in self.BAND_LIMITS:

            ref = float(reference.get(name, 0.0))
            cur = float(current.get(name, 0.0))

            diff = cur - ref

            result.append(
                BandDifference(
                    band=name,
                    start_hz=low,
                    end_hz=high,
                    reference_energy=ref,
                    current_energy=cur,
                    difference_db=diff,
                    severity=self._severity(diff),
                )
            )

        return result

    def _severity(
        self,
        difference: float,
    ) -> Severity:

        value = abs(difference)

        if value < 1:
            return Severity.INFO

        if value < 2:
            return Severity.LOW

        if value < 4:
            return Severity.MEDIUM

        if value < 6:
            return Severity.HIGH

        return Severity.CRITICAL

    def _category(
        self,
        metric: str,
    ) -> Category:

        metric = metric.lower()

        if "lufs" in metric:
            return Category.LOUDNESS

        if "peak" in metric:
            return Category.LOUDNESS

        if "rms" in metric:
            return Category.DYNAMICS

        if "crest" in metric:
            return Category.DYNAMICS

        if "stereo" in metric:
            return Category.STEREO

        if "phase" in metric:
            return Category.PHASE

        if "transient" in metric:
            return Category.TRANSIENT

        if "freq" in metric:
            return Category.FREQUENCY

        return Category.TONAL

    def _recommendation(
        self,
        metric: str,
        difference: float,
    ) -> str:

        if difference > 0:

            return (
                f"Reduce {metric} "
                f"by approximately {abs(difference):.2f}"
            )

        return (
            f"Increase {metric} "
            f"by approximately {abs(difference):.2f}"
        )