#create a class and object 

class Bus:
    fw=2 
    bw=4
    clr="red"
    def getColor(self):
        print(self)
        return self.clr
    def totalWheels(self):
        print(self)
        print(self.fw+self.bw)


obj=Bus()
print(obj.bw)
print(obj.fw)
print(obj.getColor()) # obj.getColor(obj)
print(obj.totalWheels()) #obj.totalWheels(obj)




