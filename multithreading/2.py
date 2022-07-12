#create thread

import threading

class MyThread1(threading.Thread):
    def run(self):
        for v in range(1,6):
            print('T1',v)

class MyThread2(threading.Thread):
    def run(self):
        for v in range(1,6):
            print('T2',v)

class MyThread3(threading.Thread):
    def run(self):
        for v in range(1,6):
            print('T3',v)

t1=MyThread1()
t2=MyThread2()
t3=MyThread3()

t1.start()
t2.start()
t3.start()
