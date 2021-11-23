#文件系统
'''
#1.文件
f2=open(r'Python\python_code\FileTest_13.txt', 'r',encoding='utf-8',errors='ignore')
f3=open(r'Python\python_code\FileTest2_13.txt', 'r+',encoding='utf-8')
f4=open(r'Python\python_code\FileTest3_13.txt', 'r+',encoding='utf-8')



for each in f3:#一行
    for estr in each:
        if estr==':':
            (_each
            ,_eachline)=each.split(':',1)
            f4.write(_each)
            f4.write('\n')
            f4.write(_eachline)   
        else:
            continue
f4.write('\n')


f2.close()
f3.close()
f4.close()
''' 

#2.文件系统
#1. os模块
import os
path1=os.getcwd()

print(os.getcwd())#C:\Users\lihang\Desktop\张晶晶Git\zjj_project\Python\python_code

#os.system('cmd')

#2. os.path模块
print(os.path.basename("张晶晶Git\\zjj_project\Python\python_code\FileTest3_13.txt"))
#去掉路径只显示最后的文件 FileTest3_13.txt

#2.1 os.path.join(path1[,path2[,path3]]) 将path1，path2各部分组合成一个路径名

print(os.path.join(path1,'FileTest1_14.txt'))
#C:\Users\lihang\Desktop\张晶晶Git\zjj_project\Python\python_code\FileTest1_14.txt

print(os.path.join('C:\\','A','B','1.txt'))
#C:\A\B\1.txt

#2.2 split(path)分割文件名和路径，所以，如果完全使用目录他也会将最后一个目录分离且不会判断文件或目录是否存在
print(os.path.split(path1))
#('C:\\Users\\lihang\\Desktop\\张晶晶Git\\zjj_project\\Python', 'python_code')

#2.3 splitext(path) 将文件和扩展名分离
print(os.path.splitext('C:\\A\\B\\1.txt'))
#('C:\\A\\B\\1', '.txt')

#2.4 os.path.exists(path)	路径存在则返回True,路径损坏返回False
print(os.path.exists('C:\\A\\B\\1.txt'))#False

#2.5 os.path.isabs(path)	判断是否为绝对路径
print(os.path.isabs('C:\\A\\B\\1.txt'))#True

#2.6 os.path.isfile(path)	判断路径是否为文件
print(os.path.isfile(path1))#False

#2.7 os.path.isdir(path)	判断路径是否为目录
print(os.path.isdir(path1))#True

#2.8 ismount 是否是一个挂载点;A B C D E这些盘都是挂载点 
print(os.path.ismount('C:\\'))#True
print(os.path.ismount('C:\\A'))#False




#永久存储 pickle
import pickle
file_content=[
"w:spring goeth all in white,F:crowned with milk-white may;W:in fleecy flocks of light,F:o \'er heaven the white clouds stray;W:white butterflies in the air;F:white daisies prank the ground;W:the cherry and hoary pear,F:scatter their snow around."]

#将FileTest2_13中的内容存储到FileTest2_14.txt
pickle_file=open('FileTest2_14.txt', 'wb')
pickle.dump(file_content, pickle_file)
pickle_file.close()

#读取
pickle_file=open('FileTest2_14.txt', 'rb')
content=pickle.load(pickle_file)
print(content)
