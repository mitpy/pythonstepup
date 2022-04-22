#variable length argument

def f(n1,*nos):
    print(n1)
    print(nos)

f(10,20)
f(1,2,3,4)
f(100)
