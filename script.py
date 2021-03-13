import pdfplumber, re

with pdfplumber.open('NIO.pdf') as pdf:
    page = pdf.pages[11]
    text = page.extract_text()

print(text)

cash_re = re.compile()
