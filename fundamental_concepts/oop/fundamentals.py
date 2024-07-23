"""
    We will introduce the concept of object-oriented
    programming (OOP). We will record the basic concepts,
    also how to define custom types using classes, and
    how to instantiate those classes.
"""

# Example
class Person:
    name: str
    age: int

    def __str__(self) -> str:
        return f"name: {self.name} \n age: {self.age}"

single_person = Person

print(type(single_person))

# Improving Class
class Person:
    name: str
    age: str

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

single_person = Person("Vinicius", 22)

print(type(single_person))
