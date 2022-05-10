# multiple Inheritance

class B:
    n2=20
class C:
    n3=30

class A(B,C):
    n1=10
    def sum(self):
        print(self.n1+self.n2+self.n3)

obj=A()
obj.sum()