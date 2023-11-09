# import PyPDF2

# def extract_section_text(pdf_file_path, start_heading, end_heading):
#     with open(pdf_file_path, "rb") as pdf_file:
#         pdf_reader = PyPDF2.PdfReader(pdf_file)
#         section_text = ""
#         is_inside_section = False

#         for page in pdf_reader.pages:
#             page_text = page.extract_text()

#             if start_heading in page_text:
#                 is_inside_section = True
#                 section_text += page_text[page_text.index(start_heading):]

#             if is_inside_section:
#                 section_text += page_text

#             if end_heading in page_text:
#                 is_inside_section = False
#                 section_text = section_text[:section_text.index(end_heading)]

#     return section_text

# # Define the headings of the sections you want to compare
# old_heading = "Old Version Policy"
# new_heading = "New Version Policy"

# # Paths to your PDF files
# old_pdf_file_path = "./file.pdf"
# new_pdf_file_path = "./new_file.pdf"

# old_section_text = extract_section_text(old_pdf_file_path, old_heading, new_heading)
# new_section_text = extract_section_text(new_pdf_file_path, old_heading, new_heading)

# # Now you can compare the extracted sections using the method of your choice
# # For example, you can use spaCy or other text comparison techniques as shown previously

# # ... (Perform comparison and detect differences)

# # Finally, write the differences to a file
# output_filename = "differences.txt"
# with open(output_filename, "w") as f:
#     f.write("Detected Differences:\n")
#     f.write("=" * 50 + "\n")
#     for diff in differences:
#         f.write(" ".join(diff) + "\n")
#         f.write("=" * 50 + "\n")

# print(f"Detected {len(differences)} differences. Details written to '{output_filename}'.")


def format_text(text):
    formatted_text = ""
    sections = text.split('* **')

    for section in sections[1:]:
        heading, *points = section.strip().split('*')
        formatted_text += f"<br><strong>{heading.strip()}</strong><ul>"
        
        for point in points:
            if point.strip():
                formatted_text += f"<li>{point.strip()}</li>"

        formatted_text += "</ul>"

    return formatted_text

input_text = """* **The major/critical/important points in the introduction and purpose section of the new_file are:** * All banks licensed by the Central Bank of the UAE must ensure that Pillar 1 risks - credit, market, and operational risk - are mitigated by capital. * Each bank is required to have a process to assess its overall capital adequacy as a function of its risk profile and its strategy. * The Central Bank analyses the capitalisation levels of banks among other information, referring to the results of the ICAAP with regard to the internal view of capital adequacy. * This Guidance presents minimum expected practices to be considered by each bank in order to undertake their ICAAP, covering the process, content, outcome, and usage. * It also intends to support each bank in the identification, measurement, reporting, and mitigation of Pillar 2 risks. * The Central Bank may apply proportionality for smaller and less complex banks when evaluating the ICAAP. * This Guidance serves several purposes. It (i) Explains in more detail the Central Bank’s expectations on fulfilling the requirements of the ICAAP Capital Standards, in particular, related to the ICAAP (process) at each bank and certain aspects of the content of the ICAAP report; (ii) Covers expectations on some processual elements of the ICAAP, such as an appropriate approval process of the ICAAP report and its submission timelines; and (iii) Formulates expectations about additional sections of the ICAAP report (e.g. related to internal audit findings and changes compared to the previous ICAAP report). * **The major/critical/important points in the ICAAP Executive Summary section of the new_file are:** * The executive summary of the ICAAP document should explain the views of Senior Management and the Board on the suitability of the bank’s capital to cover the risks faced by the bank in light of its risk profile, its risk appetite and its future business plans. * The executive summary should contain the following elements: * The main findings of the ICAAP * A brief description of the ICAAP governance framework * A brief presentation of the bank’s structure, subsidiaries, businesses, material risks, risk appetite, and risk mitigating actions, where applicable * A description of the current capital position of the bank showing the allocation of capital per risk type, covering Pillar 1 and Pillar 2 risks * A description of the current capital composition of the bank against minimum capital requirements covering at least CET1, AT1, and Tier 2 capital ratios * A forward-looking analysis of the budgeted capital position of the bank, based on the bank’s expected business plan over the next three (3) years, reflecting the current, and expected economic conditions. This needs to cover expected dividend distribution * An analysis of the capital position and capital ratios under several stress scenarios, the analysis of the stress scenarios should include the intended risk mitigation actions * An assessment of the adequacy of the bank’s risk management processes including critical judgment on the areas that need improvement * A conclusion of the ICAAP addressing the suitability of the capital to cover the bank’s current and expected risks * **The major/critical/important points in the ICAAP Governance section of the new_file are:** * The Board has ultimate ownership and responsibility of the ICAAP. It is required to approve an ICAAP on a yearly basis. The Board is also expected to approve the ICAAP governance framework with a clear and transparent assignment of responsibilities, adhering to the segregation of functions. The governance framework should ensure that the ICAAP is an integral part of the bank’s management process and decision-making. The ICAAP governance framework should include a clear approach to the regular internal review and validation by the appropriate functions of the bank. * **The major/critical/important points in the ICAAP Methodology, Scope and Use Test section of the new_file are:** * The ICAAP is an ongoing process. On an annual basis, every bank is required to submit a document outlining the outcome of the ICAAP to the Central Bank. * The ICAAP supplements the Pillar 1 minimum regulatory capital requirements by (i) identifying risks that are not addressed or not fully addressed through Pillar 1 regulations, referred to as Pillar 2 risks, and (ii) determining a level of capital commensurate with the level of risk. * The Central Bank requires each bank to adopt a Pillar 1 plus approach. According to this, the bank’s total capital requirements include the minimum Pillar 1 regulatory capital requirements, plus the capital required to cover Pillar 2 risks. As a result, the ICAAP should result in additional capital requirements specific to each bank’s business model. * Board"""
formatted_output = format_text(input_text)
print(formatted_output)
