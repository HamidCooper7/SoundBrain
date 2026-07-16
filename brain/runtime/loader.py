from __future__ import annotations

from .exceptions import ModelLoadError
from .models import LoadedModelAssets
from .repository import ModelRepository


class ModelLoader:
    """
    Generic model loader.

    Supports:
        - HuggingFace Transformers
        - SentenceTransformer
    """

    def __init__(self) -> None:

        self.repository = ModelRepository()

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

        source, local = self.repository.resolve(model_name)

        kwargs = {
            "trust_remote_code": trust_remote_code,
        }

        if local:
            kwargs["local_files_only"] = True

        try:

            # -----------------------------
            # SentenceTransformer Backend
            # -----------------------------
            if model_cls.__name__ in {"SentenceTransformer", "CrossEncoder"}:

                model = model_cls(
                    source,
                    **kwargs,
                )

                return LoadedModelAssets(
                    model=model,
                )

            # -----------------------------
            # HuggingFace Transformers
            # -----------------------------
            model = model_cls.from_pretrained(
                source,
                **kwargs,
            )

            processor = None
            tokenizer = None
            feature_extractor = None

            if processor_cls is not None:

                processor = processor_cls.from_pretrained(
                    source,
                    **kwargs,
                )

            if tokenizer_cls is not None:

                tokenizer = tokenizer_cls.from_pretrained(
                    source,
                    **kwargs,
                )

            if feature_extractor_cls is not None:

                feature_extractor = feature_extractor_cls.from_pretrained(
                    source,
                    **kwargs,
                )

            return LoadedModelAssets(
                model=model,
                processor=processor,
                tokenizer=tokenizer,
                feature_extractor=feature_extractor,
            )

        except Exception as exc:

            raise ModelLoadError(
                f"Unable to load model '{model_name}'."
            ) from exc
