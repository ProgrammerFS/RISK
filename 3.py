import difflib
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import google.generativeai as palm
from sum import gen_sum

API = "AIzaSyBkQBKS8Reo8Iue8yZLlWJitzODLsOcQmg"

def summarize_topic(dict1):
    palm.configure(api_key=API)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = f"list all the major/critical/important points in this section : {dict1}"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=100000,
    )
    x = completion.result
    print(x)
    return x

def summarize_changes(new_dict, old_dict):
    palm.configure(api_key=API)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = f"List all major changes in points of the new_file when compared to the old_file not in table format : {new_dict}, old_file : {old_dict}"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=20000,
    )
    return completion.result

pdf_file_1 = open("./Pillar 2 - NEW.pdf", "rb")
pdf_file_2 = open("./Pillar 2 - OLD.pdf", "rb")

pdf_reader_1 = PyPDF2.PdfReader(pdf_file_1)
pdf_reader_2 = PyPDF2.PdfReader(pdf_file_2)

pdf_pages_1 = pdf_reader_1.pages
pdf_pages_2 = pdf_reader_2.pages
num_pages_1 = len(pdf_pages_1)
num_pages_2 = len(pdf_pages_2)
length = num_pages_2
if num_pages_1 > num_pages_2:
    print("change in no. of pages by: ", abs(num_pages_1 - num_pages_2))
elif num_pages_1 == num_pages_2:
    print("no change in no. of pages")
else:
    print("change in no. of pages by: ", abs(num_pages_1 - num_pages_2))
    length = num_pages_1

text1 = ""
text2 = ""

for page_num in range(length):
    f1p1 = pdf_pages_1[page_num]
    text1 += f1p1.extract_text()
    f2p1 = pdf_pages_2[page_num]
    text2 += f2p1.extract_text()


# Function to preprocess the text
def preprocess_text(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in words if word.isalpha()]
    
    # Remove stopwords (common words with little meaning)
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)

# Step 2: Preprocess the text
preprocessed_text1 = preprocess_text(text1)
preprocessed_text2 = preprocess_text(text2)

# Step 3: Text comparison
differ = difflib.Differ()
diff_results = list(differ.compare(preprocessed_text1.splitlines(), preprocessed_text2.splitlines()))

# Step 4: Identify changes
added_sections = []
deleted_sections = []
modified_sections = []


for line in diff_results:
    if '+ ' in line:
        added_sections.append(line)
    elif '- ' in line:
        deleted_sections.append(line)
    elif '? ' in line:
        modified_sections.append(line)

print(added_sections[0])
# Step 5: Summarize changes
summary_report = f"""
Summary Report of Changes
-------------------------

Added Sections:
{gen_sum(added_sections[0])}

Deleted Sections:
{deleted_sections}

Modified Sections:
{modified_sections}
"""



# Step 6: Generate a report
with open('summary_report.txt', 'w') as report_file:
    report_file.write(summary_report)

print("Summary report generated successfully.")

