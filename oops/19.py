# constructor execution
class B:
    def __init__(self):
        print('B class constructor(parent/super/base)')
    n2=20

class A(B):
    n1=10
    def __init__(self):
        print('A class constructor(child/sub/derived)')
    def sum(self):
        print(self.n1+self.n2)

obj=A()
obj.sum()