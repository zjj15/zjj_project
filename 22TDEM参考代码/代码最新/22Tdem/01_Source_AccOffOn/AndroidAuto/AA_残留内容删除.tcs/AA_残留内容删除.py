from autost.api import *
DEV1=ST.DEV1

for i in range(2):
    keyevent(HOME, device=DEV1)
#touch 快捷列表框
touch([664, 411])
#touch 系统框
touch([156, 244])

if exists(Template('pic/设备列表.png'), threshold=ST.allSource_threshold, timeout=10, device=DEV1):
    touch(Template('pic/设备列表.png'), threshold=ST.allSource_threshold, timeout=10, device=DEV1)

for i in range(3):
    if exists(Template('pic/删除图标.png'), threshold=ST.allSource_threshold, timeout=5, device=DEV1):
        touch(Template('pic/删除图标.png'), threshold=ST.allSource_threshold, timeout=5, device=DEV1)
        if exists(Template('pic/确认删除弹框.png'), threshold=ST.allSource_threshold, timeout=10, device=DEV1):
            touch([465, 478])
    else:
        break
    

