from uuid import uuid4

from brain.rag.loader import load_documents
from brain.rag.splitter import split_documents
from brain.rag.vectordb import collection


BATCH_SIZE = 64


def build_database(data_path):

    print("Loading documents...")
    docs = load_documents(data_path)
    print(f"Loaded {len(docs)} documents")

    print("Splitting...")
    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]
    ids = [str(uuid4()) for _ in chunks]

    print("Adding to Chroma...")

    total = len(chunks)

    for i in range(0, total, BATCH_SIZE):

        collection.add(
            ids=ids[i:i + BATCH_SIZE],
            documents=texts[i:i + BATCH_SIZE],
            metadatas=metadatas[i:i + BATCH_SIZE],
        )

        print(f"Added {min(i + BATCH_SIZE, total)}/{total}")

    print("Done!")

    return total