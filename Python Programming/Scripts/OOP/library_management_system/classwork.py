
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def Display_info(self):
        print(f"the name of student is {self.name}\nTHe associated ID is {self.id}")
    def __repr__(self):
        return f"OBJ Name:  {self.name} OBJ ID {self.id}"
std1 = Student("Ali","24IT56")
print(std1)
