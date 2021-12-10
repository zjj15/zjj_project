import os
import shutil
from shutil import copyfile
#import psutil

usb_disk = "L:"

#进入USB
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
                print("成功进入USB目录 \n====================================")
                break
            else:
                print("无法进入USB目录")

#进入USB中名为FolderName的文件夹
def enterFolder(FolderName):
    usb_path = os.getcwd()
    if os.getcwd() != (usb_disk + "\\"):
        print("当前不在usb路径")
        return
    FolderPath = os.path.join(usb_path,FolderName)
    #判断FolderPath是否为文件夹
    if os.path.isdir(FolderPath):
        os.chdir(FolderPath)
        print("成功进入" + FolderName + "目录 \n......")
    else:
        print(FolderName+"文件夹不存在或进入失败 \n====================================")

#遍历文件夹和文件并移动
def moveFile():
    #遍历Music/Txt/Py文件夹中每层文件夹
    for folderLayer in os.walk(os.getcwd()):
        #遍历每层文件夹下的每个文件
        for file in folderLayer[2]:
            #获取每个文件的后缀名
            SuffixOfFile = file[file.find("."):]
            #后缀名为.mp3
            if SuffixOfFile == ".mp3":
                #分别定义拷贝的源文件地址和目标文件地址    
                sourceFilePath = folderLayer[0] + "\\" + file
                targetFilePath = usb_disk + "\\Music\\" + file
                #源文件地址和目标文件地址必须不一致
                if sourceFilePath != targetFilePath:
                    copyFileToUSB(sourceFilePath,targetFilePath)
            #后缀名为.txt
            elif SuffixOfFile == ".txt":
                #分别定义拷贝的源文件地址和目标文件地址    
                sourceFilePath = folderLayer[0] + "\\" + file
                targetFilePath = usb_disk + "\\Txt\\" + file
                #源文件地址和目标文件地址必须不一致
                if sourceFilePath != targetFilePath:
                    copyFileToUSB(sourceFilePath,targetFilePath)
            #后缀名为.py
            elif SuffixOfFile == ".py":
                #分别定义拷贝的源文件地址和目标文件地址    
                sourceFilePath = folderLayer[0] + "\\" + file
                targetFilePath = usb_disk + "\\Py\\" + file
                #源文件地址和目标文件地址必须不一致
                if sourceFilePath != targetFilePath:
                    copyFileToUSB(sourceFilePath,targetFilePath)
            #其他类型文件不做操作
            else:
                pass
    #结束后让当前路径重新回到"L:\"
    os.chdir(usb_disk + "\\")
def copyFileToUSB(sourceFilePath,targetFilePath):
    try:
        copyfile(sourceFilePath, targetFilePath)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        exit(1)
    #删除源文件
    os.remove(sourceFilePath)

#清空FolderName文件夹中的空白文件夹    
def deleteFolder(FolderName):
    #更改当前文件路径
    os.chdir(os.path.join(os.getcwd(),FolderName))
    for folderLayer in os.walk(os.getcwd()):
        if folderLayer[2] == []:
            #os.rmdir(os.path.join(folderLayer[0],folderLayer[1]))
            #os.rmdir(folderLayer[0])
            shutil.rmtree(folderLayer[0])
    #结束后让当前路径重新回到"L:\"
    os.chdir(usb_disk + "\\")
       
enterUSB(usb_disk)
enterFolder("Music")
moveFile()
print("mp3文件已整理完毕！ \n====================================")
enterFolder("Txt")
moveFile()
print("txt文件已整理完毕！ \n====================================")
enterFolder("Py")
moveFile()
print("py文件已整理完毕！ \n====================================")
deleteFolder("Music")
deleteFolder("Txt")
deleteFolder("Py")
print("空白文件夹已清理完毕！ \n====================================")
print("文件全部整理完毕！ \n====================================")

    