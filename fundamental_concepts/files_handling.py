"""
    Python has several built-in modules and
    functions for handling files. These functions
    are spread out over several modules, such
    as `os`, `os.path`, `shutil`, `pathlib` and others.
"""

# 1. Python's "with open(...) as ..." Pattern

"""
    The pattern `with` guarantee automatic closing of the file
"""

# 1.1 Read the file content
with open("data.txt", 'r') as f:
    data = f.read()


# 1.2 Write something to the file
with open("data.txt", 'w') as f:
    txt = "Something..."

    f.write(txt)

# 1.3 Arguments of open

"""
    The following characters represents the file
    handling mode. The default and most common is 'r'.

    - 'r' Open and reading (default)
    - 'w' Open for writing, truncating (overwriting) the file first
    - 'rb' or 'wb' open in binary mode (read/write using byte data)
"""

# 2. Working with directories

"""
    The build-in `os` module has number of useful functions that can be used
    to list directory contents and filter the result, among other operations
"""

# 2.1 List directories

import os

# Here is list of directories
entries = os.listdir('fundamental_concepts/')

"""
    The `listdir` method is basic way to list directories. Otherwise,
    we can use `scandir` method, it basically get info about file such as
    size, name and others data.
"""

# Using `scandir`
entries = os.scandir("fundamental_concepts/")

# List directories
print([entry.name for entry in entries])

# Working with `pathlib`

from pathlib import Path

entries = Path("fundamental_concepts/")

# Same result
for entry in entries.iterdir():
    print(entry.name)

# 2.2 List all files

basepath = "fundamental_concepts/"

for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

# Using `scandir`
basepath = "fundamental_concepts/"

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

# Using `pathlib`
basepath = Path("fundamental_concepts/")

files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())

for item in files_in_basepath:
    print(item.name)

# 2.3 List subdirectories

"""
    To list subdirectories instead of file, use one the methods below.

    `os.listdir` or `os.path`
"""

basepath = "fundamental_concepts/"
subdirectories = []

for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        subdirectories.append(entry)

print("Subdirectories: ", subdirectories)

# Using `os.scandir`

basepath = "fundamental_concepts/"
subdirectories = []

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            subdirectories.append(entry.name)

print("Subdirectories: ", subdirectories)

# Using `pathlib`

basepath = Path("fundamental_concepts/")
subdirectories = []

for entry in basepath.iterdir():
    if entry.is_dir():
        subdirectories.append(entry.name)

print("Subdirectories: ", subdirectories)

# 2.4 Getting File Attributes

"""
    We can retrieve file attributes such
    as file size and modified time. This is
    done through `os.stat`, `os.scandir` or
    `pathlib`
"""

# Example

"""
    The example bellow show how to get time the files were last modified
"""

with os.scandir("fundamental_concepts/") as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(info.st_mtime)

# Made in `pathlib`

basepath = Path("fundamental_concepts/")

print("Done in pathlib")

for path in basepath.iterdir():
    info = path.stat()
    print(info.st_mtime)

# Improving getting info

from datetime import datetime

basepath = "fundamental_concepts/"

def convert_date(timestamp):
    current_date = datetime.utcfromtimestamp(timestamp)
    formatted_date = current_date.strftime("%d %b %Y")

    return formatted_date

def get_files():
    dir_entries = os.scandir(basepath)

    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()

            print(f'File: {entry.name}\t Last Modified: {convert_date(info.st_mtime)}')

if __name__ == '__main__':
    get_files()

# 3. Making directories

"""
    Below, we have different ways to create
    directories.

    - `os.mkdir` method creates a single subdirectory
    - `pathlib.Path.mkdir` method creates single or multiple directories
    - `os.makedirs` method creates multiple directories, including intermediate directories
"""

# 3.1 Creating single directory

# With `os.mkdir`
os.mkdir("example_directory/")

# With `pathlib`

""""
    Can use `exist_ok` arguments if already exist.
"""

path = Path('example_directory/')

try:
    path.mkdir(exist_ok=True)
except FileExistsError as file_exception:
    pass

# 3.2 Creating Multiple Directories

"""
    Very similar to `os.mkdir`, the different between the both
    is that not only can `os.makedirs` create individual directories.
"""

""""
    This method has default permissions for create directory. If we need
    to create directories with different permission call, must pass mode
    with the value `0o770`.
"""

os.makedirs("parent_folder/children_1/children_2", exist_ok=True)

# 4. Filename Pattern Matching

"""
    We will cover filename patterns, methods and functions for
    interaction. These are the methods and functions available
    to you:

    - `endswith()` and `startswith()` string methods
    - `fnmatch.fnmatch()`
    - `glob.glob()`
    - `pathlib.Path.glob`
"""

# 4.1 Using String methods

# Get .txt files
for f_name in os.listdir('example_directory/'):
    if(f_name.endswith('.txt')):
        print(f_name)

# 4.2 Using `fnmatch`

"""
    `fnmatch` has more advanced functions and methods for pattern matching.
"""

import fnmatch

