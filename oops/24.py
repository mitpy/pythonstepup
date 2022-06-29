#Overriding
class Parent:
    def property(self):
        print('50cr')

class Child(Parent):
    pass


obj=Child()
obj.property()