#filter function

marks=[400,500,480,700,600]

'''
def f(v):
    return v>520
result=filter(f,marks)
'''

result=filter(lambda v:v>520,marks)
print(list(result))


#callback : f

#hoc : filter