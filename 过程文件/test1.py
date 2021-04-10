import threading
import time

bbb = 0

def aaa():
    for i in range(10):
        time.sleep(2)
        bbb = 2
        print(bbb)
        print('over')
        print(i)
        print('\n')

class myThread(threading.Thread):
    def run(self):
        print("starting"+self.name)
        aaa()
        print("exit")

thread1 = myThread()
thread1.start()
for j in range(10):
    bbb = 1
    time.sleep(3)
    print('main')
    print(j)
    print(bbb)
    print('\n')
