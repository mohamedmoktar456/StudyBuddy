from pdf_extractor import extract_text_from_pdf

text = extract_text_from_pdf("sample.pdf")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text saved to output.txt")