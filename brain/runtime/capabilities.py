from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class CapabilityStatus(str, Enum):
    PLANNED = "planned"
    IMPLEMENTED = "implemented"
    VERIFIED = "verified"
    PRODUCTION = "production"
    DEPRECATED = "deprecated"


@dataclass(frozen=True, slots=True)
class Capability:
    """
    Describes one runtime capability.
    """

    name: str
    description: str
    status: CapabilityStatus


class CapabilityRegistry:
    """
    Registry of Runtime capabilities.

    This registry is intentionally independent from ModelRuntime.
    Runtime will consume it in the next step.
    """

    def __init__(self) -> None:
        self._capabilities: dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        self._capabilities[capability.name] = capability

    def unregister(self, name: str) -> None:
        self._capabilities.pop(name, None)

    def exists(self, name: str) -> bool:
        return name in self._capabilities

    def get(self, name: str) -> Capability | None:
        return self._capabilities.get(name)

    def all(self) -> tuple[Capability, ...]:
        return tuple(
            sorted(
                self._capabilities.values(),
                key=lambda capability: capability.name,
            )
        )

    def names(self) -> tuple[str, ...]:
        return tuple(
            capability.name
            for capability in self.all()
        )

    def clear(self) -> None:
        self._capabilities.clear()

    def __contains__(self, name: str) -> bool:
        return self.exists(name)

    def __len__(self) -> int:
        return len(self._capabilities)

    def __iter__(self):
        return iter(self.all())


registry = CapabilityRegistry()

registry.register(
    Capability(
        name="runtime",
        description="Shared model runtime",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="model_loading",
        description="Lazy model loading",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="model_cache",
        description="Runtime cache",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="repository",
        description="Model repository resolution",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="transformers_backend",
        description="Transformers backend strategy",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="sentence_transformers_backend",
        description="SentenceTransformers backend strategy",
        status=CapabilityStatus.PRODUCTION,
    )
)

# ---------------------------------------------------------------------------
# V1 SoundBrain capabilities
# ---------------------------------------------------------------------------

registry.register(
    Capability(
        name="audio_loading",
        description="Load and validate audio files via AudioIOService",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="dsp_analysis",
        description="Deterministic DSP analysis (loudness, spectrum, dynamics, stereo)",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="audio_context",
        description="Rule-based audio context and source classification",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="engineering_analysis",
        description="Engineering rule engine that produces scores, issues, and recommendations",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="clap_embedding",
        description="CLAP-based audio-text semantic embeddings",
        status=CapabilityStatus.VERIFIED,
    )
)

registry.register(
    Capability(
        name="reference_comparison",
        description="Reference versus current mix comparison and reasoned report",
        status=CapabilityStatus.VERIFIED,
    )
)

registry.register(
    Capability(
        name="rag_retrieval",
        description="RAG document retrieval for knowledge-backed answers",
        status=CapabilityStatus.IMPLEMENTED,
    )
)

registry.register(
    Capability(
        name="llm_reasoning",
        description="LLM-based reasoning over analysis and context",
        status=CapabilityStatus.IMPLEMENTED,
    )
)

registry.register(
    Capability(
        name="report_generation",
        description="Structured JSON and Markdown report generation",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="service_facade",
        description="V1 SoundBrainService unified entry point",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="engine_registry",
        description="Named engine registry for routing runtime workflows",
        status=CapabilityStatus.PRODUCTION,
    )
)

registry.register(
    Capability(
        name="orchestration",
        description="Planner/Router/Executor orchestration layer",
        status=CapabilityStatus.IMPLEMENTED,
    )
)

registry.register(
    Capability(
        name="audio_intelligence",
        description="Sprint 4+ semantic audio intelligence",
        status=CapabilityStatus.PLANNED,
    )
)

registry.register(
    Capability(
        name="mix_intelligence",
        description="Sprint 5+ mix-aware engineering intelligence",
        status=CapabilityStatus.PLANNED,
    )
)

registry.register(
    Capability(
        name="plugin_intelligence",
        description="Sprint 6+ plugin and preset recommendation",
        status=CapabilityStatus.PLANNED,
    )
)

registry.register(
    Capability(
        name="memory_learning",
        description="Sprint 7+ long-term memory and continuous learning",
        status=CapabilityStatus.PLANNED,
    )
)

registry.register(
    Capability(
        name="daw_integration",
        description="Sprint 8+ DAW plugin and automation integration",
        status=CapabilityStatus.PLANNED,
    )
)

__all__ = [
    "Capability",
    "CapabilityRegistry",
    "CapabilityStatus",
    "registry",
]


if __name__ == "__main__":
    for capability in registry:
        print(f"{capability.name}: {capability.status.value}")
