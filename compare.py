from highlight import get_sections
import re
import difflib
import google.generativeai as palm

API = "AIzaSyBkQBKS8Reo8Iue8yZLlWJitzODLsOcQmg"

def summarize_changes(new_dict, old_dict):
    palm.configure(api_key=API)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = f"Give only the major changes related to risk in these two files if things like market risks, business risks are present please include one line summary of that also : {new_dict}, old_file : {old_dict}"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.1,
        max_output_tokens=20000,
    )
    return completion.result

def get_main_changes(summ):
    palm.configure(api_key=API)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = f"Please give the major topics that were changed in this  : {summ}"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=20000,
    )
    return completion.result

def summarize_topic(dict1):
    palm.configure(api_key=API)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = f"list all the major/critical/important points in this section if things like market risks, business risks are present please include one line summary of that also: {dict1}"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=100000,
    )
    x = completion.result
    return x

def get_html(text):
    palm.configure(api_key=API)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = f"Please re-write this in html format : {text}"
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
        d_new[i].append(summarize_topic(temp_d))

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
        d_old[i].append(summarize_topic(temp_d))
        
    summary = summarize_changes(new_text=d_new, old_text=d_old)
    main_changes = get_main_changes(summary)
    print("Main changes : ", main_changes)

    with open("change.txt", "w") as f:
        # for i in summary:
        #     f.write(i + "\n")
        #     if summary[i] != None:
        #         f.write(summary[i])
        if summary!= None:
            f.write(summary)
            f.write("\n\n")
            f.write("Major changes : \n")
            f.write(main_changes)
        else:
            f.write("Something crashed")

    print("Summary written to file")
    # g_h = get_html(summary)
    # with open("/templates/disp.html", "w") as f:
    #     f.write(g_h)
    return summary






