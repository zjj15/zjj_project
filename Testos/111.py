#修改文件夹里面所有文件以及最内层.py脚本的名字
#coding=utf-8
import os


path=r'C:\Users\autost\Desktop\ZjjGit\zjj_project\Testos'



#输出所有文件,包含文件夹
ListAll=os.listdir(path)

for file in ListAll:
    cur_path=os.path.join(path,file)
    with open(cur_path) as fd:
        print(cur_path)
        print(fd)

'''
 with open(cur_path) as fd:
        print(fd)
'''




'''
filelist=[os.path.join(path, file) for file in ListAll if file.startswith("FuncCoverage_01_Radio_Case")]
#print(filelist)

count=0
while len(filelist):
    with open(filelist[:],"rw", encoding="utf8") as f:
        filelist2=[os.path.join(path, file2) for file2 in file if file2.startswith("FuncCoverage_01_Radio_Case") and file2.endswitch('.py')]
        count=count+1
        print(filelist2)
        os.rename(filelist2,'Radio00'+str(count))
        


'''






