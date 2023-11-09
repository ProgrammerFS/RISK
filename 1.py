import pdfplumber

def extract_text_under_sections(pdf_path, section_names):
    extracted_sections = {}

    with pdfplumber.open(pdf_path) as pdf:
        for page_number in range(len(pdf.pages)):
            page = pdf.pages[page_number]
            page_text = page.extract_text()

            for i in range(len(section_names)):
                if section_names[i] in page_text:
                    section_start = page_text.index(section_names[i])
                    next_section_index = page_text.find(section_names[i+1])
                    if i !=0:
                        prev_section_index = page_text.find(section_names[i-1])

                    if next_section_index == -1:
                        next_section_index = len(page_text)

                    section_text = page_text[section_start + len(section_names[i]):next_section_index].strip()

                    if section_names[i] not in extracted_sections:
                        extracted_sections[section_names[i]] = []

                    extracted_sections[section_names[i]].append(section_text)

    return extracted_sections

pdf_file = 'Pillar 2 - NEW.pdf'  # Replace with the path to your PDF file
section_names = [
"Introduction and Scope ",
"Definitions ",
"Importance of supervisory review ",
"Four key principles of supervisory review ",
"Specific issues to be addressed under the supervisory ",
"review process ",
"Other aspects of the supervisory review process ",
"Shari'ah Implementation ",
]

extracted_sections = extract_text_under_sections(pdf_file, section_names)

for section_name, section_texts in extracted_sections.items():
    print(f"{section_name}:\n")
    for idx, text in enumerate(section_texts, start=1):
        print(f"Subsection {idx}:\n{text}\n{'=' * 30}")
