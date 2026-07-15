from __future__ import annotations

from brain.audio.analysis.models import AnalysisResult
from brain.audio.context.models import AudioContext

from .models import (
    Issue,
    Recommendation,
)


class RuleEngine:

    def evaluate(
        self,
        *,
        analysis: AnalysisResult,
        context: AudioContext | None = None,
    ) -> tuple[
        list[str],
        list[Issue],
        list[Recommendation],
        float,
    ]:

        if context and not context.is_full_mix:

            return self._evaluate_stem(
                analysis
            )

        return self._evaluate_mix(
            analysis
        )


    # =====================================
    # Full Mix / Master Rules
    # =====================================

    def _evaluate_mix(
        self,
        analysis: AnalysisResult,
    ):

        strengths = []
        issues = []
        recommendations = []

        score = 100.0


        # -------------------------
        # Loudness
        # -------------------------

        if -14.5 <= analysis.lufs <= -9.0:

            strengths.append(
                "Loudness is well balanced."
            )

        else:

            score -= 8

            issues.append(
                Issue(
                    title="Loudness",
                    severity="medium",
                    description=(
                        "Integrated loudness is outside the expected range "
                        "for a full mix."
                    ),
                    recommendation=(
                        "Review overall gain and limiting decisions."
                    ),
                )
            )


        # -------------------------
        # Dynamic Range
        # -------------------------

        if analysis.dynamic_range >= 8:

            strengths.append(
                "Dynamic range is healthy."
            )

        else:

            score -= 10

            issues.append(
                Issue(
                    title="Dynamic Range",
                    severity="medium",
                    description=(
                        "Dynamic range is limited."
                    ),
                    recommendation=(
                        "Review compression and limiting."
                    ),
                )
            )


        # -------------------------
        # Peak / Clipping
        # -------------------------

        if analysis.peak > 1.0:

            score -= 10

            issues.append(
                Issue(
                    title="Clipping",
                    severity="high",
                    description=(
                        "Peak level exceeds 0 dBFS. "
                        "Possible digital clipping or "
                        "inter-sample peak distortion."
                    ),
                    recommendation=(
                        "Reduce output gain and check true peak levels."
                    ),
                )
            )

        else:

            strengths.append(
                "No digital clipping detected."
            )


        # -------------------------
        # Phase Correlation
        # -------------------------

        if analysis.phase >= 0.7:

            strengths.append(
                "Stereo phase correlation is strong."
            )


        elif analysis.phase >= 0.3:

            issues.append(
                Issue(
                    title="Phase Correlation",
                    severity="low",
                    description=(
                        "Stereo correlation is moderate. "
                        "Review mono compatibility if required."
                    ),
                    recommendation=(
                        "Check mono compatibility during final review."
                    ),
                )
            )

        else:

            score -= 8

            issues.append(
                Issue(
                    title="Phase Correlation",
                    severity="high",
                    description=(
                        "Low stereo correlation detected. "
                        "Possible phase cancellation issues."
                    ),
                    recommendation=(
                        "Review stereo processing and polarity."
                    ),
                )
            )


        # -------------------------
        # Stereo Width
        # -------------------------

        if analysis.stereo_width >= 0.10:

            strengths.append(
                "Stereo image is acceptable."
            )

        else:

            score -= 5

            issues.append(
                Issue(
                    title="Stereo Width",
                    severity="low",
                    description=(
                        "Stereo image is narrow."
                    ),
                    recommendation=(
                        "Review stereo enhancement decisions."
                    ),
                )
            )


        return (
            strengths,
            issues,
            recommendations,
            max(score, 0),
        )


    # =====================================
    # Stem / Instrument Rules
    # =====================================

    def _evaluate_stem(
        self,
        analysis: AnalysisResult,
    ):

        strengths = []
        issues = []
        recommendations = []

        score = 100.0


        strengths.append(
            "Loudness treated as informational because this is an isolated stem."
        )


        if analysis.dynamic_range >= 8:

            strengths.append(
                "Dynamic behavior is healthy."
            )

        else:

            score -= 5

            issues.append(
                Issue(
                    title="Dynamics",
                    severity="low",
                    description=(
                        "Stem has limited dynamic variation."
                    ),
                    recommendation=(
                        "Check compression or performance dynamics."
                    ),
                )
            )


        if analysis.peak < 1.0:

            strengths.append(
                "No digital clipping detected."
            )

        else:

            score -= 10

            issues.append(
                Issue(
                    title="Clipping",
                    severity="high",
                    description=(
                        "Signal exceeds digital peak limits."
                    ),
                    recommendation=(
                        "Reduce gain."
                    ),
                )
            )


        strengths.append(
            "Tonal characteristics detected."
        )


        return (
            strengths,
            issues,
            recommendations,
            max(score, 0),
        )