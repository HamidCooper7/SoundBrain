from __future__ import annotations

from brain.audio.context.models import AudioContext

from .models import PrioritizedIssue, ProcessingStep, RootCauseResult


class ProcessingChainRecommender:
    """
    Map prioritized issues to a non-destructive processing chain.

    Sprint 5 uses high-level plugin-type suggestions only. No models are loaded.
    """

    def recommend(
        self,
        root_causes: RootCauseResult,
        prioritized_issues: list[PrioritizedIssue],
        context: AudioContext,
    ) -> list[ProcessingStep]:
        steps: list[ProcessingStep] = []
        seen_targets: set[str] = set()

        for issue in prioritized_issues:
            if len(steps) >= 6:
                break

            target = self._target(issue.title)
            if target in seen_targets:
                continue
            seen_targets.add(target)

            plugin_type = self._plugin_type(target)
            suggestion = self._suggestion(issue, root_causes)
            impact = self._impact(issue.category, issue.severity)

            steps.append(
                ProcessingStep(
                    order=issue.user_action_order,
                    target=target,
                    plugin_type=plugin_type,
                    suggestion=suggestion,
                    estimated_impact=impact,
                    confidence=issue.confidence,
                )
            )

        return steps

    def _target(self, title: str) -> str:
        title = title.lower()

        if any(keyword in title for keyword in ("harsh", "high", "sibilance", "brightness")):
            return "frequency_balance"

        if any(keyword in title for keyword in ("loudness", "lufs", "limit", "gain")):
            return "loudness"

        if any(keyword in title for keyword in ("dynamic", "compression", "punch", "flat")):
            return "dynamics"

        if any(keyword in title for keyword in ("stereo", "width", "phase", "mono")):
            return "stereo_image"

        if any(keyword in title for keyword in ("transient", "attack", "smack")):
            return "transients"

        return "tonal_balance"

    def _plugin_type(self, target: str) -> str:
        mapping = {
            "frequency_balance": "EQ",
            "loudness": "Limiter",
            "dynamics": "Compressor",
            "stereo_image": "Imager",
            "transients": "Transient Shaper",
            "tonal_balance": "EQ",
        }
        return mapping.get(target, "Utility")

    def _suggestion(
        self,
        issue: PrioritizedIssue,
        root_causes: RootCauseResult,
    ) -> str:
        for cause in root_causes.causes:
            if (
                issue.title.lower() in cause.symptom.lower()
                or cause.symptom.lower() in issue.title.lower()
            ):
                return (
                    f"Address {issue.title}: likely due to "
                    f"{cause.likely_causes[0]}. Recommended action: {issue.recommendation}"
                )

        return f"Address {issue.title}: {issue.recommendation}"

    def _impact(self, category: str, severity: str) -> str:
        if category == "fix first" or severity.lower() in ("critical", "high"):
            return "high"

        if category == "fine tune" or severity.lower() == "medium":
            return "medium"

        return "low"
