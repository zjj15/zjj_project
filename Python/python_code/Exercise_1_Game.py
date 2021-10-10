#coding=UTF-8
import random

# #GAME,用户只能输入4次
# print("Let's play a Game!")

# #1 自己写的
# count=1
# print("---------第%d次输入-------" %(count))

# Temp=input("输出你猜的数字：")
# Guess=int(Temp)

# while Guess != 8 :#这里的guess指的是上面一句的guess
#     count=count+1
#     print("---------第%d次输入-------" %(count))
#     if (Guess > 8) and (count < 5):
#         Temp=input("猜大了，请重新输入：")
#         Guess=int(Temp)#这里的guess是新的guess和第33行的guess没有任何关系
#     elif (Guess < 8) and (count < 5):
#         Temp=input("猜小了，请重新输入：")
#         Guess=int(Temp)#这里的guess是新的guess和第33行的guess没有任何关系
#     elif count == 5 :
#         print("次数用尽了")
#         print("游戏退出！")  
#         break  
# else :
#     print("我的天爷呀，猜对了！")
#     print("游戏退出！")
  


#新要求：8改为1到10之间的随机数
#2别人写的
print("Let's play a Game!")
secret=random.randint(1,10)
print("secret is: %d" %secret)
count2=1
print("---------第%d次输入-------" %(count2))
temp=input("输出你猜的数字：")
guess=int(temp)
count2=count2+1

if guess==secret:
    print("我的天爷呀，一下子就猜对了！")
else:
    while (guess != secret) and (count2 < 5):#这里的guess指的是上面一句的guess
        print("---------第%d次输入-------" %(count2))
        if guess==max(guess,secret):
            temp=input("猜大啦，请重新输入你猜的数字：")
        else:
            temp=input("猜小啦，请重新输入你猜的数字：")
        guess=int(temp) #这里的guess是新的guess和第33行的guess没有任何关系
        count2=count2+1
        if guess==secret:
            print("我的天爷呀，猜对了！")
    print("次数用尽了，游戏结束")

