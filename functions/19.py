#closure

def f1():
    name='Sachin'
    def f2():
        loc='Mumbai'
        print('This is ' + name + ' I am from '+ loc)
    return f2


f3=f1()
f3()