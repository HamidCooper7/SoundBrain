from uuid import uuid4

from brain.rag.loader import load_documents
from brain.rag.splitter import split_documents
from brain.rag.vectordb import collection

BATCH_SIZE = 64


def build_database(data_path: str):

    print("=" * 80)
    print("CLEARING DATABASE")
    print("=" * 80)

    print("Delete data/chroma manually before rebuilding.")
    print()

    print("=" * 80)
    print("LOADING DOCUMENTS")
    print("=" * 80)

    docs = load_documents(data_path)
    print(f"Loaded {len(docs)} documents")

    print()
    print("=" * 80)
    print("SPLITTING")
    print("=" * 80)

    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]
    ids = [str(uuid4()) for _ in chunks]

    print()
    print("=" * 80)
    print("ADDING TO CHROMA")
    print("=" * 80)

    total = len(chunks)

    for i in range(0, total, BATCH_SIZE):

        collection.add(
            ids=ids[i:i + BATCH_SIZE],
            documents=texts[i:i + BATCH_SIZE],
            metadatas=metadatas[i:i + BATCH_SIZE],
        )

        print(f"Added {min(i + BATCH_SIZE, total)}/{total}")

    print()
    print("=" * 80)
    print("DATABASE BUILD COMPLETE")
    print("=" * 80)

    return total