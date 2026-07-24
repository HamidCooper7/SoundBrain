from __future__ import annotations

from .models import (
    Category,
    EngineerDecision,
    ReferenceComparison,
    Severity,
)


class ReferenceReasoner:
    """
    Converts raw comparison metrics into
    professional engineering decisions.

    This is the first reasoning layer.

    Future versions will integrate:

    - AES knowledge
    - Mix engineering rules
    - RAG
    - LLM reasoning
    - Learning system
    """

    def reason(
        self,
        comparison: ReferenceComparison,
    ) -> ReferenceComparison:

        decisions: list[EngineerDecision] = []

        decisions.extend(
            self._frequency(
                comparison
            )
        )

        decisions.extend(
            self._loudness(
                comparison
            )
        )

        decisions.extend(
            self._dynamics(
                comparison
            )
        )

        decisions.extend(
            self._stereo(
                comparison
            )
        )

        decisions.extend(
            self._phase(
                comparison
            )
        )

        decisions.extend(
            self._transients(
                comparison
            )
        )

        comparison.engineer_decisions.extend(
            decisions
        )

        comparison.engineer_decisions.sort(
            key=self._priority,
            reverse=True,
        )

        return comparison

    def _frequency(
        self,
        comparison: ReferenceComparison,
    ) -> list[EngineerDecision]:

        result = []

        for band in comparison.band_differences:

            if abs(
                band.difference_db
            ) < 1.5:

                continue

            plugin = "FabFilter Pro-Q 4"

            if band.difference_db > 0:

                recommendation = (
                    f"Reduce {band.band} by "
                    f"{abs(band.difference_db):.1f} dB"
                )

            else:

                recommendation = (
                    f"Boost {band.band} by "
                    f"{abs(band.difference_db):.1f} dB"
                )

            result.append(

                EngineerDecision(

                    title=f"{band.band} Balance",

                    description=(
                        f"{band.band} differs "
                        "from the reference."
                    ),

                    category=Category.FREQUENCY,

                    severity=band.severity,

                    confidence=0.93,

                    recommendation=recommendation,

                    plugin=plugin,

                    parameters={

                        "band": band.band,

                        "start_hz": band.start_hz,

                        "end_hz": band.end_hz,

                        "difference_db":
                        band.difference_db,

                    },

                )

            )

        return result

    def _loudness(
        self,
        comparison: ReferenceComparison,
    ):

        if comparison.loudness_score >= 95:

            return []

        return [

            EngineerDecision(

                title="Loudness",

                description=(
                    "Overall loudness "
                    "differs from reference."
                ),

                category=Category.LOUDNESS,

                severity=Severity.MEDIUM,

                confidence=0.90,

                recommendation=(
                    "Adjust limiter target LUFS."
                ),

                plugin="FabFilter Pro-L 2",

            )

        ]

    def _dynamics(
        self,
        comparison: ReferenceComparison,
    ):

        if comparison.dynamic_score >= 95:

            return []

        return [

            EngineerDecision(

                title="Dynamics",

                description=(
                    "Dynamic profile "
                    "is different."
                ),

                category=Category.DYNAMICS,

                severity=Severity.MEDIUM,

                confidence=0.91,

                recommendation=(
                    "Review bus compression."
                ),

                plugin="FabFilter Pro-C 2",

            )

        ]

    def _stereo(
        self,
        comparison: ReferenceComparison,
    ):

        if comparison.stereo_score >= 95:

            return []

        return [

            EngineerDecision(

                title="Stereo Image",

                description=(
                    "Stereo image differs."
                ),

                category=Category.STEREO,

                severity=Severity.LOW,

                confidence=0.88,

                recommendation=(
                    "Adjust stereo width."
                ),

                plugin="iZotope Ozone Imager",

            )

        ]

    def _phase(
        self,
        comparison: ReferenceComparison,
    ):

        if comparison.phase_score >= 95:

            return []

        return [

            EngineerDecision(

                title="Phase",

                description=(
                    "Possible phase issues."
                ),

                category=Category.PHASE,

                severity=Severity.HIGH,

                confidence=0.94,

                recommendation=(
                    "Inspect mono compatibility."
                ),

            )

        ]

    def _transients(
        self,
        comparison: ReferenceComparison,
    ):

        if comparison.transient_score >= 95:

            return []

        return [

            EngineerDecision(

                title="Transient",

                description=(
                    "Transient response "
                    "is different."
                ),

                category=Category.TRANSIENT,

                severity=Severity.MEDIUM,

                confidence=0.89,

                recommendation=(
                    "Review transient shaping."
                ),

                plugin="SPL Transient Designer",

            )

        ]

    def _priority(
        self,
        decision: EngineerDecision,
    ) -> int:

        table = {

            Severity.CRITICAL: 5,

            Severity.HIGH: 4,

            Severity.MEDIUM: 3,

            Severity.LOW: 2,

            Severity.INFO: 1,

        }

        return table[
            decision.severity
        ]