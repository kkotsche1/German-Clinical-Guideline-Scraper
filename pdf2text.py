import os
import PyPDF2
from tqdm import tqdm
import re

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:

        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    cropbox = page.cropbox
                    cropbox.lower_left = (cropbox.lower_left[0], cropbox.lower_left[1] + 100)
                    cropbox.upper_right = (cropbox.upper_right[0], cropbox.upper_right[1] - 100)
                    page.cropbox = cropbox
                    text += page.extract_text()
                    text1 = text

            if text.count("Abbildungsverzeichnis") >= 2:
                    text1 = re.split("Abbildungsverzeichnis", text, flags=re.IGNORECASE)
                    text1 = text1[1:len(text1) - 1]
                    text1 = " ".join(text1)

            elif text.count("Algorithmen") >= 2:
                    text1 = re.split("Algorithmen", text, flags=re.IGNORECASE)
                    text1 = text1[1:len(text1) - 1]
                    text1 = " ".join(text1)

            elif text.count("Anhang") >= 2:
                    text1 = re.split("Anhang", text, flags=re.IGNORECASE)
                    text1 = text1[1:len(text1) - 1]
                    text1 = " ".join(text1)

            elif text.count("Literaturverzeichnis") >= 2:
                    text1 = re.split("Literaturverzeichnis", text, flags=re.IGNORECASE)
                    text1 = text1[1:len(text1) - 1]
                    text1 = " ".join(text1)

            elif text.count("Literatur") >= 2:
                    text1 = re.split("Literatur", text, flags=re.IGNORECASE)
                    text1 = text1[1:len(text1)-1]
                    text1 = " ".join(text1)
            try:
                if len(text1.split("Literatur")) > 1:
                    text1 = " ".join(text1.split("Literatur")[:len(text1.split("Literatur"))-1])
            except:
                print("##############################################################################")

            try:
                if len(text1.split("Zielsetzung")) > 1:
                    text1 = " ".join(text1.split("Zielsetzung")[1:])
            except:
                print("##############################################################################")

            print(f"Original Length: {len(text)}, New Length: {len(text1)}      {pdf_path}")

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text1)

        except:
            print("DIDN'T WORK ", pdf_path)



# Example usage:
pdf_folder = "C:/Users/Admin/PycharmProjects/Leitlinien_scraper/pdf_files"
txt_folder = "C:/Users/Admin/PycharmProjects/Leitlinien_scraper/txt_files"
if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
            if "abgelaufen" not in filename and "ungueltig" not in filename:
                    pdf_path = os.path.join(pdf_folder, filename)
                    txt_path = txt_folder + "/" + filename.replace(".pdf", ".txt")
                    pdf_to_txt(pdf_path, txt_path)
