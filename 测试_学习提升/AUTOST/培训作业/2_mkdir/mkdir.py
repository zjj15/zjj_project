import os
from shutil import copyfile
#import psutil
#进入USB

folder_num = 50
folder_layers = 10
usb_disk = "F:"
sourceFilePath = "D:\\PY\\application\\2_mkdir\\music.mp3"

def enterUSB(diskname):
#遍历字母A到Z，忽略光驱的盘符
    print("当前工作路径：",os.getcwd())
    for i in range(65,91):
        vol = chr(i) + ':'
        if os.path.isdir(vol):
            print(vol)
            if vol == diskname:
                os.chdir(vol)
                print("修改后工作路径：",os.getcwd())
                print("成功进入USB目录")
                break
            else:
                print("无法进入USB目录")
                
def emptyUSB():
    usb_path = os.getcwd()
    if os.getcwd()!=(usb_disk+"\\"):
        print("当前不在usb路径")
        return
    for root, dirs, files in os.walk(usb_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    if os.listdir(os.getcwd()) == []:
        print("成功清除usb中数据")
    
    
def copyFileToUSB():
    for i in range(1,folder_num):
        os.chdir(usb_disk+"\\")
        os.mkdir("folder"+str(i))
        for j in range(1,folder_layers): 
            os.chdir(usb_disk+("\\"+"folder"+str(i))*j)
            os.mkdir("folder"+str(i))
            
        targetFilePath = usb_disk+("\\"+"folder"+str(i))*(j+1)+"\\music.mp3"
     
        try:
            copyfile(sourceFilePath, targetFilePath)
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)
        print (os.listdir(os.getcwd()))
        
        
        
       
enterUSB(usb_disk)
emptyUSB()
copyFileToUSB()


    