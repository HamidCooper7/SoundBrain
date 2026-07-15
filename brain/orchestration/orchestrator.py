from __future__ import annotations

from brain.orchestration.executor import Executor
from brain.orchestration.planner import Planner
from brain.orchestration.router import Router
from brain.orchestration.state import State


class Orchestrator:

    def __init__(self):

        self.planner = Planner()
        self.router = Router()
        self.executor = Executor()

    def run(self, question: str) -> State:

        state = State(
            question=question
        )

        state = self.planner.plan(state)

        state = self.router.route(state)

        state = self.executor.execute(state)

        return state