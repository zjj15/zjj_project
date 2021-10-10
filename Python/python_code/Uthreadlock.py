
#线程
#coding=UTF-8
#线程模块 threading

#自定义线程：继承threading.Thread来定义线程类，其本质是重构Thread类中的run方法

import threading

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.thradID=threadID
        self.name=name
        self.counter=counter

    #for循环之内加锁
    def run(self):
        print("thread start!")
        #获取锁
        for i in range(self.counter):
            try:
                Lock.acquire()
                print("%s: %d" %(self.name,i))
            finally:
                Lock.release()
        print("thread end!")


    #for循环之外加锁
    # def run(self):
    #     print("thread start!")
    #     #获取锁
    #     try:
    #         Lock.acquire()
    #         for i in range(self.counter):
    #             print("%s: %d" %(self.name,i))
    #     finally:
    #         Lock.release()
    #     print("thread end!")


    

if __name__=='__main__' :
    Lock=threading.Lock()
    print("开始主线程")
    #创建线程
    t1=myThread('1','th1',6)
    t2=myThread('2','th2',6)
    #启动线程
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("退出主线程")








