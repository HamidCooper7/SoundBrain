from pprint import pprint

from brain.rag.retriever import retrieve
from brain.rag.reranker import rerank

docs = retrieve(
    "What is Compressor Threshold?",
    k=10,
)

results = rerank(
    "What is Compressor Threshold?",
    docs,
)

pprint(results)