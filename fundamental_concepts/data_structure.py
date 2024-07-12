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

# 2. Tuple

"""
  - Similar to list, but they are immutable.
  - Used when a collection of items cannot be changed
"""

my_tuple = (1, 2, 3, 'four')

# It can also be defined like this
my_tuple = 1, 2, 3, 'four'

# Packing and unpacking
tuple_example = 1, 2, 'tuple'

x, y, z = tuple_example


