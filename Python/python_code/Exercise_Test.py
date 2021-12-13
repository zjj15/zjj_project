#test.py

import os

count=0
for dirpath,dirname,filename in os.walk(os.getcwd()) :
    for file in filename :
        if file.find('Exercise') !=-1:
            count+=1
            print('第%d个符合条件的文件' %count)
            print('文件名为：', file)
            print('绝对路径为：' , os.getcwd())
        else:
            pass
