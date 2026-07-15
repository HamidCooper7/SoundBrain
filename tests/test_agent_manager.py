from brain.agents.agent_manager import AgentManager


manager = AgentManager()

questions = [
    "How do I master my song?",
    "Why does my mix sound muddy?",
    "What is LUFS?",
    "How do I use a limiter?",
    "What is EQ?",
    "Explain stereo imaging.",
    "What is gain staging?",
]

for q in questions:

    print("=" * 70)
    print(q)
    print()

    answer = manager.run(q)

    print(answer)
    print()