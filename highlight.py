import fitz  # PyMuPDF
import google.generativeai as palm

API = "AIzaSyBkQBKS8Reo8Iue8yZLlWJitzODLsOcQmg"
palm.configure(api_key=API)
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
def summarize_topic(text):
    
    prompt = f"list all the important points in this section which will help the risk team if you find any sub sections please summarize them as well if anything contains risk in it please put that in: {text}"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.6,
        max_output_tokens=100000,
    )
    x = completion.result
    return x

def identify_sections(pdf_path, min_font_size, max_font_size):
    doc = fitz.open(pdf_path)
    
    sections = {}
    heading = ""

    for page_number in range(doc.page_count):
        page = doc[page_number]
        dict = page.get_text("dict")
        blocks = dict["blocks"]
        for block in blocks:
            if "lines" in block.keys():
                spans = block['lines']
                for span in spans:
                    data = span['spans']
                    for lines in data:
                        size = lines['size'] 
                        if size > min_font_size and size < max_font_size and len(lines['text']) > 6:
                            heading = lines['text'].strip()
                            sections[heading] = []
                        if size < min_font_size and heading!= '':
                            sections[heading].append(lines['text'])
            

    doc.close()
    return sections
def get_sections(pdf_path, min_font_size, max_font_size):
    pdf_file = pdf_path  # Replace with the path to your PDF file # Adjust this value to determine what constitutes a section title
    d = {}
    sections = identify_sections(pdf_file, min_font_size, max_font_size)
    for i in sections:
        if len(i) > 6 and "FAQ" not in i:
            # if i == "Material Risks":
            #     print(sections[i])
            d[i] = summarize_topic(sections[i])

    return d

d = get_sections("Pillar 2 - NEW.pdf",14,17)

with open("change.txt", "w") as f:
    for i in d:
        if d[i] != None:
            f.write(i + "\n")
            f.write(d[i] + "\n\n")
        else:
            f.write(i + ": Cannot be checked due to error, Please check this section \n\n")



