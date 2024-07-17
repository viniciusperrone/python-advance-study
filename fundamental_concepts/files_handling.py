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

