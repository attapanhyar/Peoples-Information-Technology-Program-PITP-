lst = [1,2]
try:
    print(x)
    print(lst[10])
except NameError:
    print('x is not defined')
except Exception as ae:
    print(f'Error type is  : {ae}')
else:
    print('If try runs succesfully')
finally:
    print('Shall always be executed')
