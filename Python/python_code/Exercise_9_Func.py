#函数
def MyFirstFunction():
    print('打印函数：MyFirdtFunction')


def MySecondFunction(id,name,grade):
    print('%d, %s, %f' %(id,name,grade)) 

def MyThirdFuncion(num1,num2):
    return num1+num2

MyFirstFunction()
MySecondFunction(1,'张三',89)
print(MyThirdFuncion(3, 4))


#形参，实参，形参指的是变量名，占一个参数位置，实参指的是具体的参数
def MyFourthFunction(name):
    'name 是函数的形参'
    print("name :%s" %name)


MyFourthFunction('陆千')#name :陆千
print(MyFourthFunction.__doc__)#name 是函数的形参

help(MyFourthFunction)#输出如下：
'''
Help on function MyFourthFunction in module __main__:

MyFourthFunction(name)
    name 是函数的形参
'''

#关键字参数
def MyFiveFunction(name,words):
    print(name+'->'+words)

MyFiveFunction(words='吃树皮', name='王立航')#调用时标注哪个参数是哪个内容


#默认参数
def MySixFunction(name='王立航',words='吃树皮了'):
    print(name+'->'+words)

MySixFunction()#王立航->吃树皮了;如果不带参数就会执行默认参数
MySixFunction(name='王狗', words='吃猪了')#王狗->吃猪了


#收集参数/可变参数
def MySevenFunction(*avg):#形参前加*
    print('参数的长度是： %d' %(len(avg)))
    print('第二个参数是: %s' %(avg[1]))


MySevenFunction('王臭狗','zhu',3.14,0.151926)
'''
参数的长度是： 4
第二个参数是: zhu
'''
def MyNineFunction(*avg,exp):
    print('avg参数的长度是： %d' %(len(avg)))
    print('第二个参数是: %s' %(avg[1]))
    print('exp: ' ,exp)

MyNineFunction('hello',6,9,'zhu',3.89,-9,exp='*9')
'''
avg参数的长度是： 6
第二个参数是: 6
exp:  *9

'''


#返回值
def Func1():
    print('Hello 1')

temp=Func1()#Hello 1
print(temp)#None,函数无返回值时 返回None对象

def Func2():
    return [1,2,7.8,'str']
print(Func2())#[1, 2, 7.8, 'str']

def Func3():
    return 1,4,8,'ok'
print(Func3())#(1, 4, 8, 'ok') 逗号默认是元组


#局部变量，全局变量
#函数内部使用栈存储数据

def Func4(price,rate):
    print("old price: ",old_price)#打印的old_price是全局变量
    return price*rate

old_price=float(input('please input price: '))
rate=float(input('please input rate: '))
new_price=Func4(old_price,rate)
print('after discounts the price is : ',new_price)


def Func5(price,rate):
    #print("old price: ",old_price)#打印的old_price是全局变量
    old_price=50
    #在局部变量里试图修改全局变量的值，python会生成一个和全局变量同名的局部变量，由于局部变量和全局变量的存储位置不同，所以这是两个值互不影响
    print('1 after modify old_price is: ',old_price)#50
    return price*rate

old_price=float(input('please input price: '))
rate=float(input('please input rate: '))
new_price=Func5(old_price,rate)
print('2 after modify old_price is: ',old_price)#第109行输入的old_price

print('after discounts the price is : ',new_price)




#global关键字
count=5
def Func6():
    count=10
    print(count)

Func6()# 10
print(count)#5


num=5
def Func7():
    global num
    num=10
    print(num)

Func7()#10
print(num)#10



#内嵌函数
def MyFunc1():
    print("MyFunc1")
    def MyFunc2():
        print('MyFunc2')
    MyFunc2()

MyFunc1()

#闭包
def MyFunc3(x):
    def MyFunc4(y):
        return x * y
    return MyFunc4

print(MyFunc3(5)(8))#40

'''
def MyFunc5():
    x=5
    def MyFunc6():函数值存放在栈里
        x*=x#屏蔽外部x，使用局部未定义的x
        return x
    return MyFunc6()
    #改进方法
    '''


def MyFunc5():
    x=[5]
    def MyFunc6():#函数值存放在栈里
        x[0]*=x[0]#x[0]就是5
        return x[0]
    return MyFunc6()

print(MyFunc5())


def MyFunc5():
    x=5
    def MyFunc6():
        nonlocal x#关键字意思是：不是局部变量
        x*=x
        return x
    return MyFunc6()

print(MyFunc5())

#lambda表达式
def func(x):
    return 2*x+1

#等同于
lambda x:2*x+1
g=lambda x:2*x+1
print(g(5))# 

lambda x,y:x+y
g=lambda x,y:x+y
print(g(3,4)) 

#过滤器 filter(函数名，iterable)
def func2(x):
    return x%2

temp=range(10)
show=filter(func2, temp)#对象
print(list(show))#[1, 3, 5, 7, 9]

show=list(filter(lambda x:x%2, range(10)))
print(show)#[1, 3, 5, 7, 9]

#map 映射 map(函数名，iterable),把第二个参数里每一个值带入到第一个函数里运算并返回
show=list(map(lambda x:x%2,range(10)))
print(show)#[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


    










