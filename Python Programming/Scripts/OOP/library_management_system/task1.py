

class Student: 
    def __init__(self, name, id):
        self.name = name
        self.id = id

std1 =  Student("Zafar", "23CS30") # Instance or object of class student
std2 = Student("Ali","24TC01")

print(f'The name of student is {std1.name} and his/her ID is {std1.id}')
print(f'The name of student is {std2.name} and his/her ID is {std2.id}')

