# Multilevel Inheritance 
class C:
    n3=30
class B(C):
    n2=20
class A(B):
    n1=10
    def sum(self):
        print(self.n1+self.n2+self.n3)

obj=A()
obj.sum() #obj.sum(obj)