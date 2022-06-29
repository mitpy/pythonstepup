#abstract class 
from abc import ABC,abstractmethod

class Bus(ABC):
    fw=2
    bw=4
    def totalWheels(self):
        return self.fw+self.bw
    @abstractmethod
    def getColor(self):
        pass

obj=Bus()
print(obj.totalWheels())
print(obj.getColor())