from pathlib import Path

from brain.rag.builder import build_database
from brain.chat import chat


print("=" * 80)
print("BUILDING DATABASE")
print("=" * 80)

build_database(
    Path("data/manual/FabFilter")
)

print()
print("=" * 80)
print("CHAT TEST")
print("=" * 80)

while True:

    question = input("\nQuestion : ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = chat(question)

    print("\n")
    print("=" * 80)
    print("ANSWER")
    print("=" * 80)
    print(answer)