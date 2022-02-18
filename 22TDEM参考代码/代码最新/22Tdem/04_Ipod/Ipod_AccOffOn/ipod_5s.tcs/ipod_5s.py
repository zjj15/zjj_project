from autost.api import *

DEV1 = ST.DEV1
checkImage = Template('')
errType = 'acc_Ipod_error'

#测试前需要手动将iphone里的carplay禁用掉
def check(on_sleep):
    if exists(checkImage,threshold=ST.allSource_threshold,timeout=2, device=DEV1):
        pass
    else:
        error(errType)
 
    sleep(on_sleep)
 
def playIpod():
    global checkImage
    touch(Template("pic/菜单按钮.png"), threshold=ST.allSource_threshold)
    flick([1202, 355], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    touch(Template('pic/ipod图标.png'), threshold=ST.allSource_threshold)
    if exists(Template("pic/ipod_确认播放.png"), threshold=ST.allSource_threshold):
        print('playing bt music')
    else:
        error(errType)
    
    checkImage = snapshot(rect=ST.eare_devices2, device=DEV1)
 
for i in range(2):
    keyevent(HOME, device=DEV1)
usb_on(3)
playIpod()
#重置重启睡眠时间
ST.acc_off_sleep_time = ST.acc_off_sleep_start
#重启
do_segment(Segment('../../../common/reStart.tcs'))
#确认复归
check(ST.source_on_sleep_start)
#状态复归
usb_off(3)

