from autost.api import *

DEV1 = ST.DEV1
DEV3 = ST.DEV3
errType = 'bt_connect_error'

#phone操作
#1.让手机设备处于可发现状态
def Phone_CanBeFind():
    touch(Template('pic/phone_设置.png'), device=DEV3)
    touch(Template('pic/phone_连接.png'), device=DEV3)
    touch(Template('pic/phone_BT.png'), device=DEV3)


if exists(Template('pic/BT_Setting.png'), threshold=ST.allSource_threshold, device=DEV1):
    #点击添加设备
    touch([350, 320], device=DEV1)
    #点击搜索设备
    touch([404, 390], device=DEV1)
    
    #让手机设备处于可发现状态
    Phone_CanBeFind
    
    #车机侧查找设备并连接蓝牙
    while(1):
        if exists(Template('pic/手机名称设备.png'), threshold=ST.allSource_threshold, timeout=10, device=DEV1):
            touch(Template('pic/手机名称设备.png'), threshold=ST.allSource_threshold, timeout=10,device=DEV1)
            break
        else:
            touch_if(Template('pic/BT_Search.png'), threshold=ST.allSource_threshold, device=DEV1)
            flick([856, 555], DIR_UP, step=1, speed=SPEED_NORMAL, device=DEV1)
    sleep(1)        
    if exists(Template('pic/蓝牙配对弹框.png'), threshold=ST.allSource_threshold, device=DEV1):
        touch(Template('pic/BT_确定连接按钮.png'), threshold=ST.allSource_threshold, device=DEV1)
        
        #手机侧确认连接
        if exists(Template('pic/phone_蓝牙配对请求.png'), device=DEV3):
        #点击确定
            touch([778, 1965], device=DEV3)
        
        touch(Template('pic/AA确认启用弹框.png'), threshold=ST.allSource_threshold, device=DEV1)
        touch(Template('pic/开始按钮.png'), threshold=ST.allSource_threshold, device=DEV1)
        touch(Template('pic/BT_完成连接按钮.png'), threshold=ST.allSource_threshold, device=DEV1)
        
        #手机侧点击允许
        for i in range(2):
            touch_if(Template('pic/phone_允许.png'),  timeout=10, device=DEV3)
    else:
        error(errType)  
        


    






    
    
    
    
