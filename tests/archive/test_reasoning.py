from brain.audio.analysis import AudioAnalyzer
from brain.audio.engineer import AudioEngineer
from brain.audio.io import AudioIOService

from brain.reasoning import (
    BaseReasoningProvider,
    ReasoningContext,
    ReasoningEngine,
    ReasoningResult,
)


class MockProvider(BaseReasoningProvider):

    def generate(self, prompt):

        print("========== SYSTEM ==========")
        print(prompt.system)

        print()

        print("========== USER ==========")
        print(prompt.user)

        print()

        return ReasoningResult(
            answer="Mock response from SoundBrain.",
            confidence=1.0,
            reasoning=[
                "Pipeline OK",
                "Prompt OK",
            ],
        )


audio = AudioIOService().load(
    "music/test.wav",
)

analysis = AudioAnalyzer().analyze(
    audio,
)

engineer = AudioEngineer().analyze(
    analysis,
)

context = ReasoningContext(
    analysis=analysis,
    engineer=engineer,
    question="Is this mix good?",
)

engine = ReasoningEngine(
    MockProvider(),
)

result = engine.ask(
    context,
)

print()

print("========== RESULT ==========")

print(result.answer)

print(result.confidence)

print(result.reasoning)