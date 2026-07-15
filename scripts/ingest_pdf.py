import fitz

pdf_path = input("PDF Path: ").strip()

doc = fitz.open(pdf_path)

print("=" * 60)
print(f"Pages : {len(doc)}")
print("=" * 60)

for i, page in enumerate(doc):
    print(f"\n----- Page {i+1} -----\n")
    print(page.get_text())

print("\nFinished ✅")