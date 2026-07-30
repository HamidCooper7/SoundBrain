from __future__ import annotations

import logging
from uuid import uuid4

from brain.rag.loader import load_documents
from brain.rag.splitter import split_documents
from brain.rag.vectordb import collection


logger = logging.getLogger(__name__)


BATCH_SIZE = 64


def build_database(data_path):

    logger.info("Loading documents...")
    docs = load_documents(data_path)
    logger.info("Loaded %d documents", len(docs))

    logger.info("Splitting...")
    chunks = split_documents(docs)
    logger.info("Created %d chunks", len(chunks))

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]
    ids = [str(uuid4()) for _ in chunks]

    logger.info("Adding to Chroma...")

    total = len(chunks)

    for i in range(0, total, BATCH_SIZE):

        collection.add(
            ids=ids[i:i + BATCH_SIZE],
            documents=texts[i:i + BATCH_SIZE],
            metadatas=metadatas[i:i + BATCH_SIZE],
        )

        logger.info("Added %d/%d", min(i + BATCH_SIZE, total), total)

    logger.info("Done!")

    return total