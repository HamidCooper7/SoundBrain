from brain.evaluator import evaluate

context = """
EQ removes unwanted frequencies.
"""

print(
    evaluate(
        "What is EQ?",
        "EQ removes unwanted frequencies.",
        context
    )
)

print(
    evaluate(
        "What is EQ?",
        "EQ is a compressor.",
        context
    )
)