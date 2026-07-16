from __future__ import annotations


class ModelCache:

    def __init__(self) -> None:
        self._models: dict[str, object] = {}

    def contains(
        self,
        name: str,
    ) -> bool:

        return name in self._models

    def get(self, name: str) -> object:
        return self._models[name]

    def put(
        self,
        name: str,
        model: object,
    ) -> None:

        self._models[name] = model

    def clear(self) -> None:
        self._models.clear()

    def remove(self, name: str) -> None:
        self._models.pop(name, None)

    def names(self) -> tuple[str, ...]:
        return tuple(self._models)

    def size(self) -> int:
        return len(self._models)
