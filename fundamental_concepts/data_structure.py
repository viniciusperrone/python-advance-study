"""
Data structure

Here, we'll understand the structure data in Python.
Basic concepts about data types such as: lists, tuples, 
dictionaries and others that we already know.
"""

# 1. List

"""
  - An ordered and changeable collection of items.
  - Items can be of any type and accessed by indexes.
  - It supports operations such as adding, removing and slicing elements. 
"""

my_list = ['a', 'b', 3, 'c', 'd']

# 1.2. Main Operations

# Add new item at the end of list
my_list[len(my_list):] = ['a']

# Simplified
my_list.append('a')

# Extend new list
my_list[len(my_list):] = ['a', 'b']

# Simplified
my_list.extend(['a', 'b'])

# Clean list
my_list.clear()

# Equivalent
del my_list[:]



