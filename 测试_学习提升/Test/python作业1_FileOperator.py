#作业描述：USB中有三个文件夹，music/py/txt，每个文件夹中均包含任意个数的.mp3/.txt/.py文件，试使用python将所有.mp3文件放在music文件夹中，所有.txt文件放在txt文件夹中，所有.py文件放在py文件夹中


#coding=UTF-8
import os
import shutil

Udisk_name=input("请输入你的U盘名称： 格式为 x: (例：H: ) \n")
a_list=['music', 'py' , 'txt']


#进入U盘
def EnterUdisk(Udisk_name):
    #找到U盘
    #print('U盘路径为：%s' %Udisk_name)
    os.chdir(Udisk_name)
    for file in os.listdir(Udisk_name):
        #count=0
        if file in a_list:
            #print('filename: ' ,file) 
            path=Udisk_name + '\\' + file
            print('path',path)
            os.chdir(path)
            for mfile in os.listdir(path):
                #print('mfile: ',mfile)
                #print(type(mfile))
                #count+=1
                #print('测试: %d' %count)
                #print('os.getcwd()' , os.getcwd()) 

                #剪切文件，如果有重复的就覆盖并删除源文件
                if mfile.endswith('.mp3'):
                    if file =='music':
                        pass
                    else:
                        try:
                            shutil.move(path+'\\'+mfile,Udisk_name+'\\'+'music')
                        except shutil.Error:
                            os.remove(path+'\\'+mfile)


                if mfile.endswith('.py'):
                    if file =='py':
                        pass
                    else:
                        try:
                            shutil.move(path+'\\'+mfile,Udisk_name+'\\'+'py')
                        except shutil.Error:
                            os.remove(path+'\\'+mfile)
                    

                if mfile.endswith('.txt'):
                    if file =='txt':
                        pass
                    else:
                        try:
                            shutil.move(path+'\\'+mfile,Udisk_name+'\\'+'txt')
                        except shutil.Error:
                            os.remove(path+'\\'+mfile)
               
        else:
            print('跳过%s' %(file))
       
        
        #回到上层目录
        os.chdir("..")
        #print('回到上层目录： ', os.getcwd()) 
    print('执行完毕')     
             

  

#main主函数
if __name__=='__main__':
    EnterUdisk(Udisk_name)