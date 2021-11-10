#序列 list()
str1='i love you'
print(list(str1))
#['i', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u']

tuple1=(1,1,2,3,5,8,13,21,34)
print(list(tuple1))
#[1, 1, 2, 3, 5, 8, 13, 21, 34]


#sorted、reversed、enumerate、zip;排序、导致，自动给每个元素加索引、打包
number=[1,3,7,2,19,56,13,46,51,-8,-12,77]
print(sorted(number))
#[-12, -8, 1, 2, 3, 7, 13, 19, 46, 51, 56, 77]

#print(reversed(number))#输出一个对象
print(list(reversed(number)))
#[77, -12, -8, 51, 46, 13, 56, 19, 2, 7, 3, 1]

#print(enumerate(number))#输出一个对象
print(list(enumerate(number)))
#[(0, 1), (1, 3), (2, 7), (3, 2), (4, 19), (5, 56), (6, 13), (7, 46), (8, 51), (9, -8), (10, -12), (11, 77)]

#print(zip(number))
print(list(zip(number)))
#[(1,), (3,), (7,), (2,), (19,), (56,), (13,), (46,), (51,), (-8,), (-12,), (77,)]

number2=[12,6,43,-9,0]
print(list(zip(number,number2)))#按照元素个数少的序列匹配，number2只有5个元素，因此打包时就打包5组
#[(1, 12), (3, 6), (7, 43), (2, -9), (19, 0)]