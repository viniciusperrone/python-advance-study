"""
    We will introduce the concept of object-oriented
    programming (OOP). We will record the basic concepts,
    also how to define custom types using classes, and
    how to instantiate those classes.
"""

# 1. Intro Classes

# This is empty class


class Person:
    pass

person = Person()

# Improving class

"""
    Here, our class called Person will have some attributes and methods
"""
class Person:
    name: str
    age: int = 0

    # It's constructor
    def __init__(self, name: str, age: int = None) -> None:
        self.name = name
        self.age = age

    # An method called increment age
    def increment_age(self, new_age: int = None) -> None:
        if new_age is not None:
            self.age = new_age
        else:
            self.age = self.age + 1

person = Person('Vinicius', 22)

person.increment_age()

print(person.age)

"""
    To mack an class's instance callable, you need
    to implement a `.__call__()` special method.
"""

# 2. Using Python Class Constructors

# 2.1 Understanding Python's Instantiation Process

"""
    When triggering Python's instantiation process whenever
    call a Python class to create a new instance. This process
    runs through two separate steps.

    - Create a new instance of the target class
    - Initialize the new instance with an appropriate initial state

    The first step, it's triggering a special method called `.__new__()`, which
    is responsible for creating and returning a new empty object. The other one,
    it's called `.__init__()`, takes the resulting object, along with the class
    constructor's arguments.
"""

# Demonstration
class Point:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")

        return super().__new__(cls)

    def __init__(self, x, y) -> None:
        print("2. Initialize the new instance of Point.")

        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

