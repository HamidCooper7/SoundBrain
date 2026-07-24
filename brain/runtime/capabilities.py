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