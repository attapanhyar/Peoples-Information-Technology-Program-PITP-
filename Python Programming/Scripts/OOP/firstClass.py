class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} says {self.sound}')

# Create an object
dog = Animal('Dog', 'Woof')
dog.make_sound()  # Output: Dog says Woof
