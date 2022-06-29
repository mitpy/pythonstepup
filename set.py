#create set 
'''
s1={10,20,30,40}
print(type(s1))
s2=range(1,6)
s3=set(s2)
print(type(s3))

s4={}
print(type(s4)) #dict

'''
'''
s1={1,2,3,4}
print(s1)
print(len(s1))
s1.add(5)
s1.add(5)
print(s1)
s1.remove(3)
print(s1)
s1.clear()
print(s1)
'''
'''
nos={2,5,8,3,1,100}

print(5 in nos)
print(100 in nos)
print(88 in nos)
print(5 not in nos)
print(100 not in nos)
print(88 not in nos)

print({v*v for v in nos})

l1=[1,2,3,1,2,3,1,2,3]
s1=set(l1)
print(list(s1))

'''

s1={1,2,3,4}
s2=frozenset(s1)
print(s1)
print(s2)
s1.remove(2)
print(s1)
s2.remove(2)


