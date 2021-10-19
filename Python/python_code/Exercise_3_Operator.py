#常用操作符
#除
a=10
b=8
print(a/b)#1.25
print(a//8)#1 取整数 

#取余
print(5%2)#1 

#幂
print(3**2)#9

#优先级 +-*/ ：乘除加减，单目操作符（也叫一元操作符）- 例：-3*4=》（-3）*4
#幂操作符**，：比其左侧的一元操作符优先级高，比其右侧的一元操作符优先级低
print(-3**2)#-9   -(3**2)=-9
print(3**-2)#   3**(-2)=0.1111111111111111

#比较操作符< > <= >= !=

#逻辑操作符and or not
print(not False) #Ture
print(not 1)#False
print(not 3)#False
print(3<4<5)#Ture

#优先级从左往右优先级变低,从上到下优先级变低
#幂运算 **
#正负号 +x -x 
#算术操作符 * / // + -
#比较操作符 同级别
#逻辑运算符 not and or
abc=5+8*2**-1//2
abd=7-9<0 and not 0<2 and 1>7 or 1==False
print(abc)#7
print(abd)#False
