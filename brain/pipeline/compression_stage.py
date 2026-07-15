from __future__ import annotations

from brain.orchestration.state import State
from brain.pipeline import Stage
from brain.services import CompressionService


class CompressionStage(Stage):

    def __init__(self):

        self.service = CompressionService()

    def run(
        self,
        state: State,
    ) -> State:

        state.context = self.service.compress(
            state.question,
            state.documents,
        )

        return state