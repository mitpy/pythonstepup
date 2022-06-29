#Overloading

class Arth:
    def sum(self,n1,n2):
        print(n1+n2)
    def sum(self,n1,n2,n3):
        print(n1+n2+n3)

obj=Arth()
#obj.sum(10,20) Arth.sum() missing 1 required positional argument: 'n3'
obj.sum(10,20,30)