#variable length argument

def sum(*nos):
    result=0
    for val in nos:
        result=result+val
    print(result)



sum(10,20)
sum(1,2,3)
sum()
