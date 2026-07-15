from brain.rag.marker_loader import load_pdf

docs = load_pdf(r"data/manual/FabFilter/ffproq4-manual.pdf")

print(len(docs))
print(docs[0]["text"][:500])