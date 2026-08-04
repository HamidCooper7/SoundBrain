from __future__ import annotations

from .base import BaseAIProvider
from .models import GenerateRequest, GenerateResponse


class QwenProvider(BaseAIProvider):
    """
    Production provider backed by the local Qwen integration.

    The heavy transformers import is deferred to the first `generate()` call so
    importing this module does not load torch.
    """

    name = "qwen"

    def generate(self, request: GenerateRequest) -> GenerateResponse:
        from brain.llm.qwen import generate

        answer = generate(
            prompt=request.user_prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
        )
        return GenerateResponse(
            text=answer,
            provider=self.name,
            confidence=1.0,
        )
