# Higher order/ pure function /Decorator function 
'''
def f(getFirstNo):
    
    def sum(n2):
        print(getFirstNo()+n2)

    return sum

def f1():
    return 10

result=f(f1)

result(20)

'''

def f(getFirstNo):
    
    def sum(n2):
        print(getFirstNo()+n2)

    return sum

@f
def f1():
    return 10

f1(20)



