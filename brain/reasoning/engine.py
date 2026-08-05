from __future__ import annotations

from abc import ABC, abstractmethod

from brain.providers.base import BaseAIProvider

from .builder import PromptBuilder
from .guards.output import OutputGuard
from .models import (
    ReasoningContext,
    ReasoningPrompt,
    ReasoningResult,
)
from .parser import ResponseParser


class BaseReasoningProvider(ABC):
    """Abstract contract for reasoning providers."""

    @abstractmethod
    def generate(
        self,
        prompt: ReasoningPrompt,
    ) -> ReasoningResult: ...


class LLMReasoningProvider(BaseReasoningProvider):
    """
    Reasoning provider backed by the new AI provider layer.

    This implementation depends only on ``BaseAIProvider`` and routes generation
    calls through the provider's standard ``GenerateRequest`` / ``GenerateResponse``
    contract. The default provider is the configured production provider (Qwen by
    default), which keeps the reasoning engine free of provider-specific logic.
    """

    def __init__(
        self,
        provider: BaseAIProvider | None = None,
    ) -> None:
        from brain.providers.factory import ProviderFactory
        from brain.providers.models import GenerateRequest

        self._provider = provider or ProviderFactory.default()
        self._request_cls = GenerateRequest

    def generate(
        self,
        prompt: ReasoningPrompt,
    ) -> ReasoningResult:
        response = self._provider.generate(
            self._request_cls(
                system_prompt=prompt.system,
                user_prompt=prompt.user,
            )
        )

        return ReasoningResult(
            answer=response.text,
            confidence=response.confidence,
            reasoning=[f"Provider: {response.provider}"],
        )


class ReasoningEngine:
    """High-level reasoning entry point."""

    def __init__(
        self,
        provider: BaseReasoningProvider | None = None,
    ) -> None:
        self._builder = PromptBuilder()
        self._provider = provider or LLMReasoningProvider()
        self._output_guard = OutputGuard()
        self._parser = ResponseParser()

    def ask(
        self,
        context: ReasoningContext,
    ) -> ReasoningResult:
        prompt = self._builder.build(context)
        result = self._provider.generate(prompt)

        filtered_answer = self._output_guard.filter(result.answer)
        parsed_result = self._parser.parse(filtered_answer)

        parsed_result.confidence = result.confidence
        parsed_result.reasoning.extend(result.reasoning)

        return parsed_result
