from __future__ import annotations

from brain.orchestration.state import State


class PipelineEngine:

    def __init__(self):

        self.stages: dict[str, object] = {}

    def register(
        self,
        name: str,
        stage,
    ) -> None:

        self.stages[name] = stage

    def run(
        self,
        state: State,
    ) -> State:

        print()
        print("Pipeline:")
        print(state.pipeline)
        print()

        for stage_name in state.pipeline:

            stage = self.stages.get(stage_name)

            if stage is None:

                print(f"Skipping -> {stage_name}")

                continue

            print(f"Running -> {stage_name}")

            state = stage.run(state)

        return state