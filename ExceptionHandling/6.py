print('Start')
print(1)
print(2)
name=10

try:
    print(10/5)
    len(name)
except ZeroDivisionError as e:
    print(e)
    print('excetpion raised')
except TypeError as t:
    print(t)
    print('excetpion raised')
    name=''
print(3)
print(4)
len(name)
print('end')