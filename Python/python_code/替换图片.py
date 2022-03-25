#替换多个文件夹下的同名图片
import os
from posixpath import dirname, split
from os import startfile


ModifyPictureName=input('请输入你要修改的图片名字: ')
print('ModifyPictureName= ' ,ModifyPictureName)


for dirpath,dirname,filename in os.walk(os.getcwd()) :
    print('dirpath: ' , dirpath)
    print('filename: ' , filename)
    if dirpath.split('\\')[len(dirpath.split('\\'))-1]=='pic':
        print('dirpath==',dirpath)
        os.chdir(os.getcwd())
        for file_name in filename:
            if file_name==ModifyPictureName:
                os.chdir(os.getcwd())
                #os.system('cd D:\\autost\\gitlab\\22tdem\\Robustness\\01_Source_AccOffOn\\USB\\USBAudio_5s.tcs\\pic ')
                # 打开文件夹窗口
                startfile(dirpath)

                
        
