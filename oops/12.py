#class methods 

class Player:
    name='Sachin'
    def __init__(self):
        self.runs=2000

    @classmethod
    def getName(Cls):
        print(Cls.name)
    @classmethod
    def getRuns(Cls):
        obj=Cls()
        print(obj.runs)

obj=Player()
obj.getName() #obj.getName(Player)
Player.getRuns()