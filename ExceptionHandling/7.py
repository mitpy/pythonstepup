#finally 

print('start')
print(1)
try:
    print(10/0)
except:
    print('Exception raised')
finally:
    print('finally executed')

print('end')