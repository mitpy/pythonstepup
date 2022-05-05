# static methods 

class Player:
    name='Sachin'

    @staticmethod
    def getName():
        print('Sachin')
    @staticmethod
    def getLoc():
        print('Mumbia')

obj=Player()
obj.getName()#obj.getName()
Player.getLoc()
