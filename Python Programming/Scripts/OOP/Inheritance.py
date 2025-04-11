class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} says Woof')

class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} says Meow')

dog = Dog('Buddy')
cat = Cat('Kitty')
dog.make_sound()  # Buddy says Woof
cat.make_sound()  # Kitty says Meow
