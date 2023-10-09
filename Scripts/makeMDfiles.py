import os

'''
Script to create new markdown files for each paper. This is required for the Annotator plugin.

'''

# Specify the directory where the vault is located. NOT the papers, but where both folders are
root_directory = "C:/Users/Danny/Documents/Repos/Paper notes"

# Specify the directory of the paper PDFs AFTER they've been reorganised by Mendelay
paper_directory = f"{root_directory}/Papers"
# Specify the output directory, where the MD files will be placed
out_directory = f"{root_directory}/Annotations"

# Initialize an empty list to store the modified filenames
result_list = []

for foldername, subfolders, filenames in os.walk(paper_directory):
    for filename in filenames:
        # Try to make a markdown file for each paper, if one doesn't already exist.
        try:
            modified_filename = filename
            modified_filename = modified_filename.replace(".pdf", ".md")

            # Create the full file path
            full_path = os.path.join(out_directory, modified_filename)

            result_list.append(full_path)
            os.makedirs(out_directory, exist_ok=True)
            # Checks if the file already exists and makes one if not
            if not os.path.isfile(out_directory + "/" + modified_filename):
                with open(out_directory + "/" + modified_filename, 'w+') as new_file:
                    new_file.write("---\n")
                    new_file.write("annotation-target: Papers\\" + os.path.basename(filename) + "\n")
                    new_file.write("---")
                print("Created " + out_directory + "/" + modified_filename)
            else:
                # Prints out that it already exists
                print(out_directory + "/" + modified_filename + " already exists")
        except:
            # Catchall statement - this shouldn't appear. Check your directories and consult Danny if all else fails
            print(f"Could not write {filename}, check code" + "\n")

