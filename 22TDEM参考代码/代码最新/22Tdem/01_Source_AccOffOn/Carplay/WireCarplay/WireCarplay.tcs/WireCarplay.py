from autost.api import *

DEV1 = ST.DEV1
ST.am +=1
checkImage = Template('')
errType = 'acc_WireCarplay_error'

def check(on_sleep):
    if exists(checkImage, threshold=ST.allSource_threshold, timeout=2, device=DEV1):
        pass
    else:
        error(errType)
        
    sleep(on_sleep)
 
def playWireCarplay():
    global checkImage
    if exists(Template("pic/WireCp_Connected.png"), threshold=ST.allSource_threshold, timeout=5,device=DEV1):
        #进入carplay画面
        touch([269, 384])
        #进入主画面
        touch([70, 647])
        #播放音乐
        touch_if(Template("pic/音乐图标.png"), threshold=ST.allSource_threshold, device=DEV1)
        if exists(Template("pic/播放列表.png"), threshold=ST.allSource_threshold, timeout=5, device=DEV1):
            touch([378, 195])
            touch([429, 310])
        touch_if(Template("pic/播放中.png"), threshold=ST.allSource_threshold, device=DEV1)
        if exists(Template("pic/播放按钮.png"), threshold=ST.allSource_threshold, device=DEV1):
            touch(Template("pic/播放按钮.png"), threshold=ST.allSource_threshold, device=DEV1)
        else:
            pass
        sleep(1)
    checkImage = snapshot(rect=ST.eare_tuner, device=DEV1)

for i in range(2):
    keyevent(HOME, device=DEV1)
usb_on(3) 
playWireCarplay()

onT=0
if ST.am < ST.testTimes:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.am
    onT = ST.source_on_sleep_start + ST.am
else:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.am
    onT = ST.source_on_sleep_start + ST.am
    ST.am = 0
do_segment(Segment('../../../../common/reStart.tcs'))

check(onT)
#复归车机状态：断开carplay连接
usb_off(3)





    
    
