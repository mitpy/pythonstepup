print('Start')
print(1)
print(2)
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
    print('excetpion raised')
print(3)
print(4)
print('end')