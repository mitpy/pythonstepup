#interface
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def speed100(self):
        pass
    @abstractmethod
    def cc1000(self):
        pass

#abstract class 

class C1(Vehicle):
    def speed100(self):
        print('speed implemented')

#abstract class

class C2(C1):
    def cc1000(self):
        print('cc impleted')

#concreate class

class Bus(C2):
    pass

obj=Bus()
obj.cc1000()
obj.speed100()
