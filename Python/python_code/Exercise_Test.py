#类的变量、对象的变量
class People:
    populate=0#类变量

    def __init__(self,name):
        People.populate+=1
        self.name=name #对象变量
        print('i am __init__ fun ')  

    def __delattr__(self):
        People.populate-=1
        print('i am  __delattr__ func')

    def sayHi(self):
        print('People.populate is %s' %People.populate)
        print('i am %s' %(self.name))

p=People('小明')
p.sayHi()
    
'''
i am __init__ fun
People.populate is 1
i am 小明

'''
