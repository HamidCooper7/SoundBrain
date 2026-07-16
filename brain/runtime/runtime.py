from __future__ import annotations

import torch

from .cache import ModelCache
from .device import DeviceManager
from .loader import ModelLoader
from .models import LoadedModelAssets


class ModelRuntime:
    """
    Shared runtime for every AI model.
    """

    _shared: "ModelRuntime | None" = None

    def __init__(
        self,
        loader: ModelLoader | None = None,
        device: torch.device | None = None,
    ) -> None:

        self.device = device or DeviceManager.detect()

        self.cache = ModelCache()

        self.loader = loader or ModelLoader()

    @classmethod
    def shared(cls) -> "ModelRuntime":
        if cls._shared is None:
            cls._shared = cls()
        return cls._shared

    @property
    def dtype(self) -> torch.dtype:

        if self.device.type == "cuda":
            return torch.float16

        return torch.float32

    def load(
        self,
        *,
        model_name: str,
        model_cls: type,
        processor_cls: type | None = None,
        tokenizer_cls: type | None = None,
        feature_extractor_cls: type | None = None,
        trust_remote_code: bool = False,
    ) -> LoadedModelAssets:

        cache_key = self._cache_key(model_name, model_cls)

        if self.cache.contains(cache_key):

            return self.cache.get(cache_key)

        assets = self.loader.load(
            model_name=model_name,
            model_cls=model_cls,
            processor_cls=processor_cls,
            tokenizer_cls=tokenizer_cls,
            feature_extractor_cls=feature_extractor_cls,
            trust_remote_code=trust_remote_code,
        )

        # SentenceTransformer خودش Device را مدیریت می‌کند.
        if (
            hasattr(assets.model, "to")
            and model_cls.__name__ != "SentenceTransformer"
        ):

            assets.model = assets.model.to(
                self.device,
                dtype=self.dtype,
            )

        assets.device = self.device
        assets.dtype = self.dtype

        self.cache.put(
            cache_key,
            assets,
        )

        return assets

    def clear_cache(self) -> None:

        self.cache.clear()

    def unload_model(self, model_name: str, model_cls: type) -> None:
        self.cache.remove(self._cache_key(model_name, model_cls))

    def available_models(self) -> tuple[str, ...]:
        return self.cache.names()

    def model_info(
        self,
        model_name: str,
        model_cls: type,
    ) -> LoadedModelAssets | None:
        cache_key = self._cache_key(model_name, model_cls)
        return self.cache.get(cache_key) if self.cache.contains(cache_key) else None

    def processor(self, model_name: str, model_cls: type):
        assets = self.model_info(model_name, model_cls)
        return assets.processor if assets is not None else None

    def tokenizer(self, model_name: str, model_cls: type):
        assets = self.model_info(model_name, model_cls)
        return assets.tokenizer if assets is not None else None

    @staticmethod
    def _cache_key(model_name: str, model_cls: type) -> str:
        return f"{model_name}:{model_cls.__name__}"
