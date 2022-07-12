#read some lines

fileObj=open('players.txt','r')
data=fileObj.readlines()
print(type(data))
print(data)
for v in data[0:5]:
    print(v)