class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, aged {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alie", 30)
print(str(p))  # Output: Ali, aged 30
print(repr(p)) # Output: Person('Ali', 30)