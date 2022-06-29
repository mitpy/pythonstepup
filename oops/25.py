#Overriding
class Parent:
    def property(self):
        print('50cr')

class Child(Parent):
    def property(self):
        print('500cr')


obj=Child()
obj.property()