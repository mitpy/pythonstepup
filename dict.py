#creation
'''
player={}

print(type(player))

student={
    "name":"s1",
    "rno":10,
    "marks":400
}
print(student)
print(type(student))
'''
#insert data in dict
from numpy import outer


player={}
player['name']='Sachin'
player['runs']=20000
player['loc']='Mumbai'
print(player)

#access the data from dict
print(player['loc'])

for k,v in player.items():
    print(k,v)

#update the data in dict
print('Before Update ', player)
player['runs']=20192
player['hun']=100
print('After Update', player)

#Delete data from dict 

print(len(player))
print('Before Delete ', player)
del player['runs']
print('After Delete ', player)
#del player
#player.clear()
#print('After Clear ', player)

#keys from dict

print(player.keys())
print(player.values())
print(player.items())

#Comprehnsive

nos=range(10,21)
output={v:v*v for v in nos}
print(output)