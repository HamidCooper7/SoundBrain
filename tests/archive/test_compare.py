from __future__ import annotations

from brain.audio.analysis.models import AnalysisResult

from brain.audio.comparison import (
    AudioComparator,
    ComparisonReportBuilder,
)

from brain.audio.comparison.interpreter import (
    ComparisonInterpreter,
)


def create_analysis(
    *,
    lufs: float,
    peak: float,
    rms: float,
    dynamic: float,
    width: float,
) -> AnalysisResult:

    return AnalysisResult(
        tempo=140.0,
        pitch=87.18,
        key="C",

        lufs=lufs,
        peak=peak,
        rms=rms,

        dynamic_range=dynamic,
        crest_factor=dynamic,

        stereo_width=width,
        phase=0.55,

        spectral_centroid=2500.0,
        spectral_bandwidth=2900.0,
        spectral_rolloff=5200.0,

        spectral_flatness=0.001,
        spectral_contrast=22.0,

        zero_crossing_rate=0.055,

        mfcc=[0.0] * 20,
        chroma=[0.0] * 12,

        onset_count=960,
    )


def main():

    reference = create_analysis(
        lufs=-10.5,
        peak=0.80,
        rms=0.24,
        dynamic=13.8,
        width=0.42,
    )

    current = create_analysis(
        lufs=-9.5,
        peak=1.03,
        rms=0.27,
        dynamic=12.8,
        width=0.24,
    )

    comparator = AudioComparator()

    comparison = comparator.compare(
        reference=reference,
        current=current,
    )

    interpreter = ComparisonInterpreter()

    report = interpreter.build(
        comparison,
    )

    builder = ComparisonReportBuilder()

    print()
    print(
        builder.build(
            report,
        )
    )


if __name__ == "__main__":
    main()