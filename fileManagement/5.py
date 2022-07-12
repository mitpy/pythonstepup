
#append the content 

fileObj=open('players.txt','a+')

for i in range(1,11):
    fileObj.write('Line no ' +str(i) +'\n')

fileObj.close()
print('Successfully inserted')