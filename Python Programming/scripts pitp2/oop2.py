##
##class Student:
##    x = int()
##    def __init__(self,name, caste):
##        self.name = name
##        self.caste = caste
##        
##    def __repr__(self):
##        return f'{self.name} of caste {self.caste}'
##
##std1 = Student('Ahmed', 'Sanjrani') # object
##std2 = Student('Ali', 'Sanwal')
##print()


class Balance:
    def __init__(self, bal):
        self.bal = bal
    def __lt__(self, sec):
        return self.bal < sec.bal

sal1 = Balance(50000)
sal2 = Balance(7000)

print(sal1<sal2)













