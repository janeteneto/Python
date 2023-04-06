import os
import shutil

# prints message to terminal
os.system('echo "Hello world!"')

# os module to manipulate directories:

# 1. directory
directory = "test_dir"

# 2. path to parent dir
parent_dir = "C:/Users/user/pythonProject"

# 3. path - that's where it will be made
path = os.path.join(parent_dir, directory)
"""
# 4. create the dir
os.mkdir(path)
print("directory '% s' created" % directory)
"""

# put a file in the new directory
filename = "testfile.tt"
filepath = os.path.join(path, filename)

with open(os.path.join(path, filename), "w") as file1:
    toFile = "content of the file is written here"
    file1.write(toFile)
print("File " + filename + " created in " + directory + " folder")
