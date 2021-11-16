#递归 函数调用自身的行为


#1
def func0():
    num=1
    for i in range(1,6):
        num*=i
    print('i is :', num)

func0()

#上面函数等价于下面的函数

def func(n):
    if n==1:
        return 1
    return n*func(n-1)

print(func(5))


#递归缺点：特别吃内存，一直在
# 栈数据存放-》弹出，return不对容易死循环

#2
def func1(n):
    if n==1 or n==2:
        return 1
    else:
        return func1(n-1)+func1(n-2)

print(func1(12))

#上面函数等价于下面的函数

def func2(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print('error')
        return -1
    if n==1 or n==2:
        print('n1 or n2:', 1)
    while n>2:
        n3=n1+n2
        n1=n2 
        n2=n3 
        n=n+1
    print('n3:',n3)

func2(2)




