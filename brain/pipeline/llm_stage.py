from __future__ import annotations

from brain.orchestration.state import State
from brain.pipeline import Stage

from brain.services import LLMService


class LLMStage(Stage):

    def __init__(self):

        self.llm = LLMService()

    def run(
        self,
        state: State,
    ) -> State:

        state.answer = self.llm.ask(
            state.prompt
        )

        return state