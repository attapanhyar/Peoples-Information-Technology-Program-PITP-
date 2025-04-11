x = [1, 2, 3, 4, 5]
# This will raise a NameError because x is not defined
try:
    print(f'{x[10]}')
except NameError:
    print('Name Error has Occured')
except Exception as e:
    print(f'An error has occurred: {e}')
