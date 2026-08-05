from brain.orchestration.orchestrator import Orchestrator


def main():

    orch = Orchestrator()

    state = orch.run(
        "What is Dynamic EQ?"
    )

    print()
    print("=" * 80)
    print("FINAL ANSWER")
    print("=" * 80)

    print(state.answer)


if __name__ == "__main__":

    main()