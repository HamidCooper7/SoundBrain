from brain.audio.analysis import AudioAnalyzer
from brain.audio.context import AudioContextDetector
from brain.audio.io import AudioIOService


audio = AudioIOService().load(
    "music/test.wav"
)

analysis = AudioAnalyzer().analyze(
    audio
)

context = AudioContextDetector().detect(
    analysis
)

print(
    "========== AUDIO CONTEXT =========="
)

print(
    "Type:",
    context.audio_type
)

print(
    "Source:",
    context.source_type
)

print(
    "Instrument:",
    context.instrument
)

print(
    "Full Mix:",
    context.is_full_mix
)

print(
    "Confidence:",
    context.confidence
)

print(
    "Notes:"
)

for note in context.notes:
    print(
        "-",
        note
    )