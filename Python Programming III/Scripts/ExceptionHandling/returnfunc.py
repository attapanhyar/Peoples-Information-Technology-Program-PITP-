def addition(*args):
    temp = 1
    for i in args:
        temp *= i
    return temp
print(f'The Product of two numbers is : {addition(3,4,5)}')
print(f'The Product of two numbers is : {addition(3,4,5,4)}')