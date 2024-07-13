"""
    List and Generators

    Understanding list manipulation is necessary for code optimization.
"""

# 1. Simple Examples

names = ['Vinicius', 'Carlos', 'Eduarda', 'Lara', 'José']

names_uppercase = [name.upper() for name in names]

expr_math = [x**2 for x in range(0, 10)]

# 2. List Comprehension

"""
    The following examples comprise Python's powerful list comprehension feature.

    [expr for item in list cond]
"""

names_contains_a = [name for name in names if 'a' in name]

only_even_numbers = [x for x in range(0, 50) if x % 2 == 0]

# 3. Comparison: List and For

"""
    List comprehension has many advantages over a loop like for, such as:

    - Syntax
    - Legibility
    - Performance
    - Memory usage
"""

# 3.1 Syntax and Legibility

# In For
square_for = []

for x in range(0, 10):
    square_for.append(x * x)

print(square_for)

# In List
square_list = [x * x for x in range(0, 10)]

print(square_list)

"""
    Understanding the both ways of generating a list of squared numbers,
    we can see that we save time by using the list, but for complex expressions
    we should use the for loop.
"""

# 3.2 Performance

import timeit

def loop_for():
    squares = []

    for x in range(0, 10):
        squares.append(x * x)

def list_comprehension():
    square = [x * x for x in range(0, 10)]

loop_for_time = timeit.timeit(loop_for, number=10)
list_comprehension_time = timeit.timeit(list_comprehension, number=10)

# Here, a comparison of time between both expressions
print(loop_for_time, list_comprehension_time)

"""
    We can see, that a list comprehensions gives more saved time
"""

# 3.3 Memory usage

"""
    As their sizes are equivalent in these two approaches.
    We can only see the difference between understanding
    generators that generate items on demand.
"""
