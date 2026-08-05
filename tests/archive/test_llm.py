from brain.llm import chat

answer = chat(
    [
        {
            "role": "user",
            "content": "سلام خودتو معرفی کن",
        }
    ]
)

print(answer)