from brain.audio.io import AudioIOService
from brain.audio.intelligence import (
    AudioIntelligenceAnalyzer,
)


def main():

    audio = AudioIOService().load(
        "music/test.wav"
    )


    analyzer = AudioIntelligenceAnalyzer()


    result = analyzer.analyze(
        audio
    )


    print()
    print(
        "========== AUDIO INTELLIGENCE =========="
    )


    print(
        f"Confidence: {result.confidence:.2f}"
    )


    print()

    print(
        "Labels:"
    )


    for label in result.labels:

        print(
            f"- {label.name}: {label.confidence:.2f}"
        )



if __name__ == "__main__":

    main()