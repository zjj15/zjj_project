#类和对象
#对象=属性+方法
class Cat:
    #属性
    color='yellow and white'
    legs=4
    eyes=2
    weight=10
    mouth='大嘴'

    #方法
    def climb(self):
        print('he can climb Catshlf')
    def Eat(self):
        print('he can eat egg by his mouth')
    def Bite(self):
        print('he bite me everyday')


GouTou=Cat()
GouTou.climb()
GouTou.Eat()

#面向对象编程的特征：1.封装
list1=[2,1,7,5,3]
list1.append(9)#封装了append函数 list1 就相当于一个对象
print(list1)

#面向对象编程的特征：2.继承
class MyList(list):#list 为列表关键字
    pass

list2=MyList()
list2.append(9)
list2.append(6)
print(list2)#[9,6] list2 继承了list的所有方法

#1. Teacher 和 student 都继承People类 
class People:
    name='w'
    age=10
    __weight=100#私有变量
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
        print('init_基类：  People')
    def getweight(self):
        return self.__weight
    def speak(self):
        print('基类：people')


class Teacher(People):
    ability='Teach student'
    def __init__(self, n, a, w,ab):
        People.__init__(self,n,a,w)
        self.ability=ab
        print('init_继承类：  Teacher')
    def speak(self):
        print('继承类：  Teacher')


class Student(Teacher):
    school='Num1 Middle School'
    def __init__(self, n, a, w, ab,s):
        #super().__init__(n, a, w)
        People.__init__(self,n, a, w)
        Teacher.__init__(self,n, a, w,ab)
        self.school=s
        print('init_继承类：  Student')
    def speak(self):
        print('继承类：Student')

student=Student('WG',18,118,'Num1 Middle School','study')

#2. 




#面向对象编程的特征：3.多态
#多态的概念其实不难理解，它是指对不同类型的变量进行相同的操作，它会根据对象(或类)类型的不同而表现出不同的行为。
class A:
    def fun(self):
        print('我是A')

class B:
    def fun(self):
        print('我是B')

a=A()
b=B()
print(a.fun()) 
print(b.fun())

#4.self
#类的方法和普通函数只有一个特别的区别就是：类的方法必须有一个额外的第一个参数名称Self
#self作用：相当于this指针;__init__(self)是构造函数，类的实例化操作会自动调用构造方法
class Home:
    def __init__(self,num_member):
        self.num_member=num_member
    def name(self):
        name=input('请输入家庭成员姓名：')
        print('家庭成员个数：',self.num_member)
        print('输出成员姓名： ',name)

home=Home(3)
home.name()
'''
请输入家庭成员姓名：狗头航、狗头晶、狗头
家庭成员个数： 3
输出成员姓名：  狗头航、狗头晶、狗头
'''

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()#<__main__.Test object at 0x0000015E45247580>
t.prt()#<class '__main__.Test'>
#从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
#self 不是 python 关键字，我们把他换成 this 也是可以正常执行的:
class Test:
    def prt(this):
        print(this)
        print(this.__class__)
 
t = Test()#<__main__.Test object at 0x0000015E45247520>
t.prt()#<class '__main__.Test'>

class Test:
    def __init__(self,re,imag):
        self.r=re
        self.im=imag
        print(self.r+self.im)

complex=Test(3.0 , 4.0)#7.0

class Test2:
    r=1.0
    im=2.0
    def __init__(self,re,imag):
        self.r=re
        self.im=imag
        print(self.r+self.im)

complex=Test2(3.0 , 4.0)#7.0






















#私有和公有
#私有使用__作为标识
class Person:
    __name='gt'
    def getname(self):#通过函数返回name变量
        return self.__name


p=Person()
#print(p.__name())#报错：AttributeError: 'Person' object has no attribute '__name'
print(p.getname())#gt
print(p._Person__name)#gt 对象._类名__变量名




