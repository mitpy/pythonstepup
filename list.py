import copy;

# creation
'''
players=['Sachin','Dhoni','Kohli']
primes=[2,3,5,7]

nos=range(1,6)
nos=list(nos)

print(type(nos))
print(type(primes))

#Access the data from List 

primes=[2,3,5,7]

print(primes[1])
print(primes[-1])
# print(primes[4])    list index out of range

print(primes[0:2])
print(primes[2])
print(primes[0:4:2])
print(primes[2:])
print(primes[:])

for v in primes:
    print(v)


#count

nos=[1,2,3,3,4,5,2,1,2]
print(nos.count(2))

#reverse, len

primes=[2,3,5,7]
print(len(primes))
print(primes)
primes.reverse()
print(primes)

#mutable nature
list=[1,2,3]
print(list[0])
list[0]=200
print(list)


#shallow copy
l1=['Sachin','Dhoni','Kohli']
print(l1)
#l2=l1
l2=copy.copy(l1) 
print(l2)
l2[0]='Dravid'
print('After replacing')
print(l1)
print(l2)



l1=[1,2,[3,4],5]
l2=copy.deepcopy(l1)
print('Before')
print(l1)
print(l2)
print('do changes')
l1[2][0]=100
print('After')
print(l1)
print(l2)



players=['Sachin','Dhoni','Kohli']
print(players)
players.append('uv')
print(players)
players.insert(2,'Dravid')
print(players)
players.pop()
print(players)
players.remove('Dhoni')
print(players)
players.sort()
print(players)



a=[1,2,3]
b=[4,5,6]
c=a+b 
d=a*2
print(c)
print(d)



nos=[1,2,3,10,100,20]

print(20 in nos)
print(20 not in nos)
print(22 in nos)
print(22 not in nos)



l1=range(1,6)
squares=[v*v for v in l1]
print(squares)

'''