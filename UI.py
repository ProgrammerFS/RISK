from flask import Flask, render_template, request, redirect
#from compare2 import get_changes
from compare2 import get_changes
import json

app = Flask(__name__)


def format_text(text):
    formatted_text = ""
    sections = text.split('* **')
    print(text)

    for section in sections[1:]:
        print(section)
        heading, *points = section.strip().split('*')
        formatted_text += f"<br><strong>{heading.strip()}</strong><ul>"
        
        for point in points:
            print(point)
            if point.strip():
                formatted_text += f"<li>{point.strip()}</li>"

        formatted_text += "</ul>"
    print(formatted_text)
    return formatted_text


@app.route('/')
def index():
    return render_template('upload.html')

# @app.route("/test")
# def test():
#     if request.method == "POST":
#         if 'newfile' not in request.files and 'oldfile' not in request.files:
#             return "Please Upload Correct Files"
        
#         new_file = request.files['newfile']
#         old_file = request.files['oldfile']
        
#         if new_file.filename == '' and old_file.filename == "":
#             return "No selected file"
        
#         # Save the uploaded file to a desired location
#         new_file.save('uploads/' + new_file.filename)
#         old_file.save('uploads/' + old_file.filename)
#         changes = get_changes
    

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == "POST":
        if 'newfile' not in request.files and 'oldfile' not in request.files:
            return "Please Upload Correct Files"
        
        new_file = request.files['newfile']
        old_file = request.files['oldfile']
        
        if new_file.filename == '' and old_file.filename == "":
            return "No selected file"
        
        # Save the uploaded file to a desired location
        new_file.save('uploads/' + new_file.filename)
        old_file.save('uploads/' + old_file.filename)
        # with open('1.json', 'r') as openfile:
        #     changes = json.load(openfile) 
        changes = get_changes(f"uploads/{new_file.filename}", f"uploads/{old_file.filename}")
        # print(changes)
        # t = format_text(changes)
        # print(t)
        # t = ""
        # if t == "":
        #     return changes
        # return t
        # l = changes["Modified"][list(changes["Modified"].keys())]
        # print(l)
        return render_template("disp2.html", summary = changes)
        return changes
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run()
