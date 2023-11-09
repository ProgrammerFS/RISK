from highlight import get_sections
import re
import difflib
import google.generativeai as palm
import json

API = "API KEY"

def summarize_topic(dict1):
    palm.configure(api_key=API)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = f"list all the major/critical/important points in this section you can ignore the introductory points but just capture the very critical points which will help the risk team if you identify an subsections please summarize them as well : {dict1}"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=100000,
    )
    x = completion.result
    print(x)
    return x

def get_html(text):
    palm.configure(api_key=API)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = f"Please re-write this in html format just display it point wise : {text}"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=100000,
    )
    return completion.result


def get_changes(pdf_path_new, pdf_path_old):
    differ = difflib.Differ()
    pattern = r'\d+\. '

    sections_new = get_sections(pdf_path_new, 14, 17)
    sections_old = get_sections(pdf_path_old, 14, 17)

    d_new = {}
    d_old = {}
    errors = []
    sum_changes = {}
    for i in sections_new:
        l = sections_new[i]
        d_new[i] = []
        matches = re.findall(pattern, "".join(l))

        x = []
        for match in matches:
            try:
                x.append(l.index(match))
            except:
                errors.append(match)
        temp_d = {i : []} 
        s = ""
        for j in range(len(l)):
            if j in x and s!="":
                temp_d[i].append(s)
                s = ""
            s += l[j]
        temp_d[i].append(s)
        d_new[i].append(summarize_topic(''.join(temp_d[i])))
        

    for i in sections_old:
        l = sections_old[i]
        d_old[i] = []
        matches = re.findall(pattern, "".join(l))

        x = []
        for match in matches:
            try:
                x.append(l.index(match))
            except:
                errors.append(match)
        temp_d = {i : []} 
        s = ""
        for j in range(len(l)):
            if j in x and s!="":
                temp_d[i].append(s)
                s = ""
            s += l[j]
        temp_d[i].append(s)
        d_old[i].append(summarize_topic(''.join(temp_d[i])))
    summary = {}
    summary["New"] = []
    summary["Old"] = []
    summary["Added"] = []
    summary["Removed"] = []
    for i in range(max(len(list(d_new.keys())), len(list(d_old.keys())))):
        x = d_new.get(list(d_new.keys())[i], None)
        if i < len(list(d_old.keys())):
            y = d_old.get(list(d_old.keys())[i], None)
        else:
            y = None
        if x!=None and y!= None:
            summary["New"].append({list(d_new.keys())[i]:x})
            summary["Old"].append({list(d_old.keys())[i]:y})
        elif x!=None and y == None:
            summary["Added"].append({list(d_new.keys())[i] : x})
        else:
            summary["Removed"].append({list(d_old.keys())[i] : y})
    with open("1.json", "w") as f:
        j = json.dumps(summary)
        f.write(j)
    print(summary)
    return summary

            

#get_changes("Pillar 2 - NEW.pdf", "Pillar 2 - OLD.pdf")
