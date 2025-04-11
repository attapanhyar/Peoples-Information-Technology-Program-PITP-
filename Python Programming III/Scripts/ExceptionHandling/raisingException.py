
def greet(name : str)-> str:
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"

def callfunction(func, name):
    return func(name)

print(callfunction(greet, "John")) # This will work fine