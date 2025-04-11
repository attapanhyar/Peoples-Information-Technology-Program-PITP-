class Car:
    # Class attribute (shared across all instances)
    wheels = 4
    # Instance attributes (specific to each instance)
    def __init__(self, make, model, year):
        self.make = make  # instance attribute
        self.model = model  # instance attribute
        self.year = year  # instance attribute
    # Instance method
    def start_engine(self):
        print(f'The engine of {self.make} {self.model} ({self.year}) has started.')
    # Class method (working with class attributes)
    @classmethod
    def car_info(cls):
        print(f"Cars usually have {cls.wheels} wheels.")
car1 = Car('Toyota', 'Corolla', 2020)
car2 = Car('Honda', 'Civic', 2019)
# Accessing instance attributes and methods
car1.start_engine()  # Output: The engine of Toyota Corolla (2020) has started.
car2.start_engine()  # Output: The engine of Honda Civic (2019) has started.
# Accessing class method and class attribute
Car.car_info()  # Output: Cars usually have 4 wheels.
