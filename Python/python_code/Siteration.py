#coding=UTF-8
#1、迭代字典，同时迭代key、value
d = {1: 'a', 2: 'b', 3: 'c'}
for key, value in d.items():
    print(key, value)

#2、判断一个对象是否可迭代
from collections import Iterable
print(isinstance("abc", Iterable))  #结果为true

#3、list实现Java那样的下标循环,可以使用python的enumerate函数(可以把list变为索引-元素对)
list = [1, 2, 3, 'asd', 4, 'd']
for i, value in enumerate(list):
    print(i, value)
