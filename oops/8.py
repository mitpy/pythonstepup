#local varibales
'''
def f1():
    name='Sachin'  

print(name) // name is local , we can access inside the f1 only

'''

class A:
    def info(self):
        runs=20000
        self.name='Sachin'

    def getRuns(self):
        return runs #will throw an error

    def getName(self):
        return self.name

o=A()
o.info()
o.getRuns()
o.getName()
        


    
