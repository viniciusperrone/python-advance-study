from memory_profiler import profile

"""
    The code above shows the different memory use between two approach.
"""

@profile
def list_comprehension():
    squares = [x * x for x in range(0, 10)]
    return squares

@profile
def generator_comprehension():
    squares_gen = (x * x for x in range(0, 10))
    return list(squares_gen)

if __name__ == '__main__':
    generator_comprehension()
    list_comprehension()
