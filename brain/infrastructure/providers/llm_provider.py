from __future__ import annotations

from abc import abstractmethod

from brain.infrastructure.providers.base import Provider


class LLMProvider(Provider):

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a completion.
        """