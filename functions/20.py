#map function



marks=[400,500,480,700,600]

'''
def f(v):
    print(v)
    return v+10

result=map(f,marks)
'''

result=map(lambda v:v+10,marks)

print(list(result))

#callback : f 
#higher order : map