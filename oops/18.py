class C:
    def m1(self):
        print('m1 from C')
class B:
    def m1(self):
        print('m1 from B')

class A(C,B):
    def m2(self):
        print('m1 from A')

obj=A()
obj.m1()
print(A.mro())
