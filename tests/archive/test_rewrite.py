from brain.memory import add
from brain.rewrite import rewrite

add("User", "What is sound?")
add("Assistant", "Sound is a mechanical wave.")

print(
    rewrite(
        "Explain it more."
    )
)