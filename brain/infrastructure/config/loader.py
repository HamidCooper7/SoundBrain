from __future__ import annotations

from pathlib import Path
from typing import Any

from brain.infrastructure.config.models import (
    AppConfig,
    AudioConfig,
    ChromaConfig,
    EmbeddingConfig,
    LLMConfig,
    LoggingConfig,
    ModelEntry,
    ModelsConfig,
    RuntimeConfig,
)
from brain.infrastructure.config.settings import DEFAULT_SETTINGS

try:
    import yaml
except Exception:  # pragma: no cover - PyYAML is optional in some test envs
    yaml = None


def _project_root() -> Path:
    """Return the repository root (directory containing pyproject.toml)."""
    return Path(__file__).resolve().parents[3]


def _config_dir() -> Path:
    return _project_root() / "configs"


def _load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file, returning an empty dict if it is missing or empty."""
    if yaml is None or not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return {}
    data = yaml.safe_load(text)
    return data if isinstance(data, dict) else {}


def _deep_update(
    base: dict[str, Any],
    overlay: dict[str, Any],
) -> dict[str, Any]:
    """Recursively merge overlay into base."""
    for key, value in overlay.items():
        if (
            key in base
            and isinstance(base[key], dict)
            and isinstance(value, dict)
        ):
            _deep_update(base[key], value)
        else:
            base[key] = value
    return base


def _expand_path(value: str | Path | None, root: Path) -> Path | None:
    """Resolve a config path relative to the project root."""
    if value is None:
        return None
    path = Path(str(value)).expanduser()
    if path.is_absolute():
        return path
    return (root / path).resolve()


def _model_entry(data: dict[str, Any] | None, default: ModelEntry) -> ModelEntry:
    if not data:
        return default
    return ModelEntry(
        name=data.get("name", default.name),
        backend=data.get("backend", default.backend),
        revision=data.get("revision", default.revision),
    )


def load_settings() -> AppConfig:
    """Load configuration from configs/*.yaml and return a populated AppConfig.

    Missing or invalid YAML files fall back to DEFAULT_SETTINGS so the
    application can start even when the config directory is absent.
    """
    root = _project_root()
    config_dir = _config_dir()

    merged: dict[str, Any] = {}
    for name in ("runtime", "models", "audio"):
        merged = _deep_update(merged, _load_yaml(config_dir / f"{name}.yaml"))

    runtime_data = merged.get("runtime", {})
    logging_data = merged.get("logging", {})
    audio_data = merged.get("audio", {})
    models_data = merged.get("models", {})

    default_runtime = DEFAULT_SETTINGS.runtime
    default_logging = DEFAULT_SETTINGS.logging
    default_audio = DEFAULT_SETTINGS.audio
    default_models = DEFAULT_SETTINGS.models

    text_embedding_entry = _model_entry(
        models_data.get("text_embedding"),
        default_models.text_embedding,
    )

    return AppConfig(
        runtime=RuntimeConfig(
            device=runtime_data.get("device", default_runtime.device),
            dtype=runtime_data.get("dtype", default_runtime.dtype),
            lazy_load=runtime_data.get("lazy_load", default_runtime.lazy_load),
            model_root=_expand_path(
                runtime_data.get("model_root", default_runtime.model_root),
                root,
            ),
            model_cache_dir=_expand_path(
                runtime_data.get("model_cache_dir", default_runtime.model_cache_dir),
                root,
            ),
            cache_dir=_expand_path(
                runtime_data.get("cache_dir", default_runtime.cache_dir),
                root,
            ),
            log_dir=_expand_path(
                runtime_data.get("log_dir", default_runtime.log_dir),
                root,
            ),
            report_dir=_expand_path(
                runtime_data.get("report_dir", default_runtime.report_dir),
                root,
            ),
        ),
        logging=LoggingConfig(
            level=logging_data.get("level", default_logging.level),
            format=logging_data.get("format", default_logging.format),
        ),
        audio=AudioConfig(
            sample_rate=audio_data.get("sample_rate", default_audio.sample_rate),
            clap_target_sample_rate=audio_data.get(
                "clap_target_sample_rate",
                default_audio.clap_target_sample_rate,
            ),
            max_duration_seconds=audio_data.get(
                "max_duration_seconds",
                default_audio.max_duration_seconds,
            ),
            n_fft=audio_data.get("n_fft", default_audio.n_fft),
            hop_length=audio_data.get("hop_length", default_audio.hop_length),
            n_mels=audio_data.get("n_mels", default_audio.n_mels),
            n_mfcc=audio_data.get("n_mfcc", default_audio.n_mfcc),
            n_chroma=audio_data.get("n_chroma", default_audio.n_chroma),
        ),
        models=ModelsConfig(
            clap=_model_entry(
                models_data.get("clap"),
                default_models.clap,
            ),
            qwen=_model_entry(
                models_data.get("qwen"),
                default_models.qwen,
            ),
            bge_reranker=_model_entry(
                models_data.get("bge_reranker"),
                default_models.bge_reranker,
            ),
            text_embedding=text_embedding_entry,
        ),
        llm=DEFAULT_SETTINGS.llm,
        embedding=EmbeddingConfig(
            # Model names are kept as-is so ModelRepository can resolve
            # local folders under models/ or fall back to HuggingFace IDs.
            model_path=Path(text_embedding_entry.name),
            device=runtime_data.get(
                "embedding_device",
                DEFAULT_SETTINGS.embedding.device,
            ),
        ),
        chroma=ChromaConfig(
            path=_expand_path(
                runtime_data.get("chroma_path", DEFAULT_SETTINGS.chroma.path),
                root,
            ),
            collection=runtime_data.get(
                "chroma_collection",
                DEFAULT_SETTINGS.chroma.collection,
            ),
        ),
    )
