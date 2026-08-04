from __future__ import annotations

from brain.audio.context.models import AudioContext
from brain.audio.mix.models import (
    MixIntelligenceResult,
    PrioritizedIssue,
    RootCause,
)

from .models import (
    PluginIntelligenceResult,
    PluginIntelligenceStep,
    ProcessingGoal,
)
from .parameter_generator import ParameterGenerator
from .selector import PluginSelector
from .taxonomy import CATEGORY_TO_TYPE, CATEGORY_UTILITY


class PluginChainBuilder:
    """Transform Mix Intelligence results into a plugin-aware processing chain."""

    def __init__(
        self,
        parameter_generator: ParameterGenerator | None = None,
        selector: PluginSelector | None = None,
    ) -> None:
        if parameter_generator is None:
            self._parameter_generator = ParameterGenerator()
        else:
            self._parameter_generator = parameter_generator

        if selector is None:
            self._selector = PluginSelector()
        else:
            self._selector = selector

    def build(
        self,
        mix_result: MixIntelligenceResult,
        context: AudioContext,
    ) -> PluginIntelligenceResult:
        goals = self._build_goals(mix_result)
        steps: list[PluginIntelligenceStep] = []
        seen_categories: set[str] = set()
        order = 1

        for goal in goals:
            category = self._category_for_goal(goal)
            if category in seen_categories:
                continue
            seen_categories.add(category)

            plugin_type = CATEGORY_TO_TYPE.get(category, "Utility")
            parameters = self._parameter_generator.generate(goal, category)
            options = self._selector.select(category, limit=3)

            steps.append(
                PluginIntelligenceStep(
                    order=order,
                    goal=goal,
                    plugin_category=category,
                    plugin_type=plugin_type,
                    parameter_recommendations=parameters,
                    plugin_options=options,
                    suggestion=f"Use a {plugin_type} to {goal.description}",
                    estimated_impact=self._impact(goal.confidence),
                    confidence=goal.confidence,
                )
            )
            order += 1

            if len(steps) >= 6:
                break

        return PluginIntelligenceResult(
            goals=goals,
            steps=steps,
            confidence_scores=mix_result.confidence_scores,
            explanations=[
                f"Step {step.order}: {step.plugin_type} for {step.goal.description}"
                for step in steps
            ],
        )

    def _build_goals(
        self,
        mix_result: MixIntelligenceResult,
    ) -> list[ProcessingGoal]:
        goals: list[ProcessingGoal] = []
        for issue in mix_result.prioritized_issues[:6]:
            cause = self._find_matching_cause(issue, mix_result.root_causes)
            goals.append(
                ProcessingGoal(
                    id=f"goal_{issue.user_action_order}",
                    description=issue.description or issue.title,
                    target=issue.title,
                    root_cause=cause.symptom if cause else None,
                    action=issue.recommendation,
                    confidence=issue.confidence,
                )
            )
        return goals

    def _find_matching_cause(
        self,
        issue: PrioritizedIssue,
        causes: list[RootCause],
    ) -> RootCause | None:
        title = issue.title.lower()
        for cause in causes:
            if title in cause.symptom.lower() or cause.symptom.lower() in title:
                return cause
        return None

    def _category_for_goal(self, goal: ProcessingGoal) -> str:
        target = goal.target.lower()
        description = goal.description.lower()
        text = f"{target} {description}"

        if any(k in text for k in ("harsh", "high", "sibilance", "brightness", "frequency", "eq")):
            return "eq"
        if any(k in text for k in ("loudness", "lufs", "limit", "gain")):
            return "limiter"
        if any(k in text for k in ("dynamic", "compression", "punch", "flat")):
            return "compressor"
        if any(k in text for k in ("stereo", "width", "phase", "mono")):
            return "imager"
        if any(k in text for k in ("transient", "attack", "smack")):
            return "transient_shaper"
        if any(k in text for k in ("warmth", "saturation", "harmonic")):
            return "saturation"

        return CATEGORY_UTILITY

    def _impact(self, confidence: float) -> str:
        if confidence >= 0.85:
            return "high"
        if confidence >= 0.65:
            return "medium"
        return "low"
