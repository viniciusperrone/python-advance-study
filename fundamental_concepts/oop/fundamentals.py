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

# 2.2 Object Initialization With `.__init__()`

"""
    The `.__init__` method is probably the most common
    special method that ever override in your custom class.
    But, has some relevant information, firstly, as already
    mentioned it's the result of the object recently created
    by the `.__new__` method, so it's not class's constructor.
"""

# Simple Example
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

"""
    Additionally, keep in mind that `.__init__()` must
    not explicitly return anything different from None.
"""

# Improving Rectangle class
class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and width > 0):
            raise ValueError(f"positive width expect, got {width}")

        if not (isinstance(width, (int, float)) and width > 0):
            raise ValueError(f"positive height expected, got {height}")

        self.width = width
        self.height = height

# Using inheritance
class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

class Employee(Person):
    def __init__(self, name, birth_date, position):
        super().__init__(name, birth_date)
        self.position = position

john = Employee("John Doe", "2002-20-01", "Python Developer")

print(john)

"""
    The base implementation of `.__init__()` comes from
    built-in object class. This implementation is automatically
    called when you don't provide an explicit `.__init__()` method
    in tour classes.
"""

# 2.3 Object Creation With `.__new__()`

"""
    The `.__new__` special method is not necessary to provide it in
    your own implementation.
"""

# Proving Custom Object Creators
class SomeClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

        return instance

print(SomeClass(42))

"""
    Cases that should customize the `.__new__()` special
    method. These cases reference the subclass an immutable
    built-in data type.

"""

# How customize `.__new__` method
class Distance(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)

        instance.unit = unit

        return instance

in_miles = Distance(42.0, 'Miles')

print(in_miles)

"""
    This custom `.__new__` runs the three steps. First, the method
    creates a new instance of the current class, `cls`, by calling
    `super().__new__()`. This time, the call rolls back to `float.__new__()`,
    which create a new instance and initializes it using `value` as an argument.
    The third step, it's create new instance by adding a `.unit` attribute
    to it. Finally, the new instance gets returned.
"""

# 3. Providing Multiple Constructors in Your Python Classes

# 4. Supercharge Your Classes With Python `super()`

# 5. Inheritance and Composition

# 6. Managing Attributes With Python's propery

# 7. Python Descriptors

# 8. Pythonic OOP String Conversion: __repr__() cs __str__()

# 9. OOP Method Types in Python

# 10. Operator in Function Overloading in Custom Python Classes

# 11. Using Data Classes in Python

# 12. Metaclasses in Python
