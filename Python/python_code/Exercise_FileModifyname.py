#修改文件夹里面所有文件以及最内层.py脚本的名字
#coding=utf-8
import os


with open('C:\Users\autost\Desktop\ZjjGit\zjj_project\FileTest') as file_obj:
     content = file_obj.read()
     print(content)

'''

#get路径，进入文件任意一层
os.getcwd()
path=os.getcwd()+'\FileTest'

#输出所有文件,包含文件夹
ListAll=os.listdir(path)

for file in ListAll:
    cur_path=os.path.join(path,file)


for dirpath,dirname,filenames in os.walk(path):
    print(filenames)

'''

'''
ListAll=os.listdir(path)

for file in ListAll:
    cur_path=os.path.join(path,file)
    list2=os.listdir(cur_path)#返回path指定的文件夹包含的文件或文件夹的名字的列表。
    print(list2)
    fd=os.system(cur_path)
    print(fd)

'''

    
            


'''
for file2 in fd:
        print(file2)
        if file2.startswith("FuncCoverage_01_Radio_Case") and file2.endswitch('.py'):
            print(file2)


'''




'''
    for file2 in file:
        print(file2)
        if file2.startswith("FuncCoverage_01_Radio_Case") and file2.endswitch('.py'):
            print(file2)
'''

    
'''
filename=[filename for file2 in file if file2.startswith("FuncCoverage_01_Radio_Case") and file2.endswitch('.py')]
    print(filename)
'''


'''
 with os.open(cur_path, os.O_RDWR) as In_cur_path:
        print(In_cur_path)

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






