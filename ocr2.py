# import fitz  # PyMuPDF

# def get_text_pdf(input_path, output_path, text_to_highlight):
#     doc = fitz.open(input_path)
#     for page_number in range(doc.page_count):  # Choose the page number to highlight (0-based index)
#         page = doc[page_number]
        
#         # Search for text and create a highlight annotation
#         text_instances = page.searchFor(text_to_highlight)
#         for inst in text_instances:
#             highlight = page.addHighlightAnnot(inst)
        
#         # Save the modified PDF
#         doc.save(output_path)
#         doc.close()

# input_pdf = 'input.pdf'   # Replace with the path to your input PDF
# output_pdf = 'output.pdf'  # Replace with the path to your output PDF
# text_to_highlight = 'example text'  # Replace with the text you want to highlight

# highlight_pdf(input_pdf, output_pdf, text_to_highlight)

import pdfplumber  # PyMuPDF

def extract_text_under_sections(pdf_path, section_names):
    extracted_sections = {}

    with pdfplumber.open(pdf_path) as pdf:
        for page_number in range(len(pdf.pages)):
            page = pdf.pages[page_number]
            page_text = page.extract_text()

            for section_name in section_names:
                if section_name in page_text:
                    section_start = page_text.index(section_name)
                    next_section_index = page_text.find(section_name, section_start + 1)

                    if next_section_index == -1:
                        next_section_index = len(page_text)

                    section_text = page_text[section_start + len(section_name):next_section_index].strip()

                    if section_name not in extracted_sections:
                        extracted_sections[section_name] = []

                    extracted_sections[section_name].append(section_text)

    return extracted_sections

pdf_file = 'Pillar 2 - NEW.pdf'  # Replace with the path to your PDF file
section_names = [
"Introduction and Purpose ",
"ICAAP Executive Summary ",
"ICAAP Governance ",
"ICAAP Methodology, Scope and Use Test ",
"Capital Planning ",
"Material Risks ",
"ICAAP Stress Test and Reverse Stress Test ",
"ICAAP Submission and Approval ",
"Internal Control Review ",
"Frequently-Asked Questions (FAQ) ",
"Appendices "
]

extracted_sections = extract_text_under_sections(pdf_file, section_names)

for section_name, section_texts in extracted_sections.items():
    print(f"{section_name}:\n")
    for idx, text in enumerate(section_texts, start=1):
        print(f"Subsection {idx}:\n{text}\n{'=' * 30}")

