from brain.audio.pipeline import analyze_audio


results = analyze_audio(
    "tests/audio.wav",
    analyses=[
        "pitch",
        "lufs",
        "bpm",
        "key",
        "spectrum",
    ],
)

print()

for name, result in results.items():
    print("=" * 40)
    print(name.upper())
    print("=" * 40)
    print(result)