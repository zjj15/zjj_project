#1.文件
#涉及到的函数；f.close();f.read(size)按字节读取;
#conding=UTF-8

from os import error


f=open(r'Python\python_code\FileTest_13.txt', 'r',encoding='utf-8',errors='ignore')
print('f.read: \n', f.read())

f.seek(5,0)
#offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
#whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

print('f.readline: \n', f.readline())

print(list(f))
#['crowned with milk-white may;\n', 'in fleecy flocks of light,\n', "o'er heaven the white clouds stray;\n", 'white butterflies in the air;\n', 'white daisies prank the ground;\n', 'the cherry and hoary pear,\n', 'scatter their snow around.']


f.seek(0,0)#指针放到初始位置
for eachline in f:
    print(eachline)


f1=open(r'Python\python_code\FileTest2_13.txt', 'r+',encoding='utf-8',errors='ignore')
f1.write('apple')
print(f1.readline())

f.close()
f1.close()


#2.文件分割split() 
'''
通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
#str.split(str="", num=string.count(str)).
参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
'''

f2=open(r'Python\python_code\FileTest_13.txt', 'r',encoding='utf-8',errors='ignore')
f3=open(r'Python\python_code\FileTest2_13.txt', 'r+',encoding='utf-8',errors='ignore')
for each in f2:
    if each==':':
        (_each,_eachline)=each.split(':',1)
        f3.write(_each)
        f3.write(_eachline)
        
        
print(f3.readline())