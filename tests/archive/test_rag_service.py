from brain.services import RAGService


def main():

    rag = RAGService()

    question = "What is Dynamic EQ?"

    result = rag.ask(question)

    print("=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(result["question"])

    print()

    print("=" * 80)
    print("DOCUMENTS")
    print("=" * 80)

    print(result["count"])

    print()

    print("=" * 80)
    print("CONTEXT")
    print("=" * 80)

    print(result["context"])


if __name__ == "__main__":
    main()