import PyPDF2
import difflib
import spacy
from highlight import get_sections

nlp = spacy.load("en_core_web_sm")


pdf_file_1 = open("Pillar 2 - NEW.pdf", "rb")
pdf_file_2 = open("Pillar 2 - OLD.pdf", "rb")

pdf_reader_1 = PyPDF2.PdfReader(pdf_file_1)
pdf_reader_2 = PyPDF2.PdfReader(pdf_file_2)

pdf_pages_1 = pdf_reader_1.pages
pdf_pages_2 = pdf_reader_2.pages
num_pages_1 = len(pdf_pages_1)
num_pages_2 = len(pdf_pages_2)
length = num_pages_1
if num_pages_1 < num_pages_2:
    print("change in no. of pages by: ", abs(num_pages_1 - num_pages_2))
    
elif num_pages_1 == num_pages_2:
    print("no change in no. of pages")
else:
    print("change in no. of pages by: ", abs(num_pages_1 - num_pages_2))
    length = num_pages_2

s1 = ""
s2 = ""

for page_num in range(length):
    f1p1 = pdf_pages_1[page_num]
    s1 += f1p1.extract_text()
    f2p1 = pdf_pages_2[page_num]
    s2 += f2p1.extract_text()

sections = get_sections("Pillar 2 - NEW.pdf", 14, 17)


def identify_headings(text):
    doc = nlp(text)
    headings = []
    #fetch sentences and then check those for title case to identify headings
    for token in doc:
        # Identify tokens with titlecase formatting as potential headings
        if token.is_title and token.is_alpha:
            headings.append(token.text)

    return headings


lines1 = s1.splitlines()
lines2 = s2.splitlines()
diff = []
if len(lines1) <= len(lines2):
    length = len(lines1)
    extra_arr = lines2[length:]
else:
    length = len(lines2)
    extra_arr = lines1[length:]

for i in range(length):
    t1 = nlp(lines1[i])
    t2 = nlp(lines2[i])
    score = t1.similarity(t2)
    if score < 0.9:
        diff.append("Removed : " + lines1[i] )
        diff.append("Added : " + lines2[i])
for i in extra_arr:
    diff.append("Added : " + i)





output_filename = "differences.txt"
with open(output_filename, "w") as f:
    for i in diff:
        f.write(i + "\n")


pdf_file_1.close()
pdf_file_2.close()

# new_keys = list(d_new.keys())
# old_keys = list(d_old.keys())

# new_values = list(d_new.values())
# old_values = list(d_old.values())

# new_len = len(new_keys)
# old_len = len(old_keys)
# old_extra = 0
# new_extra = 0
# if new_len <= old_len:
#     min_len = new_len
#     old_extra = old_keys[min_len: ]
# else:
#     min_len = old_len
#     new_extra = new_keys[min_len: ]



# if old_extra != 0:
#     for i in old_extra:
#         changes[i] = ["Removed : " + x for x in d_old[i]]

# if new_extra != 0:
#     for i in new_extra:
#         changes[i] = ["Removed : " + x for x in d_new[i]]     

# print(changes)