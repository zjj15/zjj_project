#print的使用


from typing import Counter


print(100,end='\n')
print(200)
print(300)
#100
#200
#300

print(100,end='打印完成')#打印完成后以end作为结束标志，end默认是'\n'
print(200)
print(300)
#100打印完成200
#300


print(100,200,300)
#100 200 300 默认是用空格隔开
print(100,200,300,sep='\n')#修改打印多个数据之间的方式
#100
#200
#300

print(100,200,300,sep='\n',end='ok')
#100
#200
#300ok 

print('\n')
print(100,200,300,sep='=',end='ok')
#100=200=300ok

print('\n')
str1="a""123"#a和123之间的两个双引号自动被忽略
print(str1)#a123

print('今天天气好吗', end='\n123')
#今天天气好吗
#123


print('\n')
print("1234kkk中文@@！！")


a=12
print(a)#12

#多字段
print("我的名字：%s,我的身高：%f,我的年龄：%d, 我的英文名第一个字母: %c" %('张三',1.79,26,'G'))
#我的名字：张三,我的身高：1.790000,我的年龄：26, 我的英文名第一个字母: G

#单引号
print("I'm student")
#I'm student
print('I\'m student')
#I'm student


#格式化
count='Google'
print('{} is what?'.format(count))
#Google is what?

#格式化字符串 f string 
print(f'{count} is what?')
#Google is what?

print('%s is what?' %count)
#Google is what?



