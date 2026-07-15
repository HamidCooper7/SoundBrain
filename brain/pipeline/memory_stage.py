from __future__ import annotations

from brain.orchestration.state import State
from brain.pipeline import Stage


class MemoryStage(Stage):

    def run(
        self,
        state: State,
    ) -> State:

        return state