for file_name in os.listdir('example_directory/'):
    if fnmatch.fnmatch(file_name, '*.txt'):
        print(file_name)

# 4.3 Advance Pattern Matching

"""
    If you want to find `.txt` files that meet certain criteria. For example,
    you could be only interested in finding `.txt` specific files that contain
    certain word for like 'data_01'.
"""

for filename in os.listdir('.'):
    if fnmatch.fnmatch('filename', 'data_*_backup.txt'):
        print(filename)

# 4.4 Filename Pattern Matching Using `glob`

"""
    The `.glob()` is module very similar with `fnmatch.fnmatch()`, but
    it treats files beginning with period (.) as special
"""

import glob

files_found =  glob.glob('**/*.py')

print('Files Found: ', files_found)

# Using `pathlib`

current_path = Path('./fundamental_concepts')

for filename in current_path.glob('*.p*'):
    print(filename)

# 5. Traversing Directories and Processing Files

"""
    We'll exploring walking a directories tree and
    processing files in tree. To do this, we'll use
    an integrated function `os.walk` from the `os`
    module.
"""

# Walking a directory tree and get data of the directories and files
for dirpath, dirnames, files in os.walk('./fundamental_concepts'):
    print(f'Found directory: {dirpath}')

    for file_name in files:
        print(file_name)

# 6. Making Temporary Files and Directories

"""
    Python provides a handy module for creating temporary files
    and directories called `tempfile`. It can be used to open and
    store data temporarily in a file or directory while your program
    is running. Also, `tempfile` handles the deletion these files or
    directories used when your program is done.
"""

# 6.1 Creating a temporary file
from tempfile import TemporaryFile

fp = TemporaryFile('w+t')
fp.write('Hello universe!')

fp.seek(0)

data = fp.read()
print(data)

fp.close()

# It's also can be used in conjunction with th `with` statement
with TemporaryFile('w+t') as fp:
    fp.write('Hello universe')
    fp.seek(0)
    print(f"Content of temporary file: {fp.read()}")

# 6.2 Creating temporary directories

import tempfile

with tempfile.TemporaryDirectory() as tmpdir:
    print('Created temporary directory ', tmpdir)
    os.path.exists(tmpdir)

# 7. Deleting Files and Directories

"""
    The `os`, `shutil`, and `pathlib` module provides an way
    handle exclusion of single files, directories and entire directory trees
"""

# 7.1 Deleting Files in Python

"""
    To delete a single file, use `pathlib.Path.inlink()`, `os.remove()` or
    `os.inlink()`
"""

data_file = 'C:\\Users\\AnyUser\\Desktop\\Test\\data.txt'

try:
    os.remove(data_file)
except OSError as e:
    print(f"Error: {data_file} : {e.strerror}")

    pass

# Using `os.unlink`
data_file = 'C:\\Users\\AnyUser\\Desktop\\Test\\data.txt'

try:
    os.unlink(data_file)
except OSError as e:
    print(f"Error: {data_file} : {e.strerror}")

    pass

# Using `pathlib.Path.unlink()`
data_file = Path('C:\\Users\\AnyUser\\Desktop\\Test\\data.txt')

try:
    data_file.unlink()
except IsADirectoryError as e:
    print(f"Error: {data_file} : {e.strerror}")

# 7.2 Deleting Directories

"""
    The `os.rmdir`, `pathlib.rmdir` and `shutil.rmtree` can be used
    for deleting of directories.
"""

# Deleting Single Directory or Folder

"""
    To delete a single directory or folder, can be used `os.rmdir()` or
    `pathlib.rmdir()`, but these both methods only work if the directory or
    folder is empty. If not, it returns an `osError` error is raised.
"""

trash_dir = 'my_documents/bad_dir'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f"Error: {trash_dir} : {e.strerror}")

# Other Alternative
trash_dir = Path('my_documents/bad_dir')

try:
    trash_dir.rmdir()
except OSError as e:
    print(f"Error: {trash_dir} : {e.strerror}")

# 7.3 Deleting Entire Directory Trees

"""
    To delete non-empty directories and entire
    directory trees, Python offers `shutil.rmtree()`
"""

import shutil

trash_dir = 'my_documents/bad_dir'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f"Error: {trash_dir} : {e.strerror}")

# To delete empty folders recursively

for dirpath, dirname, files in os.walk('.', topdown=False):
    try:
        os.rmdir(dirpath)
    except OSError as ex:
        pass

# 8 Copying, Moving, and Renaming Files and Directories

"""
    Python ships with the `shutil` module. It's is short
    for shell utilities. It provides a number of hight-level
    operations on files to support copying, archiving, and
    removal of files and directories. In this section, you'll
    learn how to move and copy files and directories.
"""

# 8.1 Copying Files in Python

current_path_file = os.path.dirname(os.path.realpath(__file__)) + '/files_handling.py'

destination_dir = os.path.join(os.path.dirname(__file__), '..')

shutil.copy(current_path_file, destination_dir)

"""
    If you want preserve metadata of files when copying, it's necessary use `shutil.copy2`
"""

