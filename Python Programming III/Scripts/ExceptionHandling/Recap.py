
# def Introduction(name): # parameters / agruments
#     print(f'Welcome {name}')
# name = input('Enter your name')
# Introduction(name) # function call

# def addition(*x):
#     return sum(x)
# print(f'The sum of two numbers is {addition(3,5,4,5,6,5,6,7)}')

def details(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} -- {value}')


details(fname = "James", caste = "Achrani", location = "Pakistan")




