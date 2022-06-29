#create tuple variable 
'''
players=('Sachin','Dhoni','Kohli')

print(type(players))

nos=range(1,6)
data=tuple(nos)
print(type(data))

names=('Sachin')
print(type(names))

'''

#Access the data from tuple 
'''
players=('Sachin','Dhoni','Kohli')

print(players[2])
print(players[-1])

nos=range(1,11)
nos=tuple(nos)
print(nos[3:6])
print(nos[3:])
print(nos[2])
print(nos[:])
print(nos[::])
print(nos[::2])

for v in nos:
    print(v)
'''

#nature (mutable/ immutable)
'''
players=('Sachin','Dhoni','Kohli')

players[0]='Lara' # 'tuple' object does not support item assignment

'''
#mathematical operations
'''

t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)

print(t3*3)
print(len(t3))

'''

'''
t1=(10,22,5,1,2,1,2,1,1,1,5)
print(t1.count(1))
print(t1.index(22))
print(t1.index(1))
t2=sorted(t1)
print(t1)
print(tuple(t2))
print(min(t1))
print(max(t1))

'''

nos=range(1,6)
nos=tuple(nos)
print(nos)
output=(v*v for v in nos)
print(tuple(output))
