
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod()

#导入单个类；从一个模块中导入多个类
#有一个car.py的脚本里面写了Car类、ElectricCar类
#from car import Car
#from car import Car, ElectricCar