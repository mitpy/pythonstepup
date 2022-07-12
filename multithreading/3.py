#create a thread

import threading

def f1():
    for v in range(1,6):
        print('f1',v)

def f2():
    for v in range(1,6):
        print('f2',v)

class T:
    def f3(self):
        for v in range(1,6):
            print('f3',v)
o=T()
t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)
t3=threading.Thread(target=o.f3)

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
