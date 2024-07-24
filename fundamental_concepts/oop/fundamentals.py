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
