'''
Write a python program to print the contents of a directory using the os module. 
Search online for the function which does that.
'''

import os

# provide the directory path
path = '/'

# list all the files and directories in the given path
files_and_directories = os.listdir(path)

# print the list of files and directories
for file_or_directory in files_and_directories:
    print(file_or_directory)
    