import os
import re

# Set the path of the directory containing the text files
dir_path = "./txt_files"

# Set the name of the output file
output_file = "merged_clinical_guidelines_v2" \
              ".txt"

# Open the output file in append mode
with open(output_file, "a", encoding='utf-8') as f_out:

    # Iterate over all files in the directory
    for file_name in os.listdir(dir_path):

            # Open the file in read mode
            with open(os.path.join(dir_path, file_name), encoding='utf-8') as f_in:

                # Read the contents of the file and write them to the output file
                #Using re.sub() to remove in text reference numbers
                f_out.write(re.sub(r'\[\d+\]', '', f_in.read()))