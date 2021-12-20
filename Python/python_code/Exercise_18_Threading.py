#threading 线程
import threading
import time
''' 
#1 

def run():
    for i in range(5):
        print('第%d个%s线程' %(i,threading.current_thread().name))

print('这是%s线程'%threading.current_thread().name)
th=threading.Thread(target=run,name='LoopThread')#子线程名在创建时指定
th.start()
th.join()
print('这是%s线程'%threading.current_thread().name)

'''
''' 
#2 
class myThread(threading.Thread):
    def __init__(self,threadID,name,delay,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.delay=delay
        self.counter=counter
 
 
    def run(self):
        print('开始线程' + self.name) 
        thlock.acquire()#加锁后只能等线程1执行完毕才能执行线程2
        while self.counter:
            self.counter-=1
            print('%d,%s' %(self.threadID,self.name))
            time.sleep(self.delay)
        thlock.release() #开启下一个线程  
        print('退出线程'+ self.name)
        
        

thlock=threading.Lock()
print('开始'+threading.current_thread().name)

th1=myThread(1,'threadid1',1,6)
th2=myThread(2,'threadid2',2,6)
th3=myThread(3,'threadid3',3,6)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()
print('退出'+threading.current_thread().name)

'''
