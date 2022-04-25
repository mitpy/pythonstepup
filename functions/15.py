# pass data through callback functions

def f1(data):
    name='Sachin'
    data(name)


def myFun(name):
    print('myFun called', name)

f1(myFun)


