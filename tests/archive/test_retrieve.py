from pprint import pprint

from brain.rag.retriever import retrieve


results = retrieve(
    "What is Compression Ratio?",
    k=3,
)

pprint(results)