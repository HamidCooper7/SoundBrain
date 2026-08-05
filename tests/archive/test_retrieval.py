from brain.rag.vectordb import collection

print("=" * 80)
print("QUERY")
print("=" * 80)

query = "Parallel Compression چیست؟"
print(query)

print("\nSearching...\n")

results = collection.query(
    query_texts=[query],
    n_results=5,
)

print("=" * 80)
print("RESULTS")
print("=" * 80)

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"\n========== RESULT {i} ==========\n")
    print(doc[:2000])

print("\nDone.")