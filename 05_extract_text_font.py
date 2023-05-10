from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTAnno

for page_layout in extract_pages('data/pdf_sample/one.pdf'):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            for text_line in element:
                if not isinstance(text_line, LTChar) and not isinstance(text_line, LTAnno):
                    for character in text_line:
                        if isinstance(character, LTChar):
                            print(character.fontname)
                            print(character.size)
