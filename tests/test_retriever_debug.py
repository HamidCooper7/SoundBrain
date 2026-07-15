from brain.rag.retriever import retrieve

query = "Parallel Compression چیست؟"

print("=" * 80)
print("QUESTION")
print("=" * 80)
print(query)

print()

docs = retrieve(query, k=5)

print("=" * 80)
print("RETRIEVED DOCUMENTS")
print("=" * 80)

for i, doc in enumerate(docs, start=1):

    print(f"\n========== DOCUMENT {i} ==========\n")

    print(doc[:1500])

    print("\n")