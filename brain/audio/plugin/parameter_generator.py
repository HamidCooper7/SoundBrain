from __future__ import annotations

from .models import ParameterRecommendation, ProcessingGoal
from .taxonomy import (
    CATEGORY_COMPRESSOR,
    CATEGORY_EQ,
    CATEGORY_IMAGER,
    CATEGORY_LIMITER,
    CATEGORY_SATURATION,
    CATEGORY_TRANSIENT_SHAPER,
)


class ParameterGenerator:
    """Rule-based parameter recommendations for a processing goal and category."""

    def generate(
        self,
        goal: ProcessingGoal,
        category: str,
    ) -> list[ParameterRecommendation]:
        if category == CATEGORY_EQ:
            return self._eq_parameters(goal)
        if category == CATEGORY_COMPRESSOR:
            return self._compressor_parameters(goal)
        if category == CATEGORY_LIMITER:
            return self._limiter_parameters(goal)
        if category == CATEGORY_IMAGER:
            return self._imager_parameters(goal)
        if category == CATEGORY_TRANSIENT_SHAPER:
            return self._transient_parameters(goal)
        if category == CATEGORY_SATURATION:
            return self._saturation_parameters(goal)
        return []

    def _eq_parameters(self, goal: ProcessingGoal) -> list[ParameterRecommendation]:
        return [
            ParameterRecommendation(
                name="frequency",
                value=3000.0,
                unit="Hz",
                range_min=20.0,
                range_max=20000.0,
                confidence=0.85,
                reason="Target 2–5 kHz harshness region",
            ),
            ParameterRecommendation(
                name="gain",
                value=-2.0,
                unit="dB",
                range_min=-24.0,
                range_max=24.0,
                confidence=0.80,
                reason="Gentle reduction to reduce harshness",
            ),
            ParameterRecommendation(
                name="q",
                value=1.4,
                range_min=0.1,
                range_max=10.0,
                confidence=0.85,
                reason="Moderate bandwidth for surgical cut",
            ),
        ]

    def _compressor_parameters(
        self,
        goal: ProcessingGoal,
    ) -> list[ParameterRecommendation]:
        return [
            ParameterRecommendation(
                name="threshold",
                value=-18.0,
                unit="dB",
                range_min=-60.0,
                range_max=0.0,
                confidence=0.82,
                reason="Control peaks without crushing the mix",
            ),
            ParameterRecommendation(
                name="ratio",
                value=3.0,
                unit=":1",
                range_min=1.0,
                range_max=20.0,
                confidence=0.80,
                reason="Moderate gain reduction for dynamics",
            ),
            ParameterRecommendation(
                name="attack",
                value=10.0,
                unit="ms",
                range_min=0.01,
                range_max=1000.0,
                confidence=0.78,
                reason="Preserve transients",
            ),
            ParameterRecommendation(
                name="release",
                value=100.0,
                unit="ms",
                range_min=1.0,
                range_max=5000.0,
                confidence=0.78,
                reason="Natural recovery",
            ),
        ]

    def _limiter_parameters(
        self,
        goal: ProcessingGoal,
    ) -> list[ParameterRecommendation]:
        return [
            ParameterRecommendation(
                name="ceiling",
                value=-1.0,
                unit="dB",
                range_min=-3.0,
                range_max=-0.1,
                confidence=0.88,
                reason="Prevent inter-sample peaks for streaming",
            ),
            ParameterRecommendation(
                name="release",
                value=50.0,
                unit="ms",
                range_min=1.0,
                range_max=5000.0,
                confidence=0.80,
                reason="Transparent loudness target",
            ),
            ParameterRecommendation(
                name="lookahead",
                value=5.0,
                unit="ms",
                range_min=0.0,
                range_max=20.0,
                confidence=0.75,
                reason="Catch peaks before they clip",
            ),
        ]

    def _imager_parameters(
        self,
        goal: ProcessingGoal,
    ) -> list[ParameterRecommendation]:
        return [
            ParameterRecommendation(
                name="width",
                value=125.0,
                unit="%",
                range_min=0.0,
                range_max=200.0,
                confidence=0.75,
                reason="Widen narrow stereo image",
            ),
            ParameterRecommendation(
                name="mono_below_hz",
                value=120.0,
                unit="Hz",
                range_min=20.0,
                range_max=500.0,
                confidence=0.70,
                reason="Improve mono compatibility below bass region",
            ),
        ]

    def _transient_parameters(
        self,
        goal: ProcessingGoal,
    ) -> list[ParameterRecommendation]:
        return [
            ParameterRecommendation(
                name="attack",
                value=20.0,
                unit="%",
                range_min=-100.0,
                range_max=100.0,
                confidence=0.75,
                reason="Add punch to dull transients",
            ),
            ParameterRecommendation(
                name="sustain",
                value=-10.0,
                unit="%",
                range_min=-100.0,
                range_max=100.0,
                confidence=0.70,
                reason="Control decay",
            ),
        ]

    def _saturation_parameters(
        self,
        goal: ProcessingGoal,
    ) -> list[ParameterRecommendation]:
        return [
            ParameterRecommendation(
                name="drive",
                value=15.0,
                unit="%",
                range_min=0.0,
                range_max=100.0,
                confidence=0.70,
                reason="Add harmonic warmth",
            ),
            ParameterRecommendation(
                name="mix",
                value=25.0,
                unit="%",
                range_min=0.0,
                range_max=100.0,
                confidence=0.75,
                reason="Blend saturation with dry signal",
            ),
        ]
