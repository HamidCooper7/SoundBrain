from __future__ import annotations

from brain.orchestration.state import State
from brain.pipeline import Stage

from brain.services import PromptService


class PromptStage(Stage):

    def __init__(self):

        self.prompt = PromptService()

    def run(
        self,
        state: State,
    ) -> State:

        state.context, state.prompt = self.prompt.build(
            question=state.question,
            documents=state.documents,
        )

        return state