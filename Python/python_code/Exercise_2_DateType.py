#数据类型
#conding=UTF-8

#float
print(0.0000000000000000000000000015)#1.5e-27

print(0.1+0.2)#0.30000000000000004

a=5.99
c=int(a)
print(c)#5,把5后面的数字全部砍掉
 
b='520'
d=float(b)
print(d)#520.0

e=520
f=float(e)
print(f)#520.0

#注意：字符串在终端输出没有引号
g=5.99
h=str(g)
print(h)#'5.99' 
print("------")
print(type(h))#<class 'str'>

m=str(5e19)
print(m)#'5e+19'

#str="hello,world"
#ac=str(5e19)
#print(ac)#结果报错，为啥呢？因为这里定义了str=helloworld再使用str的话，str就代表了hello world而不是字符串转化
#Traceback (most recent call last):
#  File "C:\Users\lihang\Desktop\张晶晶Git\zjj_project\Python\python_code\Exercise_2_DateType.py", line 32, in <module>
#    ac=str(5e19)
#TypeError: 'str' object is not callable

a1=2
print(isinstance(a1,str))


