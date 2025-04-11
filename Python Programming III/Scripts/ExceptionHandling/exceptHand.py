
num1 = int(input('Enter Num1: '))
num2 = int(input('Enter Num2: '))
try:
    result = num1/num2
except:
    print('Can divide number with zero')
else:
    print(f'Result: {result}')
finally:
    print('This shall alway be executed')
