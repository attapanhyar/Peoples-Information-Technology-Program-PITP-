

##class A:
##    def message(self):
##        print('Print from A class')
##
##
##class B(A):
##    pass
##
##
##obj = B()
##obj.message()
##










class Animal:
    def __init__(self, name, sound):
        self.name =name
        self.sound = sound

    def __repr__(self):
        return f'{self.name} makes {self.sound} sound'
class Cat(Animal):
    def __init__(self, name, sound):
        super.__init__(name,sound)
cat1 = Cat('TOM', 'MEOW')
print(cat1)















