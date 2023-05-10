from pdfminer.high_level import extract_text

text = extract_text('data/pdf_sample/one.pdf')
print(repr(text))
