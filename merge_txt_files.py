import os

# Set the path of the directory containing the text files
dir_path = "./txt_files"

# Set the name of the output file
output_file = "merged_clinical_guidelines_short" \
              ".txt"

# Open the output file in append mode
with open(output_file, "a", encoding='utf-8') as f_out:

    # Iterate over all files in the directory
    for file_name in os.listdir(dir_path):

        # Check if the file is a text file
        if "Diabetes" in file_name:
            print(file_name)
            # Open the file in read mode
            with open(os.path.join(dir_path, file_name), encoding='utf-8') as f_in:

                # Read the contents of the file and write them to the output file
                f_out.write(f_in.read())