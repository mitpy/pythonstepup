# return multiple values

def Player():
    name='Sachin'
    loc="Mumbai"
    return name,loc

result=Player()
print(result)

for  val in result:
    print(val)

