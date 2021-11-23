#异常处理
'''
file_name=input('请输入文件名： ')
file=open(file_name)
for eachline in file :
    print(eachline)
'''

#1.try/except
'''
try:
    执行代码1（如果这里就出错了 那代码2不会被执行）
    执行代码2
except:
    发生异常时执行的代码
'''

try:
    file_name=input('请输入文件名： ')
    file=open(file_name)
    for eachline in file :
        print(eachline)
except OSError as reason:#FileNotFoundError属于OSError
    print("文件出错啦" +str(reason))#请输入文件名： pp 文件出错啦[Errno 2] No such file or directory: 'pp'

try :
    sum=1+'1'
except TypeError as reason:
    print("文件出错啦" +str(reason))#文件出错啦unsupported operand type(s) for +: 'int' and 'str'


try :
    sum=1+'1'
except TypeError as reason:
    print("文件出错啦" +str(reason))#文件出错啦unsupported operand type(s) for +: 'int' and 'str'
except OSError as reason:
    print('文件出现错误'+str(reason))


try :
    sum=1+'1'
except (TypeError,OSError):
    print('文件出现错误')


#try/exccept/finally
'''
try:
    执行代码
except Exception[as reason]:
    出现异常后执行的代码
finally:
    无论如何都会被执行的代码

'''



try:
    f1=open('我存在.txt','w',encoding='utf-8')
    print(f1.write('写入'))
    sum=1+'1'
except(OSError,TypeError):
    print('出错了')
finally:
    f1.close()


#try/except/else/finally
'''
try:
    执行语句1
except:
    出现异常时执行的语句
else:
    未出现异常时执行的语句
finally:
    不管有没有异常都会执行
    
'''

#raise

if 1/0:
    raise ZeroDivisionError('除数不为0')

