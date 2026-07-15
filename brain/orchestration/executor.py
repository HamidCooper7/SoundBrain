from __future__ import annotations

from brain.orchestration.state import State

from brain.pipeline.engine import PipelineEngine


from brain.pipeline.memory_stage import MemoryStage
from brain.pipeline.rag_stage import RAGStage
from brain.pipeline.compression_stage import CompressionStage
from brain.pipeline.prompt_stage import PromptStage
from brain.pipeline.llm_stage import LLMStage
from brain.pipeline.vision_stage import VisionStage


class Executor:

    def __init__(self):

        self.engine = PipelineEngine()

        self.engine.register(
            "memory",
            MemoryStage(),
        )

        self.engine.register(
            "rag",
            RAGStage(),
        )

        self.engine.register(
            "compression",
            CompressionStage(),
        )

        self.engine.register(
            "prompt",
            PromptStage(),
        )

        self.engine.register(
            "llm",
            LLMStage(),
        )

        self.engine.register(
            "vision",
            VisionStage(),
        )

    def execute(
        self,
        state: State,
    ) -> State:

        print()
        print("=" * 80)
        print("EXECUTION")
        print("=" * 80)

        return self.engine.run(state)