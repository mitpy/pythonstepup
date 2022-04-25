def f1(n):
    return n

def myFun():
    print('myFun called')

f2=f1(myFun)
f2()
print(type(f2))
