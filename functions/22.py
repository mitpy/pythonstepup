#reducer method

from functools import reduce


stdMarks=[88,70,90,66,50]   
'''
def f(a,b):
    print(a,b)
    return a+b

totalMarks=reduce(f,stdMarks)
'''

totalMarks=reduce(lambda a,b:a+b,stdMarks)
print(totalMarks)

#callback: f 
#higher order : reduce