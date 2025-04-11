# fruits = ['Banana','Apple','Orange'] # list
# fruits[1]='Grapes'
# fruits.append('Gajar')
# for i, fruit in enumerate(fruits):
#     print(f'{i+1}-{fruit}')
# fruits = []
# while True:
#     myin = input('Enter your Favourite Fruit [Press q to exit]')
#     if myin =='q':
#         print('All favourite fruits are Added')
#         break
#     fruits.append(myin)
# for fruit in fruits:
#     print(fruit)


fruits = ['orange','apple','banana']
fruits.insert(1,'Grapes')
while True:
    gfruit = input('Gues my favorite fruit')
    if gfruit.lower() in fruits:
        print('You guessed it correctly')
        break
    else:
        print('Try again.')












