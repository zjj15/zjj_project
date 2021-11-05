'''
Author: your name
Date: 2021-11-04 12:18:23
LastEditTime: 2021-11-04 13:09:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python_code\Exercise_5_Array.py
'''
#数组
#1.创建混合列表、空列表
mix=[1,'耳机',3.14,[1,2,3]]
print(mix)
empty=[]
print(empty)
#2.列表操作,在尾部插入append、extend；append参数为：一个数据，extend参数为: 一个列表
#append()和extend()方法都是用来添加数据到list末尾的，两者的区别：
#append()添加的时候会把添加的数据当成一个整体进行添加，允许添加任意类型的数据
#extend()添加的时候会把添加的数据迭代进行添加，只允许添加可迭代对象数据（可迭代对象： 能用for循环进行迭代的对象就是可迭代对象， 比如：字符串，列表，元祖，字典，集合等等 ）
member=['猫','狗','土狗','兔毛','土猫']
member.append('哈士奇')
member.extend(['竹林','迷离'])
member.extend('黄鹂')
print(member)
#['猫', '狗', '土狗', '兔毛', '土猫', '哈士奇', '竹林', '迷离', '黄', '鹂']

#3.在任意位置插入 insert(位置,内容)
member.insert(1,'猪')
print(member)
#['猫', '猪', '狗', '土狗', '兔毛', '土猫', '哈士奇', '竹林', '迷离', '黄', '鹂']

#4.获取列表值
print(member[0],member[1])#猫 猪
#临时交换
temp=member[0]
member[0]=member[1]
member[1]=temp
print(member[0],member[1])#猪 猫


#列表分片
print(member[1:3])#下标为1、2的值 

print(member[:])#所有的值

print(member[-3:-1])#['迷离', '黄']#下标为-3 -2的值

print(member[-11:-1])#下标从-11到-2的值，最后一个值下标是-1
#['猪', '猫', '狗', '土狗', '兔毛', '土猫', '哈士奇', '竹林', '迷离', '黄']

print(member[-11:])#所有的值：下标从-11到-1的值
#['猪', '猫', '狗', '土狗', '兔毛', '土猫', '哈士奇', '竹林', '迷离', '黄', '鹂']

#列表拷贝
member2=member[:]
print(member2)


#5.删除元素remve()、del、pop()、pop(下标)
#删除不存在的元素会报错
#member.remove('意境')
#print(member)#ValueError: list.remove(x): x not in list

member.remove('竹林')
print(member)

del member[0]
print(member)

member.pop()#不加参数默认删除最后一个值
print(member)

member.pop(6)#加参数：下标
print(member)


#6.操作符在列表中的使用
list1=[123]
list2=[234]
print(list1 >  list2)#False
list3=[123,456]
list4=[234,123]
print(list1 >  list2)#False,和AScll比较方法一致

list5=list1+list2 # +号两边类型一致,错误示范：list1+'apple'，尽量别用加号而用extend
print(list5)

print(list1 * 3)
list1 *= 4
print(list1)

print('--------in not in----------------')
print(123 in list1)#true
print(123 in list2)#false
print(123 not in list1)#false
print(123 not in list2)#true

print('--------list[list]---------------')
list7=[123,[123,456],789]
print(123 in list7)#true
print(456 in list7)#false,列表里边的列表
print(456 in list7[1])#true
print(list7[1][1])#456
print(list3 in list7)#true



#FBI(内置函数)
list8=[123,222,344,678,[999,101,'mu',123,'牡丹',678],'p',123,'驴',878,678,545,'hudie']
list9=[90,78,123,456,1,34]
#1.count,计算某个数据出现的次数
print(list8.count(123))#2次

#2.index，返回参数在列表中的位置
print(list8.index(678))#3,位置下标为3

#print(list8.index(678,4,8))#报错， 678 is not in list
print(list8.index(678,4,11))#9，index(数据，查找范围start,查找范围stop)

#3.reverse,反转
list8.reverse()#没有返回值,打印出来是None
print(list8)

#4.sort,排序
list9.sort()#没有返回值,打印出来是None;sort有3个默认参数sort(排序函数func,默认是归并排序，归并排序的参数，reverse=false,默认是false)
print(list9)
#想从大到小排序
list9.sort(reverse=True)
print(list9)



#************list的深浅拷贝************
print('************list的深浅拷贝************')
list9.reverse()
print(list9)#[1, 34, 78, 90, 123, 456]

list10 = list9[:]#使用分片浅拷贝，拷贝一份list9
print(list10)#[1, 34, 78, 90, 123, 456]

list11=list9#深拷贝，list10指向list9
print(list11)#[1, 34, 78, 90, 123, 456]

#************
list9.reverse()#[456, 123, 90, 78, 34, 1]
print(list10)#[1, 34, 78, 90, 123, 456]
print(list11)#[456, 123, 90, 78, 34, 1]
