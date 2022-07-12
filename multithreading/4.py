import threading
import time

threadLock=threading.Lock()

class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        threadLock.acquire()
        self.transaction()
        threadLock.release()

    def transaction(self):
        for v in range(1,5):
            time.sleep(2)
            print(self.name,v)


t1=MyThread('t1')
t2=MyThread('t2')
t3=MyThread('t3')

t1.start()
t2.start()
t3.start()
