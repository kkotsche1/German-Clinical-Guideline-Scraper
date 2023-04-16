import os
import PyPDF2
from tqdm import tqdm
import re

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        try:
            text = re.split("Literaturverzeichnis", text, flags=re.IGNORECASE)
            if len(text) != 3:
                print("NOT LEN 3  ", pdf_path)

            text = text[1]
        except:
            print("EXCEPT   ", pdf_path)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

# Example usage:
pdf_folder = "C:/Users/Admin/PycharmProjects/Leitlinien_scraper/pdf_files"
txt_folder = "C:/Users/Admin/PycharmProjects/Leitlinien_scraper/txt_files"
if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)
for filename in tqdm(os.listdir(pdf_folder)):
    if filename.endswith('.pdf'):
        if "Diabetes" in filename:
            if "abgelaufen" not in filename and "ungueltig" not in filename:
                try:
                    pdf_path = os.path.join(pdf_folder, filename)
                    txt_path = txt_folder + "/" + filename.replace(".pdf", ".txt")
                    pdf_to_txt(pdf_path, txt_path)
                    print(txt_path)
                except:
                    print(filename)