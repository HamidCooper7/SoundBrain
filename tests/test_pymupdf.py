import fitz

doc = fitz.open(r"E:\SoundBrain\data\courses\sound and psychoacoustics\01 - Physics of Sound\1. Physics of Sound_1.pdf")

page = doc.load_page(0)

text = page.get_text()

print(text)