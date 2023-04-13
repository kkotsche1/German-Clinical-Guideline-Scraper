import os
import PyPDF2
from tqdm import tqdm

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

# Example usage:
pdf_folder = "C:/Users/Admin/PycharmProjects/Leitlinien/pdf_files"
txt_folder = "C:/Users/Admin/PycharmProjects/Leitlinien/txt_files"
if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)
for filename in tqdm(os.listdir(pdf_folder)):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)
        txt_path = os.path.join(txt_folder, os.path.splitext(filename)[0] + '.txt')
        pdf_to_txt(pdf_path, txt_path)