from brain.tool_selector import select_tools

questions = [
    "Analyze my mix",
    "Check loudness",
    "Detect BPM",
    "Find musical key",
    "Analyze vocal pitch",
]

for q in questions:
    print("=" * 50)
    print(q)
    print(select_tools(q))