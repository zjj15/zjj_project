#else  with
#'''
#'我不存在.txt' 不存在 所以报错：出错啦 [Errno 2] No such file or directory: '我不存在.txt'
try:
    f=open('我不存在.txt','r')
    for eachline in f:
        print(eachline)
except OSError as reason:
    print('出错啦 '+ str(reason))
finally:
    f.close()
#报错：出错啦 [Errno 2] No such file or directory: '我不存在.txt'
#Traceback (most recent call last):
#  File "c:\Users\lihang\Desktop\张晶晶Git\zjj_project\Python\python_code\Exercise_16_elsewith.py", line 11, in <module>
#    f.close()
#+NameError: name 'f' is not defined
 #'''

''' 
try:
    with open('我不存在.txt','r') as f:#使用with后不需要使用close函数
        for eachline in f:
            print(eachline)
except OSError as reason:
    print('出错啦 '+ str(reason))
#报错：出错啦 [Errno 2] No such file or directory: '我不存在.txt'

    '''

#open 和 with open区别
'''
使用open打开文件，必须要使用close关闭文件，所以，为了保证无论是否出错都能正确地关闭文件。
with open可以不用close()方法关闭文件，无论在文件使用中遇到什么问题都能安全的退出，即使发生错误，退出运行时环境时也能安全退出文件并给出报错信息。

'''