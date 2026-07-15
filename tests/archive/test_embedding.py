from brain.embedding import get_embedding_model

model = get_embedding_model()

embedding = model.encode("What is gain staging?")

print("=" * 60)
print(f"Embedding dimension: {len(embedding)}")
print("=" * 60)
print(embedding[:10])