from autost.api import *
DEV1=ST.DEV1

checkImage = Template('')
errType = 'acc_WireCarplay_5s_error'

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


#重置重启睡眠时间
ST.acc_off_sleep_time = ST.acc_off_sleep_start
#重启
do_segment(Segment("../../../../common/reStart.tcs"))
#确认复归
check(ST.source_on_sleep_start)
#复归车机状态：断开carplay连接
usb_off(3)




    
    
