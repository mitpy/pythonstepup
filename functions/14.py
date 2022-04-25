#lambda functions

def f(data):
    print(type(data))
    print(data())

f(lambda : print('lambda function'))

