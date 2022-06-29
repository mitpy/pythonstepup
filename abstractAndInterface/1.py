#concrete class

class Bus:
    fw=2
    bw=4
    def totalWheels(self):
        return self.fw+self.bw
    def getColor(self):
        return 'red'

obj=Bus()
print(obj.totalWheels())
print(obj.getColor())