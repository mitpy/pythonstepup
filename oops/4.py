#constructor

class A:
    n1=10
    n2=20
    def __init__(self):
        print('init called')
    def f1(self):
        print('f1 called')


obj=A()  
#obj.__init__(obj)
obj.f1()