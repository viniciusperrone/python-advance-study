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
