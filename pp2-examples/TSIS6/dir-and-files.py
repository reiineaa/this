#Task 1
import os

def list_files(path):
    directories = []
    files = []
    all_files = []

    for root, dirs, filenames in os.walk(path):
        directories.extend(dirs)
        files.extend(filenames)
        all_files.extend([os.path.join(root, filename) for filename in filenames])

    print("Directories:", directories)
    print("Files:", files)
    print("All files:", all_files)

path = '.'
list_files(path)

#Task 2
import os
import stat

def check_access(path):
    if os.path.exists(path):
        print("Path exists:", path)
    else:
        print("Path does not exist:", path)

    if os.path.isfile(path):
        print("Path is a file:", path)
    elif os.path.isdir(path):
        print("Path is a directory:", path)
    else:
        print("Path is neither a file nor a directory:", path)

    if os.access(path, os.F_OK):
        print("Path is accessible:", path)
    else:
        print("Path is not accessible:", path)

    if os.access(path, os.R_OK):
        print("Path is readable:", path)
    else:
        print("Path is not readable:", path)

    if os.access(path, os.W_OK):
        print("Path is writable:", path)
    else:
        print("Path is not writable:", path)

    if os.access(path, os.X_OK):
        print("Path is executable:", path)
    else:
        print("Path is not executable:", path)

path = '.'
check_access(path)

#Task 3
import os

def get_filename_directory(path):
    if os.path.exists(path):
        print("Path exists:", path)
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist:", path)

path = '.'
get_filename_directory(path)

#Task 4
def count_lines(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        print("Number of lines:", len(lines))

file = 'test.txt'
count_lines(file)

#Task 5
def write_list_to_file(file, list):
    with open(file, 'w') as f:
        for item in list:
            f.write("%s\n" % item)

file = 'test.txt'
list = ['apple', 'banana', 'cherry']
write_list_to_file(file, list)

#Task 6
def generate_files(start, end):
    for i in range(start, end + 1):
        filename = chr(i + ord('A')) + '.txt'
        with open(filename, 'w') as f:
            f.write('This is file ' + filename)

generate_files(ord('A'), ord('Z'))

#Task 7
import shutil

def copy_file(src, dest):
    if os.path.exists(src):
        print("Source file exists:", src)
        if os.access(src, os.F_OK):
            print("Source file is accessible:", src)
            shutil.copyfile(src, dest)
            print("File copied from", src, "to", dest)
        else:
            print("Source file is not accessible:", src)
    else:
        print("Source file does not exist:", src)

src = 'test.txt'
dest = 'copy_of_test.txt'
copy_file(src, dest)

#Task 8
import os

def delete_file(path):
    if os.path.exists(path):
        print("Path exists:", path)
        if os.access(path, os.F_OK):
            print("Path is accessible:", path)
            os.remove(path)
            print("File deleted:", path)
        else:
            print("Path is not accessible:", path)
    else:
        print("Path does not exist:", path)

path = 'test.txt'
delete_file(path)