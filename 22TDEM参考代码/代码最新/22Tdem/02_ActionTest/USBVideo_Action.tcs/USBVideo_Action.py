from autost.api import *

DEV1 = ST.DEV1
DEV2 = ST.DEV2
checkImage_Default = 'pic/USBV_On.png'
#设置初始状态
rev_off()
ill_off()
spd_speed(0)

def checkDisp(checkImage=checkImage_Default):
    if not exists(Template('pic/上一曲按钮.png'), threshold=ST.allSource_threshold, timeout=5):
        print('当前是全屏状态')
        #解除全屏
        touch([574, 97])
    if exists(Template(checkImage), threshold=ST.allSource_threshold, timeout=1, device=DEV1):
        return True
    else:
        return False
 
def setError(errType):
    error(errType)

def test():
    errStr = ''
    #ILL
    errStr = "error_USBVideo_ill"
    ill_on()
    sleep(2)

    if not checkDisp('pic/ILL_On_Video_On.png'):
        setError(errStr)
 
    ill_off()
    sleep(2)
    if not checkDisp():
        setError(errStr)

    #SPD+PKB
    spd_pkb()
 
    #REV
    do_segment(Segment('../../common/rev_on_off.tcs'))

def spd_pkb():
 
    spd_speed(0)

    #case 1:[PKB:OFF + SPD:0] SPD:0->10->0[km/h]
    sleep(1)
    spd_speed(10)
    sleep(1)
    errStr = "error_SPD_PKB"
    checkImage='pic/SPD_Limit.png'
    #check into run limit
    if not checkDisp(checkImage):
        setError(errStr)

    #case 2:[PKB:OFF + SPD:10] SPD:10->0[km/h]
    spd_speed(0)
    sleep(1)
    #check relieve run limit
    if checkDisp(checkImage) and not checkDisp():
        setError(errStr)
 
    #case 3:[PKB:OFF + SPD:10] SPD:10->PKN:ON[km/h]
    sleep(1)
    spd_speed(10)
    sleep(1)
    errStr = "error_SPD_PKB"
    checkImage='pic/SPD_Limit.png'
    #check into run limit
    if not checkDisp(checkImage):
        setError(errStr)

    pkb_on()
    #check relieve run limit
    if checkDisp(checkImage) and not checkDisp():
        setError(errStr)
 
    #case 4:[PKB:ON + SPD:0] SPD:0->10[km/h]
    #set status
    pkb_off()
    spd_speed(0)
    pkb_on()
 
    sleep(2)
    spd_speed(10)
    sleep(2)
    errStr = "error_SPD_PKB"
    checkImage='pic/SPD_Limit.png'
    #check into run limit
    if checkDisp(checkImage):
        setError(errStr)

for i in range(2):
    keyevent(HOME, device=DEV1)
usb_on(1)
touch(Template('pic/菜单按钮.png'), threshold=ST.allSource_threshold)
if exists(Template('pic/USB卡片.png'), threshold=ST.allSource_threshold):
    for i in range(2):
        touch([478, 480])
    touch([482, 346])
    if not exists(Template('pic/上一曲按钮.png'), threshold=ST.allSource_threshold, timeout=5):
        print('当前是全屏状态')
        #解除全屏
        touch([574, 97])
    elif exists(Template('pic/USB_Audio.png'), threshold=ST.allSource_threshold):
        pass
    else:
        touch(Template('pic/USB_Video.png'), threshold=ST.allSource_threshold)
    touch_if(Template('pic/播放按钮.png'), threshold=ST.allSource_threshold)
    if exists(Template('pic/暂停按钮.png'), threshold=ST.allSource_threshold):
        print('video playing')
    else:
        print('video not playing')
 
test()

#复归
usb_off(1)
 

