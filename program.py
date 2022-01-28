#!/usr/bin/python
# Name                      : Paveetheran A/L Thinagaran
# Date                      : 18/01/2022
# File                      : program.py
# Programming Language      : Python 

# Syntax to run this program.py
# -------------------------------
# $ python program.py ./testcase1
# or 
# $ python program.py ./testcase2


# Import Library
import sys
import os

# Get directory path from command-line arguments
def get_directory_path():
    # Set index 1 to fetch the path
    directory_path = sys.argv[1]
    return directory_path

# Scan all possible sub-directories
def scan_entire_directory(directory_path):
    # Create empty list
    text_files = []

    # Scan all avaiable text file
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Adding path of text file into list 
            text_files.append(os.path.join(root,file))

    return text_files

# Get text file name without extension
def extract_text_file_name(text_file_path):
    # Separate the root path and text file name
    text_file_name = os.path.split(text_file_path)
    # Remove ".txt" extension
    rm_extension = os.path.splitext(text_file_name[1])[0]

    return rm_extension

# Sorting ascending order based on the content in the text files
def read_textfiles(paths):
    # Create empty list
    text_files_list = []

    # 1. Read the text file
    # 2. Insert the text file name only and its content
    for path in paths:
        # Create empty dictionary in every iteration
        text_file_dict = {}    
        # Read the text file content
        f = open(str(path), "r")
        get_content = f.readline()
        f.close()

        # Append generated dictionary into list
        text_file_dict['text_file'] = str(extract_text_file_name(path))
        text_file_dict['content'] = int(get_content)
        text_files_list.append(text_file_dict)

    # Sorting ascending order based on the number contain in the text files
    text_files_list.sort(key=lambda x: x.get('content'))
    # Assign the text_files_list into sorted_text
    sort_text_files_list = text_files_list

    # Create empty string
    output_concat = ''

    # Concat each text file name
    for sort_text_file_list in sort_text_files_list:
        output_concat = output_concat + sort_text_file_list['text_file']

    print ("Output\t: " + output_concat)

def main():
    directory_path = get_directory_path()
    scan_subdir = scan_entire_directory(directory_path)
    read_textfiles(scan_subdir)

# Run code
main()