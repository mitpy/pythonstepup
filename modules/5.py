'''
import Student as s

print(s.name)
print(s.getStdRno())
print(s.MyStd().totalMarks())
'''
'''
from Student import  name ,getStdRno,MyStd
print(name)
print(getStdRno())
print(MyStd().totalMarks())
'''
'''
from Student import *
print(name)
print(getStdRno())
print(MyStd().totalMarks())
'''
'''
from Student import  getStdRno as gs
print(gs())
'''
import Student
print(dir(Student))