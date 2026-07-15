from __future__ import annotations


from .embeddings import (
    AudioEmbeddingModel,
    CLAPAudioEmbeddingModel,
)


from .classifier import (
    AudioSemanticClassifier,
)


from .models import (
    AudioSemanticResult,
)



class AudioIntelligenceAnalyzer:


    def __init__(
        self,
        embedding_model: AudioEmbeddingModel | None = None,
        classifier: AudioSemanticClassifier | None = None,
    ) -> None:


        self._embedding_model = (

            embedding_model

            or CLAPAudioEmbeddingModel()

        )


        self._classifier = (

            classifier

            or AudioSemanticClassifier(
                self._embedding_model
            )

        )



    def analyze(
        self,
        audio,
    ) -> AudioSemanticResult:


        embedding = (

            self._embedding_model.encode(
                audio
            )

        )


        return self._classifier.classify(
            embedding
        )