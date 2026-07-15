from __future__ import annotations


from abc import ABC
from abc import abstractmethod


from brain.llm.manager import LLMManager


from .builder import PromptBuilder

from .guards.output import OutputGuard

from .parser import ResponseParser

from .models import (
    ReasoningContext,
    ReasoningPrompt,
    ReasoningResult,
)




class BaseReasoningProvider(ABC):


    @abstractmethod
    def generate(
        self,
        prompt: ReasoningPrompt,
    ) -> ReasoningResult:

        ...





class LLMReasoningProvider(BaseReasoningProvider):


    def __init__(
        self,
        llm_manager: LLMManager | None = None,
        provider_name: str = "lmstudio",
    ) -> None:


        self._manager = (

            llm_manager

            or LLMManager()

        )


        self._provider_name = provider_name




    def generate(
        self,
        prompt: ReasoningPrompt,
    ) -> ReasoningResult:


        llm = self._manager.get(
            self._provider_name,
        )


        answer = llm.generate(

            system_prompt=prompt.system,

            user_prompt=prompt.user,

        )


        return ReasoningResult(

            answer=answer,

            confidence=1.0,

            reasoning=[

                f"Provider: {self._provider_name}"

            ],

        )






class ReasoningEngine:


    def __init__(
        self,
        provider: BaseReasoningProvider | None = None,
    ) -> None:


        self._builder = PromptBuilder()


        self._provider = (

            provider

            or LLMReasoningProvider()

        )


        self._output_guard = OutputGuard()


        self._parser = ResponseParser()





    def ask(
        self,
        context: ReasoningContext,
    ) -> ReasoningResult:


        prompt = self._builder.build(
            context,
        )


        result = self._provider.generate(
            prompt,
        )


        filtered_answer = self._output_guard.filter(
            result.answer,
        )


        parsed_result = self._parser.parse(
            filtered_answer,
        )


        parsed_result.confidence = result.confidence


        parsed_result.reasoning.extend(
            result.reasoning,
        )


        return parsed_result