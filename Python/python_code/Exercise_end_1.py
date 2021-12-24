#python 补充
#可以但不推荐的几种情况

# 1.如果你的语句块只包含一句语句，那么你可以在条件语句或循环语句的同一行指明它
flag=input("please input whatever you want: ")
if flag: print('yes')

#2.使用列表综合
list1=[1,2,3,4,5]
list2=[i*2 for i in list1 if i>2]
print(list2)
#[6, 8, 10]

