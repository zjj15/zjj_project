#文件系统




f2=open(r'Python\python_code\FileTest_13.txt', 'r',encoding='utf-8',errors='ignore')
f3=open(r'Python\python_code\FileTest2_13.txt', 'r+',encoding='utf-8')

for each in f2:
    fo
    if each==':':
        (_each,_eachline)=each.split(':',1)
        f3.write(_each)
        f3.write('\n')
        f3.write(_eachline)
    else:
        print(each)
        print('###########################################')
        
#print(f3.readline())