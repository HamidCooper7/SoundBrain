from brain.chat import chat

question = "Parallel Compression چیست؟"

answer = chat(question)

with open(
    "answer.txt",
    "w",
    encoding="utf-8",
) as f:
    f.write(answer)

print("Answer saved to answer.txt")