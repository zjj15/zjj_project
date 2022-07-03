#glob函数
import glob

#1.打印当前目录下所有的.py文件
for i in glob.glob('./*.py'):
    print(i)
    print('\n')


#https://blog.csdn.net/hehedadaq/article/details/81836025
# for循环，若要平行迭代兩個 list，你需要的是 zip 或 zip_longest