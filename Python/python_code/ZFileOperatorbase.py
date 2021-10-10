#coding=UTF-8
#读取文件夹
import os

#读取path下的文件夹
def File_Traveral():
    file=os.listdir(path)
    print("file name: " , file)


#endswith、startswith判断文本以什么结尾和开头
text="hello world"
print( text.startswith('e'))#false
print( text.startswith('h'))#true

def File_Traveral2():
    file=os.listdir(path)
    for code in file:
        if code.endswith(".py"):
            print("1.py file nam: " , code)
        else:
            print(print("2.not py file name: " , code))


def File_baseoperator():
    with open(r'C:\Users\lihang\Desktop\zjj\README.txt', 'a+', encoding='gbk') as f:
        #f.readlines()
        f.write("hello world")


def FilebaseW():
    f=open(r'C:\Users\lihang\Desktop\zjj\a.txt', 'w+', encoding='utf-8')
    f.write('你叫啥？')
    f.write('张晶晶')
    f.close()

def FilebaseR():
    f=open(r'C:\Users\lihang\Desktop\zjj\a.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close

def FilebaseWR():
    f=open(r'C:\Users\lihang\Desktop\zjj\b.txt', 'a+', encoding='utf-8')
    f.write('你叫啥？')
    f.write('王立航')
    f.seek(0, 0)# 把文件指针从末尾移到开头，没有这句话下面的read()就读不到正确的东西
    print(f.read())
    f.close()

 



if __name__=='__main__':
    path=r'C:\Users\lihang\Desktop\zjj_learn_py'
    #File_Traveral()
    #File_Traveral2()
    #File_baseoperator()
    #FilebaseW()
    #FilebaseR()
    #FilebaseWR()