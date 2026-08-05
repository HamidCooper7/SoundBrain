from brain.rag.loader import load_documents

docs = load_documents("data/courses")

print(docs[0].page_content)