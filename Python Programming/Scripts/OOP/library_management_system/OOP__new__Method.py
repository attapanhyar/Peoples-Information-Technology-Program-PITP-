class Example:
    def __new__(cls):
        print("Creating Instance")
        return super(Example, cls).__new__(cls)
    
    def __init__(self):
        print("Initializing Instance")

ex = Example()
