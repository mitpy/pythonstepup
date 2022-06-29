#name='Sachin'
#name="Sachin"

name='''Sahcin'''
lastName='Tendulkar'

empName='E1'
salary=20000
age=28
print(type(str(salary)))
print('Emploayee name  is {} , his salary is {} and his age is {}'.format(empName,salary,age))
print('Emploayee name  is {0} , his salary is {1} and his age is {2}'.format(empName,salary,age))
print('Emploayee name  is {x} , his salary is {y} and his age is {z}'.format(y=salary,z=age,x=empName))



'''
print(list(map(lambda x:x,name)))
s1='Python is a programming language'
print(s1)
print(type(s1))
result=s1.split()
print(result)
print(type(result))

'''

'''
s1='Java is a programming language'
s2=s1.replace('Java','Python')
print(id(s1))
print(id(s2))
print(s1)
print(s2)
'''

'''

str='Python is a programming language and Python is easy to learn'

print(str.count('Python'))
print(str.count('programming'))
print(str.count('Sachin'))

'''

'''
text='Hi this is Sachin , I am from Mumbai'

print(text.find('Sachin'))
print(text.find('Python'))
print(text.find('Hi'))
print(text.find('Hellow'))
print(text.index('Hi'))
print(text.index('Sachin'))
print(text.index('Hellow'))
'''

'''
courseName='Python  '
print(len(courseName))
print(len(courseName.strip()))

'''


#print(name==lastName) False
#print('h' not in name) False
#print('hci' in name) True
#print('hcn' in name) False
#print(name+lastName)
#print(name*5)
#print(len(name))

#name[0]='D'  Not possible , because string by default has immutable nature

#print(type(name))    type of name is class 'str'

#name.startswith('a') # name is an object of str class, using that object we call one of the method startswith in str class

'''
Retrieve the data from string using index 

print(name[2])
print(name[0])
print(name[-4])
print(name[-1])

'''
'''
Access the data from string using slice
print(name[0:2])
print(name[2:3])
print(name[3])
print(name[0:6:2])
'''





