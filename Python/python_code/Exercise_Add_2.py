#glob函数
import glob

#1.打印当前目录下所有的.py文件
for i in glob.glob('./*.py'):
    print(i)
    print('\n')