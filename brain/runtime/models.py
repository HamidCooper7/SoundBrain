from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch
from transformers import PretrainedConfig


@dataclass(slots=True, frozen=True)
class ModelInfo:
    """
    Static information describing a model.
    """

    name: str

    backend: str = "transformers"

    revision: str | None = None

    local_path: Path | None = None

    dtype: torch.dtype = torch.float32


@dataclass(slots=True)
class LoadedModelAssets:
    """
    Every loaded model returns this object.

    Not every model has tokenizer or feature extractor,
    therefore they are optional.
    """

    model: Any

    processor: Any | None = None

    tokenizer: Any | None = None

    feature_extractor: Any | None = None

    config: PretrainedConfig | None = None

    device: torch.device | None = None

    dtype: torch.dtype | None = None