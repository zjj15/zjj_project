#元组
print("元组")

#元组的值不可更改
tuple1=(1,2,5,6,8,9,10)
print(tuple1[:3])#1,2,5 ;0-2取不到下标3
print(tuple1[3:])#6，8,9,10；下标3到最后一个

#元组：由逗号标识
tuple2=(1)#int
print(type(tuple2))

tuple3=(1,)#tuple
print(type(tuple3))

tuple4=()#tuple
print(type(tuple4))

tuple5=(2,3,4)#tuple
print(type(tuple5))

print(8*(8))#64

print(8*(8,))#(8, 8, 8, 8, 8, 8, 8, 8)


#更新删除元组
#在元组中添加数据，在白昼后加入'哦'
tmp =('黑夜', '白昼', '不停', '歇')
tmp1=tmp[:2]+('哦',)+tmp[2:]
print(tmp1)#('黑夜', '白昼', '哦', '不停', '歇')

''' 
del tmp
print(tmp[:])#报错，tmp已被删除

'''



