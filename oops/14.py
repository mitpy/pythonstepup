#inheritance

class B:
    n2=30

class A(B):
    n1=10
    def sum(self):
        print(self.n1+self.n2)

obj=A()
obj.sum() #30

#A ---> child , sub, derived
#B ---> parent, super, base