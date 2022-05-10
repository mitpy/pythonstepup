# Single Inheritance 

class P:
    n2=20
    def sub(self):
        print('sub', self.n1-self.n2)


class C(P):
    n1=10
    def sum(self):
        print('sum ', self.n1+self.n2)

obj=C()
print(obj.n1)
print(obj.n2)
obj.sub() # obj.sub(obj)
obj.sum() # obj.sum(obj)



