from autost.api import *
DEV1 = ST.DEV1

for i in range(2):
    keyevent(HOME, device=DEV1)

touch(Template("pic/菜单按钮.png"), threshold=ST.allSource_threshold)
touch(Template("pic/BT图标.png"), threshold=ST.allSource_threshold)
if exists(Template('pic/蓝牙未连接.png'), threshold=ST.allSource_threshold):
    #点击蓝牙图标   
    touch([230, 626])
    touch(Template('pic/配对设备列表.png'), threshold=ST.allSource_threshold)
    touch(Template('pic/A_MB_0056.png'), threshold=ST.allSource_threshold)
    #蓝牙音频
    touch([1185, 388])
    # 确定
    touch([1121, 157])
    #确定
    touch([617, 467])
else:
    pass
    
    
    
    

    

