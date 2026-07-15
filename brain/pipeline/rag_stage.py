from __future__ import annotations

from brain.orchestration.state import State
from brain.pipeline import Stage
from brain.services.rag_service import RAGService


class RAGStage(Stage):

    def __init__(self):

        self.rag = RAGService()

    def run(
        self,
        state: State,
    ) -> State:

        result = self.rag.ask(
            state.question
        )

        state.documents = result["documents"]

        return state