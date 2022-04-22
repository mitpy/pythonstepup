#variable length vs keyword variable length

def f1(*nos):
    print(nos)


f1(1,2,3)

f1('sachin','Dhoni','Uv')

def f2(**data):
    print(data)

f2(name='Sachin',runs=20000)