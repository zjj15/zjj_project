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




    










