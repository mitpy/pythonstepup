# instance & static varibales

class Student:
    #static variable
    school='PUBLIC School'
    def __init__(self,name,rno):
        #instace variables
        self.name=name
        self.rno=rno
  

std1=Student('s1',1)
print(std1.name)
print(std1.rno)
print(std1.school)

std2=Student('s2',2)
print(std2.name)
print(std2.rno)
print(std2.school)

std3=Student('s3',3)
print(std3.name)
print(std3.rno)
print(std3.school)
