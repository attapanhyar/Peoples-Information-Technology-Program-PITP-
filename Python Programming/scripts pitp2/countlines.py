file = open('example.txt','r')
count = 0
for read in file:
    count +=1
    #print(read)
print(f'The number of lines are {count}')
file.close()
