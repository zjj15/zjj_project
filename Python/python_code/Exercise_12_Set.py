#集合set
#1.集合与字典
num1={}
num2={1:'h',2:'e',3:'l',4:'l',5:'o'}
num3={1,2,3,4,5}
num4={1,2,2,2,3,3,4,5}

print(type(num1))#<class 'dict'>
print(type(num2))#<class 'dict'>
print(type(num3))#<class 'set'>
print(type(num4))#<class 'set'>
print(num4)#{1, 2, 3, 4, 5} 集合元素不重复，自动剔除重复元素；元素是无序的，不支持索引


#2.set 集合关键字的使用
set1=set([1,2,3,4,5,6,6,6,6])
print(set1)#{1, 2, 3, 4, 5, 6}

#3.去重
#没有集合前：
tmp=[]
for each in num4:
    if each not in tmp:
        tmp.append(each)

print(tmp)#[1, 2, 3, 4, 5]

#有了集合以后；集合是无序的，会导致该list也无序
print(list(set(num4)))#[1, 2, 3, 4, 5]

#4.集合内置方法
#add
num4.add(7)
print(num4)#{1, 2, 3, 4, 5, 7}
#remove
num4.remove(5)
print(num4)#{1, 2, 3, 4, 7}

#frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
num5=frozenset([1,6,9,23,5])
print(num5)#frozenset({1, 23, 5, 6, 9})
'''
num5.add(88)
print(num5)#出错，冻结后集合不能再添加或删除任何元素

'''




