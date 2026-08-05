from brain.rag.loader import load_documents
from brain.rag.splitter import split_documents


docs = load_documents("data")

chunks = split_documents(docs)

print("=" * 60)
print(f"Documents : {len(docs)}")
print(f"Chunks    : {len(chunks)}")
print("=" * 60)

print(chunks[0].page_content)