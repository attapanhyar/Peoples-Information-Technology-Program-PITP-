
# Encapsulation: Data Hiding
class Learning_Encap:
    def __init__(self, name):
        self.__name = name
    def display_name(self):
        print(f'The name of obj1 is {self.__name}')


obj1 = Learning_Encap('Ali')
obj1.display_name()