def square(x):
    return x*x
number = [1,2,3,4,5,6,7]
sqaureIterator = map(square, number)
print (list(sqaureIterator))
