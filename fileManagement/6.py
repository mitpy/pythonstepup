#read the content 

fileObj=open('players.txt','r')
content=fileObj.read()
print(type(content))#str
print(content)