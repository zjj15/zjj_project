#coding=utf-8
#数据类型

'''
#1.List
#1.1 title()函数 让元素第一个字符大写，list格式为 [] ,
animals=['dog','cat','sheep','pig']
print(animals[0])#dog
print(animals[0].title())#Dog
#1.2访问不知道长度的list
print(animals[-1])#倒数第1个元素
print(animals[-2])#倒数第2个元素
print(animals[-3])#倒数第3个元素
#1.3添加、删除
animals.append('wolf')#在末尾添加元素
animals.insert(0, 'tiger')#在指定下标插入元素，其他元素右移
print(animals)
#1.4排序
#1.4.1永久性排序
animals.sort()#按字母排序，但要求全是小写字母，永久排序
print(animals)
animals.sort(reverse=True)#反方向排序
print(animals)
animals.reverse()#逆序排列，永久性，可再次调用该函数回到原顺序
print(animals)
#1.4.2临时性排序,原列表顺序不变
print(sorted(animals))
print(animals)
print(sorted(animals, reverse=True))
print(animals)
#1.5 当list[-1]报错时，说明list为空
'''

'''
#2 range()函数、list 切片、复制列表
#补充：range()函数和list切片一样，取值范围为左闭右开区间，即左边能取到，右边取前一个值
#2.1 range(起始范围，终止范围，步长)、range(起始范围，终止范围)、list（range(起始范围，终止范围，步长)）、list（range(起始范围，终止范围））
for i in range(1,5):
    print(i)#1,2,3,4
for i in range(1,5,2):
    print(i)#1,3
print(list(range(1,5)))#[1,2,3,4]
print(list(range(1,5,2)))#[1,3]
_list=[i**2 for i in range(1,5)]
print(_list)#[1,4,9,16]

#2.2list切片
animals=['dog','cat','sheep','pig','wolf','tiger']
print(animals[1:3])#['cat','sheep']

#2.3复制列表
#2.3.1指向相同
animals_copy=animals
print(animals_copy)#['dog','cat','sheep','pig','wolf','tiger']
animals.append('sheep')
#2.3.2值相同，指向不同
animals_copy=animals[:]
print(animals_copy)['dog','cat','sheep','pig','wolf','tiger','sheep']
'''

'''
#3.tuple 元组
#tuple,又称不可变的列表，元素不可修改
shopt=('basketball','football','pingpang')
for value in shopt[:]:
    print(value)
#shopt[0]='modifyball'#报错
#虽然元素不可修改，但是可以直接给存储元组的变量赋值
shopt=('modify_basketball','modify_football','modify_pingpang')
for value in shopt:
    print(value)
'''

#4.字典 dict,键值对模式
#4.1 字典的格式、添加、删除
dict_aninmal={'cat':'yellow','dog':'blank','sheep':'white','fish':'red'}#格式1
_dict_aninmal={
    '_cat1':'yellow',
    '_dog':'blank',
    '_sheep':'white',
    '_fish':'red',
    '_rooster':'red',
}#格式2
dict_aninmal_={'wolf':'blank,white'}
print(dict_aninmal)
print(_dict_aninmal)
dict_aninmal['duck']='green'#添加
print(dict_aninmal)
del dict_aninmal['duck']#永久删除
print(dict_aninmal)
#4.2字典的访问
for key,value in dict_aninmal.items():
    print('key-value: '+key+':'+value)
for key in dict_aninmal.keys():
    print('key: '+key)
for key in sorted(dict_aninmal.keys()):#临时排序
    print('sorted key: '+key)
for value in _dict_aninmal.values():
    print('value: '+value)
for value in set(_dict_aninmal.values()):
    print(' set value: '+value)
#4.3字典与列表的相互嵌套，及嵌套后如何访问
#4.3.1 list里嵌套dict
list=[dict_aninmal,_dict_aninmal]
for i in list:
    print(i)
for key,value in list[0].items():
    print('list-dict key-value: '+key+':'+value)
for key in list[0].keys():
    print('list-dict key: '+key)
for value in list[0].values():
    print('list-dict value: '+value)
list.append(dict_aninmal_)
print(list)

#4.3.1 dict里嵌套list
dict_language={
    'xm':['English','Japanish','Chinese'],
    'xh':['French','Chinese'],
    'hh':['Spanish']
}
for key,values in dict_language.items():
    for value in values:
        print('dict_language: '+value)
for value in dict_language['xm']:
    print('xm: '+value)

#4.3.2字典嵌套字典
_dict_language={
    'class1':{'English':10,'Japanish':4,'Chinese':20,'French':5,'Spanish':1},
    'class2':{'English':16,'Japanish':2,'Chinese':18,'French':0,'Spanish':1},
    'class3':{'English':11,'Japanish':7,'Chinese':20,'French':6,'Spanish':0},
}
for key,value in _dict_language.items():
    for key1, value1 in _dict_language[key].items():
        print('key1-value1: '+key1+':'+str(value1))