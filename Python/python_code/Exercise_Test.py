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

#1/0
raise ZeroDivisionError('除数不为0')