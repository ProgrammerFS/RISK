import fitz  # PyMuPDF

def extract_text_under_section(page, y0, y1):
    text_instances = page.get_text("textlines")
    section_text = ""

    for instance in text_instances:
        bbox = instance[0]  # Bounding box (x0, y0, x1, y1) of the text instance
        if y0 <= bbox[3] <= y1:
            section_text += instance[4] + "\n"

    return section_text.strip()

def identify_sections(pdf_path, min_font_size, max_font_size):
    doc = fitz.open(pdf_path)
    
    sections = []

    for page_number in range(doc.page_count):
        page = doc[page_number]
        text_instances = page.get_text("textlines")
        
        for instance in text_instances:
            size = instance[1][1]  # Font size
            if min_font_size < size < max_font_size:
                section_name = instance[4]  # Text content
                y0, y1 = instance[0][1], instance[0][3]  # Bounding box coordinates

                next_section = None
                for next_instance in text_instances:
                    next_size = next_instance[1][1]
                    if size < next_size and y0 < next_instance[0][1]:
                        next_section = next_instance
                        break

                if next_section is not None:
                    section_text = extract_text_under_section(page, y0, next_section[0][1])
                else:
                    section_text = extract_text_under_section(page, y0, y1)

                sections.append({'name': section_name, 'text': section_text})
            
    doc.close()
    return sections

def get_sections(pdf_path, min_font_size, max_font_size):
    sections = identify_sections(pdf_path, min_font_size, max_font_size)
    for section in sections:
        section_name = section['name']
        section_text = section['text']
        print(f"Section: {section_name}")
        print(f"Text: {section_text}\n{'=' * 30}")

pdf_file = "Pillar 2 - NEW.pdf"  # Replace with the path to your PDF file
min_font_size = 14
max_font_size = 17

get_sections(pdf_file, min_font_size, max_font_size)
