# pass data through callback functions(anonymous)

def f1(data):
    name='Sachin'
    data(name)

f1(lambda name:print('myFunction', name))


