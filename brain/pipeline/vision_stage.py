from __future__ import annotations

from brain.orchestration.state import State
from brain.pipeline import Stage

from brain.services import VisionService


class VisionStage(Stage):

    def __init__(self):

        self.vision = VisionService()

    def run(
        self,
        state: State,
    ) -> State:

        if state.image is not None:

            state.image = self.vision.process(
                state.image
            )

        return state