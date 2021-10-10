#coding=UTF-8
#1、列表生成式
print(list(range(1, 11)))  #生成1-10的数字list

#2、如果要生成1*1、2*2、3*3。。。。

print(list(x * x for x in range(1, 10)))

#3、
[m + n for m in "abc" for n in "xyz"]

#4、dict
d = {'a': "X", 'b': 'Y', 'c': 'Z'}
print([k + "=" + v for k, v in d.items()])

#列出目录下所有文件和目录名
import os
print([d for d in os.listdir('.')])

#print(d for d in os.listdir('.'))
# 上一句运行出错，错误原因为下一行内容，原因是()代表生成了迭代器对象，[]代表生成的是list对象
#运行结果出现generator object <genexpr> at 0x0000017BEBAB46D8
#https://blog.csdn.net/Eider1998/article/details/102489591

#5、#由于lower函数只能用于字符串，非字符串类型没有lower函数；但是isinstance("abc", str)函数可以判断一个对象是不是字符串
#给这句话加个if使语句表达正确
L1 = ['hello', 'world', 18, 'apple', 'none']
#[s.lower() for s in L1]

#wrong: [i for i in L1 if isinstance(L1, str)=='False' L2.append(i) ]
#right
[s.lower() if isinstance(s, str) else s for s in L1]

print([s.lower() if isinstance(s, str) else s for s in L1])

#生成器与list对象的打印方式
g = (x * x for x in range(1, 10))
for n in g:
    print(n)

L = [x * x for x in range(1, 10)]
print(L[:])  #print(L)
