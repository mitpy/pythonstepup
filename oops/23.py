class Arth:
    def sum(sel1,n1=None,n2=None,n3=None):
        if n1 != None and n2 !=None and n3 !=None :
            print(n1+n2+n3)
        elif n1!=None and n2 !=None:
            print(n1+n2)
        elif n1 != None:
            print(n1)


obj=Arth()
obj.sum(10,20,30)
obj.sum(100,200)
obj.sum(1000)