# 8.2 Copying Directories

"""
    The `shutil.copytree` can be used to copy an entire directory and
    everything container in it.
"""

# Example

shutil.copytree('fundamental_concepts', 'fundamental_concepts_backup')

# 8.3 Moving Files and Directories

"""
    To move a file or directory to another location. use `shutil.move(src, dst)`
"""

shutil.move('dir_moved/', 'dir_destination/')

# 8.4 Renaming Files and Directories

"""
    Python includes `os.rename(src, dst)` for renaming files and directories.
"""

# Example
os.rename('first.zip', 'fist_01.zop')

# Another way
data_file = Path('data_01.txt')

data_file.rename('data.txt')

# 9. Archiving

"""
    With Python we'll can write programs that will create,
    read and extract data from archives.
"""

# 9.1 Reading ZIP Files

"""
    We can use the `zipfile` module that will
    brings easy functions to open and extract
    ZIP files
"""

import zipfile

with zipfile.ZipFile('data.zip', 'r') as zip_obj:
    read_data = zip_obj.read()

# Get a list of files in the archive
with zipfile.ZipFile('data.zip', 'r') as zip_obj:
    read_data = zip_obj.namelist()

# Using `.getinfo()` to retrieve information about the files in the archive
with zipfile.ZipFile('data.zip', 'r') as zip_obj:
    file_info = zip_obj.getinfo('sub_dir/any.py')
    file_info.file_size

# 9.2 Extracting ZIP Archives

"""
    To extract files, it's necessary use `zipfile.extract()`
    and `zipfile.extractall()` methods.
"""

# Extracting single file in current directory
data_zip = zipfile.ZipFile('data.zip', 'r')

data_zip.extract('file1.py')

# Extracting all files into a different directory
data_zip.extractall(path='extract_dir/')

data_zip.close()

# 9.3 Extracting Data from Password Protected Archives

"""
    The `zipfile` supports extracting password protected ZIPs.
    To do this, it's only necessary pass in the password to
    the `.extract()` or `.extractall` method as an argument
"""

with zipfile.ZipFile("secret.zip", "r") as pwd_zip:
    pwd_zip.extractall(path='extract_dir', pwd='password123')

# 9.4 Creating New ZIP Archives

files_list = ['file1.py', 'sub_dir/', 'file2.py', 'sub_dir2/']

with zipfile.ZipFile("new.zip", "w") as new_zip:
    for name in files_list:
        new_zip.write(name)

# 9.5 Opening TAR Archives

"""
    The TAR files are uncompressed file archives like ZIP.
    To compress them is necessary `gzip`, `bzip2` and `Izma`
    compression methods.
"""

# Reading archive
import tarfile
import time

with tarfile.open('example.tar', 'r') as tar_file:
    print(tar_file.getnames)

# Getting Metadata of each entry in the archive
for entry in tar_file.getmembers():
    print(entry.name)
    print('  Modified:', time.ctime(entry.mtime))
    print('  Size    :', entry.size, 'bytes')
    print()

# 9.6 Extracting Files from a TAR Archive

"""
    To extract files from TAR archives, can use
    these methods: `.extract`, `.extractfiles`, `.extractall`
"""

tarfile.extract("README.md")

# To unpack or extract everything from archive, can be use `.extractall`
tarfile.extractall(path="extracted/")

# To extract file for reading or writing
f = tar_file.extractfile('app.py')

f.read()

tar_file.close()

# 9.7 Creating New TAR Archives

import tarfile

file_list = ['app.py', 'config.py', 'tests.py']

with tarfile.open('packages.tar', mode='w') as tar:
    for file in file_list:
        tar.add(file)

# To add new file to an existing archive
with tarfile.open("package.tar", mode='r') as tar:
    for member in tar.getmembers():
        print(member.name)

# 9.8 Working With Compressed Archives

files = ['app.py', 'config.py', 'tests.py']

with tarfile.open('packages.tar.gz', mode='w:gz') as tar:
  tar.add('app.py')
  tar.add('config.py')
  tar.add('tests.py')

with tarfile.open('packages.tar.gz', mode='r:gz') as t:
  for member in t.getmembers():
    print(member.name)

# 10. An Easier Way of Creating Archives

"""
    The `shutil` module is also used to
    create, read and extract ZIP and TAR
    archives.
"""

# 10.1 Working with archives using `shutil.make_archive()`

shutil.make_archive('data/backup', 'tar', 'data/')

# To extract
shutil.unpack_archive('backup.tar', 'extract_dir/')

# 11. Reading Multiple Files

"""
    Python supports reading data from multiple
    input streams or from a list of files through
    `fileinput` module.
"""

import fileinput

def process(line):
    print(f"Processing line: {line.strip()}")

for line in fileinput.input():
    process(line)

# 11.1 Using `fileinput` to Loop Over Multiple Files

import sys

files = fileinput.input()
for line in files:
    if fileinput.isfirstline():
        print(f'\n --- Reading {fileinput.filename()} ---')
    print('-> ' + line, end='')
print()
