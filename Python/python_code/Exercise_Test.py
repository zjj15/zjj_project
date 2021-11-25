
import time

time1=int(time.time())
while int(time.time())-time1 <5:
    print(int(time.time()))
    print(int(time1))
    print(int(time.time()-time1))
