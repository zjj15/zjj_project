#python 补充
#可以但不推荐的几种情况

# 1.如果你的语句块只包含一句语句，那么你可以在条件语句或循环语句的同一行指明它
flag=input("please input whatever you want: ")
if flag: print('yes')


#2.使用列表综合
list1=[1,2,3,4,5]
list2=[i*2 for i in list1 if i>2]
print(list2)
#[6, 8, 10]


#3.lambda表达式
#3.1. 单独的表达式
sum= lambda n: n*2
print('输出lambda表达式： ' , sum(5) )#10

#3.2.用在函数返回值里
def Func():
    return lambda num:num*2+1

#Func_Sum接收return 返回值
Func_Sum=Func()

#调用lambda表达式
print(Func_Sum(6))#13

#3.3.lambda x:x+1 在这里 lambda后面紧跟的x是输入，后面的x+1是输出
def Func1(avg1):
    value=avg1*2-1
    return lambda s: value-s

ssum=Func1(3)
print(ssum(1))#4


#4.



