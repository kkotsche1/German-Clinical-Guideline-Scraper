import os
import deepl
import time
from tqdm import tqdm
import dl_translate as dlt

# Set up the DeepL client
api_key = 'e39995ba-b706-6920-ea51-37f46c572a51:fx'

deepl_client = deepl.Translator(api_key)

# Read in the German text file
with open('merged_clinical_guidelines.txt', 'r', encoding='utf-8') as f:
    german_text = f.read()

# Split the German text into smaller chunks (maximum 5000 characters per request)
chunk_size = 5000
german_chunks = [german_text[i:i+chunk_size] for i in range(0, len(german_text), chunk_size)]
mt = dlt.TranslationModel()

# Translate each chunk and save the results to a new file
with open('merged_clinical_guidelines_english.txt', 'w', encoding='utf-8') as f:
    for chunk in tqdm(german_chunks):
        translated_chunk = mt.translate(chunk, source=dlt.lang.GERMAN, target=dlt.lang.ENGLISH)
        f.write(translated_chunk)