def f(a,b):
    a()
    b('Dhoni')
    def f1():
        print('Kohli')
    return f1

def f2():
    print('Sachin')

f3=f(f2,lambda name: print(name))
f3()