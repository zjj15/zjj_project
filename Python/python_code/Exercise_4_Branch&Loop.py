#分支和循环
#coding=UTF-8
#1.游戏_飞机大战思路：
'''
while True:
    if 用户点击关闭按钮:
        退出程序

    interval += 1
    if interval ==50:
        interval = 0
        小飞机诞生

    小飞机移动一个位置
    屏幕刷新

    if 用户鼠标产生移动:
        我方飞机中心位置 == 用户鼠标位置
        屏幕刷新

    if 我方飞机与小飞机发生冲突:
        播放撞机音乐
        修改我方飞机图案
        打印“Game over”
        停止背景音乐，最好淡出  
'''

#2.条件表达式（三元操作符）
x, y =4, 5
if x < y:
    small = x
else:
    small = y

#改进：small=x if x < y else y

#3.断言 assert,NG时抛出AssertError
#assert 3 > 4
#报错：Traceback (most recent call last):
#  File "C:\Users\lihang\Desktop\张晶晶Git\zjj_project\Python\python_code\Excecise_4_Fly_Branche&loop.py", line 38, in <module>
#    assert 3 > 4
#AssertionError

#4.循环
#while 条件：
#   循环体

#for循环
#for 目标 in 表达式：
#循环体
img='hello world'
for i in img:
    print(i,end=' ')#以空格隔开
print('\n')
#h e l l o   w o r l d 

img1=['寒冷','饥饿','交迫','冰天雪地']
for j in img1:
    print(j,len(j))
'''
寒冷 2
饥饿 2
交迫 2
冰天雪地 4
'''

#5.range(), range(start, stop),range(start,stop,step),step指的是步长
print(range(5))#range(0, 5)
print(list(range(5)))#[0, 1, 2, 3, 4]
print(list(range(2,7,1)))#[2, 3, 4, 5, 6]
print(list(range(2,7,2)))#[2, 4, 6]


#6.break,continue
#break,跳出循环
#continue,终止本轮循环并继续下一轮
for k in range(6):
    if k%2 == 0:
        print(k)
        print('continue')
        continue
    elif k%2 ==1:
        print(k)
        print('break')
        break
    else:
        print(k,'i am else')

